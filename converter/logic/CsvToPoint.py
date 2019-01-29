from converter.model.Point import Point


class CsvToPoint(object):
    def __init__(self, xlabel, ylabel):
        self.xlabel = xlabel
        self.ylabel = ylabel

    def convert(self, output):
        points = []

        line_count = 0
        xlabel_index = -1
        ylabel_index = -1

        for row in output:
            if line_count == 0:
                xlabel_index = row.index(self.xlabel)
                ylabel_index = row.index(self.ylabel)
                line_count += 1
            else:
                points.append(Point(row[xlabel_index], row[ylabel_index]))
                line_count += 1

        return points