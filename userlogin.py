from pymongo import MongoClient
import bcrypt

def return_db(db_name):
    CONNECTION_STRING = "mongodb://quarterblack:1@ac-qps7ry1-shard-00-00.e0vyjcs.mongodb.net:27017,ac-qps7ry1-shard-00-01.e0vyjcs.mongodb.net:27017,ac-qps7ry1-shard-00-02.e0vyjcs.mongodb.net:27017/?ssl=true&replicaSet=atlas-7weo1b-shard-0&authSource=admin&retryWrites=true&w=majority"

    client = MongoClient(CONNECTION_STRING)

    return client[db_name]

# return

def check_record(collection_name, email, password):
    email_exists = collection_name.find_one({"email": email})

    if not email_exists:
        return -1

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    passwordhash = email_exists["password"]
    if not bcrypt.checkpw(password.encode('utf-8'), passwordhash):
        return -1

    return 1

if __name__ == "__main__":
    dbname = return_db("password_db")

    print(check_record(dbname["stored_passwords"], "abc", "xyz"))

    

    