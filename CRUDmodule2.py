# Justin Leger
# SNHU CS340
# 4/13/2025

from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password, host, port, db_name):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = password
        HOST = host
        PORT = port
        DB = db_name
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            isValid = self.database.animals.insert(data)  # data should be dictionary

            if isValid == 0:
                return True
            return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            data = self.database.animals.find(data, {"_id": False})
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        return data

#create method to implement the U in CRUD
    def update(self, dataS, dataU):
        if dataS is not None:
            myResult = self.database.animals.update_many(dataS, {"$set": dataU})
        else:
            return "{}"
        return myResult.raw_result

#create read method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            myResult = self.database.animals.delete_many(data)
        else:
            return "{}"
        return myResult.raw_result
