import random

class PlotNode(object):
    """An action in the plot"""
    def __init__(self, name, nextNodes, features, templates, wordset):
        super(PlotNode, self).__init__()
        self.name = name
        self.nextNodes = nextNodes
        self.features = features
        self.templates = templates
        self.wordset = wordset
        
    def generateText(self):
        #optionally pass in features of move for smarter templating
        return random.choice(self.templates)