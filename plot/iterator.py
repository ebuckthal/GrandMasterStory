import random, math
from collections import Counter
from node import PlotNode
import chess.features as features 
import re

class PlotIterator(object):
  """Iterates through the plot tree"""
  def __init__(self, plotNodes, chessGame=None, whitesView=True, plotDepth=15, separator='\n', debug=False):
    super(PlotIterator, self).__init__()
    self.plotNodes = plotNodes
    self.game = chessGame
    self.maxDepth = plotDepth
    self.plotDepth = 0
    self.whitesView = whitesView
    self.separator = separator
    self.debug = debug
    self.overallFeatures = []
    self.pastFeatures = Counter() 
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

   # add to overAllFeatures

    self.overallFeatures.append({ 'victory': ((self.game.outcome[0] and self.whitesView) or (not self.game.outcome[0] and not self.whitesView)) })
    #print self.overallFeatures

  def getMoveFeatures(self, moves):
    if (moves):
      if self.whitesView:
        return features.getFeatures(moves)[0]
      else:
        return features.getFeatures(moves)[1]
    else: 
      if ((self.game.outcome[0] and self.whitesView) or (not self.game.outcome[0] and not self.whitesView)):
        return [features.SAFETY]
      else:
        return [features.DEFEAT]

  def chooseNodeWithMoves(self, nodeIds, moves):

    moveFeatures = self.getMoveFeatures(moves)

    #this keeps track of all features that we have seen so far in the GAME, not necessarily in the PLOT
    self.pastFeatures.update(moveFeatures)

    bestMatch = None 
    bestScore = -100
      
    for nodeId in nodeIds:
      if (self.plotNodes[nodeId].empty):
        continue
      score = 0
      nodeFeatures = self.plotNodes[nodeId].features

      for feat in nodeFeatures:
         if feat in moveFeatures:
            score += 1
      score -= math.fabs( len(nodeFeatures) - len(moveFeatures) ) 
      if score > bestScore:
         bestScore = score
         bestMatch = [self.plotNodes[nodeId]]
      elif score == bestScore:
         bestMatch.append( self.plotNodes[nodeId] )

    r = random.choice( bestMatch )
    r.moveGroupFeatures = moveFeatures;
    if self.debug:
      print r.name, r.features, moveFeatures
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
            plot += currentNode.name + '\n' + currentNode.features + '\n'
    else:
      print "Error: no plot"
    return plot


  def generateStory(self, debug=False):
    story = ""
    if self.plotNodes:
        currentNode = self.plotNodes[0]
        story += currentNode.generateText(self.overallFeatures, self.pastFeatures) + self.separator
        while (currentNode.nextNodes):
            currentNode = self.getNextNode(currentNode)
            story += currentNode.generateText(self.overallFeatures, self.pastFeatures) + self.separator
    else:
      print "Error: no plot"
    return story


if __name__ == "__main__": 
  print "Self-test not implemented"     
