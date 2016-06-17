from pymongo import MongoClient

__author__ = 'matthew.farrugia'

class dbUtils:

    @staticmethod
    def set_collection(value):
        global collection
        collection = value

    @staticmethod
    def get_collection():
        return collection

    @staticmethod
    def connect(host, port=27017, username='', password=''):
        #client = MongoClient("mongodb://" + username + ":" + password + "@" + host + ":" + port.__str__())
        client = MongoClient(host,port)
        db = client.xawertajm_db
        db.authenticate(username, password)
        coll = db.current_weather
        coll.insert_one({"key" : "value"})
        #dbUtils.set_collection(coll)
        return coll


    @staticmethod
    def insert(content):

        return collection.insert_one(content);