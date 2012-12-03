import random
from node import PlotNode
import features 
import re

class PlotIterator(object):
  """Iterates through the plot tree"""
  def __init__(self, plotNodes, chessGame=None):
    super(PlotIterator, self).__init__()
    self.plotNodes = plotNodes
    self.game = chessGame
    if (chessGame):
      self.weightList = features.getWeightVector(chessGame) 

  def searchNode(self, node, ):
    """Takes in a starting node initially and recursively 
    descends a plot tree looking for end story nodes. When an 
    end node is found, the path to the end from the current node 
    is returned. Multiple nodes can be returned if they are at the same 
    depth, although only the first ending found is returned. 
    
    Returns: a list of indices (choices) that must be taken to 
             arrive at the end node from the current node
    """
    #print "Beep"
    endChildren = []   
    followChildren = []
    for child in range(len(node.nextNodes)):
      #print node.nextNodes
      #print self.plotNodes[node.nextNodes[child]]
      #print self.plotNodes[node.nextNodes[child]].nextNodes
      if not self.plotNodes[node.nextNodes[child]].nextNodes:
        endChildren.append(child)
      else: 
        followChildren.append(child)

    if endChildren: 
      return endChildren

    # dont do this in the above loop because it would follow to the
    # tree even if we already have a solution. Can't return because we 
    # need all end children (which may not be at consecutive indices)
    for child in followChildren:
      #print node.nextNodes[child]
      return [child] + self.searchNode(self.plotNodes[node.nextNodes[child]])

  def findClosestEnd(self, root):
    path = self.searchNode(root)
    return path  

  def chooseNextNode(self, nodeList):
    options = [] 
    # only one option, pick it
    if len(nodeList) == 1:
      return 0
            
    for i in range(len(self.nextNodes)):
      highestValue = -1
      for featureWeights in self.weightList:
        total = sum([fWeight.values() for fWeight in self.weightList])
        if total == highestValue:
          options.append(weightList.index(featureWeights))
        elif total > highestValue:
          options = [weightList.index(featureWeights)]

    return random.choice(options)

  def filterMoves(self):
    aggregateStats = self.game.getGameStats()
    for key in aggregateStats:
      print aggregateStats[key]

  def generatePlot(self):
    plot = ""
    if self.plotNodes:
      currentNode = self.plotNodes[0]
      while (currentNode.nextNodes):
          plot += currentNode.name + '\n'
          nextNodeId = random.choice(currentNode.nextNodes)
          currentNode = self.plotNodes[nextNodeId]
      plot += currentNode.name + '\n'
    else:
      print "Error: no plot"
    return plot


  def generateStory(self, debug=False):
    story = ""
    if self.plotNodes:
      currentNode = self.plotNodes[0]
      if (self.game):
        for i in range(self.game.totalMoves):
          print "Generate Story Iteration %s" % i
          story += currentNode.generateText() + '\n'
          nextNodeId = self.chooseNextNode(currentNode.nextNodes)
          currentNode = self.plotNodes[nextNodeId]
          if self.plotNodes[nextNodeId].nextNodes is None:
            break
        # More plot items than significant moves
        if currentNode.nextNodes:
          path = self.findClosestEnd(currentNode)
          for step in path:
            story += currentNode.generateText() + '\n'
            currentNode = self.plotNodes[currentNode.nextNodes[step]]
          assert currentNode.nextNodes is None
      else: # no chess game
        while (currentNode.nextNodes):
          story += currentNode.generateText() + '\n'
          nextNodeId = random.choice(currentNode.nextNodes)
          currentNode = self.plotNodes[nextNodeId]
      #generate last node's text
      story += currentNode.generateText() + '\n'
    else:
      print "Error: no plot"
    return story


if __name__ == "__main__": 
  print "Self-test not implemented"     
