import argparse

from converter.logic.CsvToPoint import CsvToPoint
from converter.type.ObjectConverter import ObjectConverter
from file.reader.Csv import Csv
from graph.dataframe.logic.PointToDataFrame import PointToDataFrame
from graph.draw.LinePlot import LinePlot

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="give input file or files path as -f <path_file1>,<path_file2>")
parser.add_argument("-x", "--x-field", help="give a field for selecting which field used for x axis")
parser.add_argument("-y", "--y-field", help="give a field for selecting which field used for y axis")
parser.add_argument("-c", "--line-color", help="give a color for lines in b,g,r,c,m,y,k,w as -c b,k")
parser.add_argument("-o", "--output-dir", help="give output directory path for draw")
parser.add_argument("-lx", "--label-x", help="label x axis")
parser.add_argument("-ly", "--label-y", help="label y axis")
parser.add_argument("-t", "--title", help="give title of the draw")

args = parser.parse_args()


def main():
    file = print(args.file)
    x_field = print(args.x_field)
    y_field = print(args.y_field)
    line_color = print(args.line_color)
    output_dir = print(args.output_dir)
    label_x = print(args.label_x)
    label_y = print(args.label_y)
    title = print(args.title)

    files = file.split(',')
    colors = line_color.split(',')

    y = 0
    y_to_objects = {}
    y_to_color = {}

    for f in files:
        y_id = 'y' + str(y)

        csv = Csv(f)
        csv_to_point = CsvToPoint(x_field, y_field)
        object_converter = ObjectConverter(csv, csv_to_point)
        y_to_objects[y_id] = object_converter.convert()
        y_to_color[y_id] = colors[y]

        y += 1

    data_frame_logic = PointToDataFrame()
    line_plot = LinePlot(title, label_x, label_y, data_frame_logic)
    line_plot.save(output_dir, y_to_objects, y_to_color)



main()
