import csv


class Csv(object):
    def __init__(self, path):
        self.path = path
        self.output = []

    def read(self):
        if len(self.output) == 0:
            with open(self.path, 'r') as file:
                self.output = csv.reader(file, delimeter=',')
        return self.output
