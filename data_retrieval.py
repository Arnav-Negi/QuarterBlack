from pprint import pprint
from pymongo import MongoClient
import bcrypt

def return_db(db_name):
    CONNECTION_STRING = "mongodb://quarterblack:1@ac-qps7ry1-shard-00-00.e0vyjcs.mongodb.net:27017,ac-qps7ry1-shard-00-01.e0vyjcs.mongodb.net:27017,ac-qps7ry1-shard-00-02.e0vyjcs.mongodb.net:27017/?ssl=true&replicaSet=atlas-7weo1b-shard-0&authSource=admin&retryWrites=true&w=majority"

    client = MongoClient(CONNECTION_STRING)

    return client[db_name]

# returns data as disctionary if email already exists
# returns None otherwise
def retrieve_seat(email, collection_name = return_db("password_db")["stored_passwords"]):
    email_exists = collection_name.find_one({"email": email})

    if not email_exists:
        return None

    return email_exists

if __name__ == "__main__":
    dbname = return_db("password_db")

    pprint(retrieve_seat('abc'))