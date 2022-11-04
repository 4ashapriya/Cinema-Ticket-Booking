from flask import request, jsonify, render_template
from app import run_query, __ticket_details, api
from app.ticketservices.purchase_exceptions import InvalidPurchaseException
from app.seatbooking.seat_reservation_service import SeatReservationService
from app.paymentgateway.ticket_payment_service import TicketPaymentService
from flask_restx import Resource, fields


ticket_type_requests = api.model('Resources', {
    'adult_count': fields.Integer,
    'child_count': fields.Integer,
    'infant_count': fields.Integer,
    'date': fields.Date,
    'film':fields.String
})


@api.route('/get_tickets', methods=["POST"])
class TicketService(Resource):

    """

      purchase_tickets should be the only public method

    """

    def __init__(self, account_id = None, ticket_type_requests=None):
          self.account_id = account_id
          self.ticket_type_requests = ticket_type_requests

    def __get_movies(self):
        res = run_query("SELECT * FROM movies ORDER BY show_time")
        return res

    def __get_tickets(self):
          res = run_query("SELECT sum(no__of_tickets) FROM tickets")
          return res
    
    @api.expect(ticket_type_requests)
    def post(self, account_id=None, ticket_type_requests={}):
          ticket_type_requests=request.get_json(force=True)
          ticket_purchased = __get_tickets()
          ticket_info = __ticket_details()

          while ticket_purchased <= ticket_info["total_seat"]:
            if account_id >= 1 and ticket_type_requests["types"]["adult_count"] and sum(ticket_type_requests["types"].values()) <=20:
                  total_cost = ticket_type_requests["types"]["adult_count"] * ticket_info["adult_ticket"] + ticket_type_requests["types"]["child_count"] * ticket_info["child_ticket"] + ticket_type_requests["types"]["infant_count"] * ticket_info["infant_ticket"]
                  no_of_tickets = sum(ticket_type_requests["types"].values())
                  TicketPaymentService.make_payment(account_id, total_cost)
                  SeatReservationService.reserve_seat(account_id, no_of_tickets)
                  return {"message": "Congratulations"}
            else:
                raise InvalidPurchaseException  
          else:
            raise InvalidPurchaseException

