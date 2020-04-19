from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, n_data = 20):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.get_xaxis().set_visible(False)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        # FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.xdata = list(range(n_data))
        self.ydata = [0 for i in range(n_data)]
        self.axes.cla()  # Clear the canvas.
        self.axes.grid(True)
        self.axes.plot(self.xdata, self.ydata, 'r')

    def updateData(self, newData = {'t': 0,  'h':0}):
        newTemp = newData['t']
        self.ydata = self.ydata[1:] + [newTemp]
        self.axes.cla()  # Clear the canvas.
        self.axes.grid(True)
        self.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.draw()

    def compute_initial_figure(self):
        pass