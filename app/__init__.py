from configparser import SafeConfigParser
from flask import Flask
from flask_cors import CORS
import mysql.connector,sys
from mysql.connector import Error
from flask_restx import Api


app = Flask(__name__)
CORS(app)
config = SafeConfigParser()

api = Api(app, version='1.0', title='Cinema Tickets',
          description='A sample Cinem Tickets API',
          )


def __database_conf(self):
    config.read("configurations/database.ini")
    db_info = { "database_name" : config.get("MYSQL", "database"),
                    "db_host" : config.get("MYSQL", "host"),
                    "db_user" : config.get("MYSQL", "user"),
                    "password" : config.get("MYSQL", "password")}
    return db_info

def __ticket_details(self):
    config.read("configurations/ticket_details.ini")
    ticket_info = { "total_seat": config.get("TICKETS", "total_seat"),
                    "adult_ticket": config.get("TICKETS", "adult_ticket"),
                    "infant_ticket": config.get("TICKETS", "infant_ticket"),
                    "child_ticket": config.get("TICKETS", "child_ticket"),
                    "max_ticket": config.get("TICKETS", "max_ticket")}
    return ticket_info

def run_query(query):
    try:
        db_info = __database_conf()
        db = mysql.connector.connect(
			host= db_info["db_host"],
			database= db_info["database_name"],
			user= db_info["db_user"],
			password= db_info["password"])

        if db.is_connected():
            print("Connected to MySQL, running query: ", query)
            cursor = db.cursor(buffered = True)
            cursor.execute(query)
            db.commit()
            res = None
            try:
                res = cursor.fetchall()
            except Exception as e:
                print("Query returned nothing, ", e)
                return []
            return res

    except Exception as e:
        print(e)
        return e

    finally:
        db.close()

    print("Couldn't connect to MySQL Database")
    #Couldn't connect to MySQL
    return None

# To resolve the circular import error the app modules are imported here.
from app.ticketservices.ticket_service import TicketService

# endpoints
app.add_url_rule("/get_tickets", view_func=TicketService.as_view("Tickets"))
