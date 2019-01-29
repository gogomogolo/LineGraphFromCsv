import util.GraphUtil as GraphUtil
from graph.component.Line import Line


class LinePlot(object):
    def __init__(self, title, xlabel, ylabel, dataframe_logic):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.dataframe_logic = dataframe_logic

    def save(self, draw_path, y_to_objects_map, y_to_color_map):
        plot = GraphUtil.create_plot(title=self.title, xlabel=self.xlabel, ylabel=self.ylabel)

        for ylabel_id in y_to_objects_map:
            data_frame = self.dataframe_logic.convert(y_to_objects_map[ylabel_id])
            line = Line(self.xlabel, self.ylabel, data_frame,
                        y_to_color_map[ylabel_id], 'o', 2)
            GraphUtil.add_line_to_plot(plot, line)

        GraphUtil.write_plot_to_file(plot, draw_path)
        GraphUtil.clear_plot(plot)
