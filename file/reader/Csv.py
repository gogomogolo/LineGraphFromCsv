import csv


class Csv(object):
    def __init__(self, path):
        self.path = path
        self.output = []

    def read(self):
        if len(self.output) == 0:
            with open(self.path, 'r') as file:
                content = csv.reader(file, delimiter=',')
                for row in content:
                    self.output.append(row)
        return self.output
