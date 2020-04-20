from pprint import pprint
from typing import Dict
from random import randrange
from pymongo import MongoClient


class MongoConnector:

    def __init__(self):
        self.client = MongoClient(host=['localhost:27017'])
        self.db = self.client.quiz

    def insert(self, data: Dict):
        return self.db.questions.insert_one(data)

    def get(self, data: Dict):
        return self.db.questions.find_one(data)

    def get_random(self):
        number = self.db.questions.count()
        random = randrange(number)
        return self.db.questions.find().limit(1).skip(random)
