import random, math
from node import PlotNode
import chess.features as features 
import re

class PlotIterator(object):
  """Iterates through the plot tree"""
  def __init__(self, plotNodes, chessGame=None, plotDepth=15):
    super(PlotIterator, self).__init__()
    self.plotNodes = plotNodes
    self.game = chessGame
    self.maxDepth = plotDepth
    self.plotDepth = 0
    if (chessGame):
      self.__setupGame__()

  def __setupGame__(self):
    #determine group dist
    moves = self.game.getMoveTuples()
    maxDepth = self.maxDepth
    numMoves = len(moves)
    mpg = numMoves / maxDepth
    r = numMoves - maxDepth*mpg
    
    # make moveGroups
    self.moveGroups = []
    counts = [mpg + (i < r) for i in range(maxDepth)]
    total = 0
    for count in counts:
      self.moveGroups.append(moves[total:total+count])
      total += count

  def chooseNodeWithMoves(self, nodeIds, moves):
    if (moves):
      moveFeatures = features.getFeatures(moves)
    else: 
      if (self.game.outcome[0]):
        moveFeatures = ([features.DEFEAT],[features.SAFETY])
      else:
        moveFeatures = ([features.SAFETY],[features.DEFEAT])
    print moveFeatures
    bestMatch = None 
    bestScore = -100
    for nodeId in nodeIds:
      score = 0
      nodeFeatures = self.plotNodes[nodeId].features
      for feat in nodeFeatures:
         if feat in moveFeatures[0]:
            score += 1
      score -= math.fabs( len(nodeFeatures) - len(moveFeatures[0]) )
#print score, nodeId, nodeFeatures, self.plotNodes[nodeId].name 
      if score > bestScore:
         bestScore = score
         bestMatch = [self.plotNodes[nodeId]]
      elif score == bestScore:
         bestMatch.append( self.plotNodes[nodeId] )

    r = random.choice( bestMatch )
    print r.name
    return r 

  def getNextNode(self, currentNode):
    if (self.game):
      # Get set of chess moves for plot depth
      if self.plotDepth < self.maxDepth:
        moveGroup = self.moveGroups[self.plotDepth]
        self.plotDepth += 1
      else:
        moveGroup = None
      # use the group of moves to make decision
      return self.chooseNodeWithMoves(currentNode.nextNodes, moveGroup)
    else:
      nextNodeId = random.choice(currentNode.nextNodes)
      return self.plotNodes[nextNodeId]

  def generatePlot(self):
    plot = ""
    if self.plotNodes:
        self.plotDepth = 0
        currentNode = self.plotNodes[0]
        plot += currentNode.name + '\n'
        while (currentNode.nextNodes):
            currentNode = self.getNextNode(currentNode)
            plot += currentNode.name + '\n'
    else:
      print "Error: no plot"
    return plot


  def generateStory(self, debug=False):
    story = ""
    if self.plotNodes:
        currentNode = self.plotNodes[0]
        story += currentNode.generateText() + '\n'
        while (currentNode.nextNodes):
            currentNode = self.getNextNode(currentNode)
            story += currentNode.generateText() + '\n'
    else:
      print "Error: no plot"
    return story


if __name__ == "__main__": 
  print "Self-test not implemented"     
