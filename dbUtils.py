from pymongo import MongoClient

__author__ = 'matthew.farrugia'

class dbUtils:

    @staticmethod
    def connect(host, port=27017, username='', password=''):
        client = MongoClient(host,port)
        db = client.xawertajm_db
        db.current_weather


    @staticmethod
    def insert(content):

        return none;