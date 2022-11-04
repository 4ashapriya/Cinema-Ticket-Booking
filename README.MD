This is a python project for Cinema ticket booking with the following features:

# Business Rules
​
    - There are 3 types of tickets i.e. Infant, Child, and Adult.
    - The ticket prices are based on the type of ticket (see table below).
    - The ticket purchaser declares how many and what type of tickets they want to buy.
    - Multiple tickets can be purchased at any given time.
    - Only a maximum of 20 tickets that can be purchased at a time.
    - Infants do not pay for a ticket and are not allocated a seat. They will be sitting on an Adult's lap.
    - Child and Infant tickets cannot be purchased without purchasing an Adult ticket.

- Considers the above objective, business rules, constraints & assumptions.
- Calculates the correct amount for the requested tickets and makes a payment request to the `TicketPaymentService`.  
- Calculates the correct no of seats to reserve and makes a seat reservation request to the `SeatReservationService`.  
- Rejects any invalid ticket purchase requests. It is up to you to identify what should be deemed as an invalid purchase request.

# This project uses Flask framework and it starts from main.py.
# To run the project first install the requirements using the command pip install -r requirements.txt then run the command python main.py
# All the DB configurations can be found in \cinema-tickets-python\configurations\database.ini
# This uses pytest for the test automation and the result can be found in \cinema-tickets-python\test\reports
