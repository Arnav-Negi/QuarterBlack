from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://quarterblack:ivehearditbothways@quarterblack.m3lf4hi.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGODB_URI)
db = client["Megathon"]
seats = db["seats"]

# check that email exists first
# insert a users preference for a seat for a given car type
def insert_seat_preference(email, inclination_angle, x_coord, y_coord, car_type = "sedan", massaging = False, bolstering = False):
    results = seats.find({
        "$and" : [
        {"email" : email},
        {"car_type" : car_type}
        ]})

    for x in results:
        query = {
            "$and" :[
            {"email" : email},
            {"car_type" : car_type}
            ]}
        newvalues = {"$set" : {"inclination_angle" : inclination_angle, "x_coord" : x_coord, "y_coord" : y_coord, "massaging" : massaging, "bolstering" : bolstering}}
        seats.update_one(query, newvalues)
        return

    seats.insert_one({"email" : email, "inclination_angle" : inclination_angle, "x_coord" : x_coord, "y_coord" : y_coord, "car_type" : car_type,  "massaging" : massaging, "bolstering" : bolstering})

# insert_seat_preference("abc", 2.1, 2.1, 2.1, "hatchback")