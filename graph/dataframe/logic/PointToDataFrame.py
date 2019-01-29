import pandas as pd


class PointToDataFrame(object):
    def convert(self, points):
        x_values = []
        y_values = []

        for point in points:
            x_values.append(getattr(point, 'x'))
            y_values.append(getattr(point, 'y'))

        return pd.DataFrame({'x': x_values, 'y': y_values})
