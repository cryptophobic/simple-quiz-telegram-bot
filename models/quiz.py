import csv
import re
from pprint import pprint
from random import randrange

from components.mongodb_connector import MongoConnector
from config.config import csv_quiz_path


class Quiz:

    def __init__(self):
        self.mongo = MongoConnector()
        self.current_question = None
        self.words = list()

    def quiz_load(self):
        with open(csv_quiz_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            for row in reader:
                self.mongo.insert(
                    {
                        'question': row[0],
                        'answer': row[1]
                    }
                )

    def get_current_question(self):
        if self.current_question is None:
            self.next_question()
        return self.current_question['question']

    def get_current_answer(self):
        if self.current_question is None:
            self.next_question()
        return self.current_question['answer']

    def display_answer(self):
        distorted_answer = list(re.sub(r'[^\s]', '*', self.get_current_answer()))
        number = len(distorted_answer)

        for word_index in self.words:
            distorted_answer[word_index] = self.get_current_answer()[word_index]

        random = randrange(number) - 1
        self.words.append(random)

        return "".join(distorted_answer)

    def match_answer(self, answer):
        return self.get_current_answer().lower() == answer.lower()

    def attempts_number(self):
        return len(self.words)

    def next_question(self):
        self.words = list()
        self.current_question = self.get_random_question()

    def get_random_question(self):
        res = self.mongo.get_random()
        return res[0]
