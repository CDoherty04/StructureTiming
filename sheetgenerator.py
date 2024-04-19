import openpyxl
from openpyxl.chart import LineChart, Reference
from openpyxl.chart.text import RichText
from openpyxl.drawing.text import RichTextProperties, Paragraph, ParagraphProperties, CharacterProperties


class Worksheet:
    """Creates an Excel worksheet and manages the data within it"""

    def __init__(self, file_name):
        self.file_name = file_name

        # Create worksheet
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active

    def plot(self, iterations, time):
        """Creates a point, with the x-value being the number of iterations, and the y-value being the elapsed time"""

        self.sheet.append([iterations, time])

    def create_graph(self):
        """Sets the properties of the Excel sheet, generates the graph, and saves the file"""

        # Create a Reference object
        values = Reference(self.sheet, min_col=2, min_row=1, max_col=2, max_row=100)

        # Create object of LineChart class
        chart = LineChart()
        chart.add_data(values)

        # Set the chart properties
        chart.title = self.file_name
        chart.legend = None
        chart.x_axis.title = "Iterations"
        chart.y_axis.title = "Time (ns)"
        chart.x_axis.txPr = RichText(bodyPr=RichTextProperties(rot="1"),
                                     p=[Paragraph(pPr=ParagraphProperties(defRPr=CharacterProperties()),
                                                  endParaRPr=CharacterProperties())])

        # Add chart to the sheet. The top-left corner of a chart is anchored to cell D2.
        self.sheet.add_chart(chart, "D2")

        # Save the file
        self.wb.save(f"{self.file_name}.xlsx")


if __name__ == "__main__":

    # Create test worksheet
    test_ws = Worksheet("Test")

    # Add various points
    for i in range(100):
        test_ws.plot(i, i ** 2)

    # Save data and graph it
    test_ws.create_graph()
