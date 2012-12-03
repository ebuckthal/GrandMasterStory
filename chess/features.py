import math
import chess
from chess.move import ChessMove
from chess.game import ChessGame 
from chess.board import Piece
# Plot Features

DRAMATIC = "dramatic"
HERO = 'hero'
TRAVEL = 'travel'
IMPORTANT_DEATH = 'importantDeath'
UNIMPORTANT_DEATH = 'unimportantDeath'
IMPORTANT_KILL = 'importantKill'
UNIMPORTANT_KILL = 'unimportantKill'
DEFEAT = 'defeat'
SAFTY = 'safty'
DANGER = 'danger'
CHECK = "check"

#list of tuples of moves
def getFeatures(moves): 
  if moves == [] or moves == None:
    return {}
  bfeatureWeights = {}
  wfeatureWeights = {}
  wfeatures = [] 
  bfeatures = [] 
  for i in range(len(moves)):
    move_tup = game.getMove(i)
    for move in move_tup:
      if move.isWhite:
         wfeatureWeights[DRAMATIC] += getDramaticWeight(move)
         wfeatureWeights[TRAVEL] += getTravelWeight(move)
      else:
         bfeatureWeights[DRAMATIC] += getDramaticWeight(move)
         bfeatureWeights[TRAVEL] += getTravelWeight(move)

      death = getDeathWeight( move )
      if death == 1:
        if move.isWhite:
          wfeatures.append( UNIMPORTANT_DEATH )
          bfeatures.append( UNIMPORTANT_kill )
        else:
          bfeatures.append( UNIMPORTANT_DEATH )
          wfeatures.append( UNIMPORTANT_kill )
      if death > 1:
        if move.isWhite:
          wfeatures.append( IMPORTANT_DEATH )
          bfeatures.append( IMPORTANT_kill )
        else:
          bfeatures.append( IMPORTANT_DEATH )
          wfeatures.append( IMPORTANT_kill )

      if getCheckWeight(move) > 0:
        if move.isWhite:
          wfeatures.append( CHECK )
        else:
          bfeatures.append( CHECK )

      if getDefeatWeight( move ) > 0:
        if move.isWhite:
          wfeatures.append( SAFTY )
          bfeatures.append( DEFEAT )
        else:
          bfeatures.append( SAFTY )
          wfeatures.append( DEFEAT )

  if bfeatureWeights[DRAMATIC] / len(moves) > 3:
    bfeatures.append( DRAMATIC )
  if wfeatureWeights[DRAMATIC] / len(moves) > 3:
    wfeatures.append( DRAMATIC )
  if bfeatureWeights[TRAVEL] / len(moves) > 2:
    bfeatures.append( TRAVEL )
  if wfeatureWeights[TRAVEL] / len(moves) > 2:
    wfeatures.append( TRAVEL )
  
  return (set(wfeatures), set(bfeatures))
    

#dramatic is 0 to 7 
def getDramaticWeight(move):
   rate = 0
   features = move.features
   threat = len( move.features["Threatened Pieces"] )
   target = len( move.features["Targeted Pieces"] )
   if threat > 1:
      rate +=2
   if threat > target:
      rate += 2

   if move.castling != None:
      rate += 1
   if move.whiteScore > move.blackScore and move.isWhite:
      rate += 2
   if move.whiteScore < move.blackScore and not move.isWhite:
      rate += 2
   return rate

#Death weight is 0-9 or 100
def getDeathWeight(move):
   if move.capture == None:
      return 0
   return Piece.value[move.capture]

#Check weight is 0 or 5
def getCheckWeight(move):
   if move.check:
      return 5
   return 0

# travel is the distance traveled 0 to 4
def getTravelWeight(move):
   if move.location == None or move.dest == None:
      return 0
   x = move.location[0] - move.dest[0]
   y = move.location[1] - move.dest[1]
   return int( math.sqrt( x*x + y*y ) )

# 0 or 100
def getDefeatWeight( move ):
   if move.mate:
      return 100
   return 0

