import csv
from config.config import csv_quiz_path


class Quiz:

    @staticmethod
    def quiz_load():
        with open(csv_quiz_path) as csv_file:
            spamreader = csv.reader(csv_file, delimiter=',', quotechar='"')
            for row in spamreader:
                print(', '.join(row))
