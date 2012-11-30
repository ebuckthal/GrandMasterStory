import random
from node import PlotNode

class PlotIterator(object):
    """Iterates through the plot tree"""
    def __init__(self, plotNodes):
        super(PlotIterator, self).__init__()
        self.plotNodes = plotNodes

    def generateStory(self):
        story = ""
        if self.plotNodes:
            currentNode = self.plotNodes[0]
            while (currentNode.nextNodes):
                story += currentNode.generateText() + '\n'
                nextNodeId = random.choice(currentNode.nextNodes)
                currentNode = self.plotNodes[nextNodeId]
            story += currentNode.generateText() + '\n'
        else:
            print "Error: no plot"
        return story