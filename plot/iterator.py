from node import PlotNode

class PlotIterator(object):
    """Iterates through the plot tree"""
    def __init__(self, arg):
        super(PlotIterator, self).__init__()
        self.arg = arg
        