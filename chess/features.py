import math
import chess
from chess.move import ChessMove
from chess.game import ChessGame 
from chess.board import Piece
# Plot Features

DRAMATIC = "dramatic"
DANGER = 'danger'
HERO = 'hero'
TRAVEL = 'travel'
IMPORTANT_DEATH = 'importantDeath'
UNIMPORTANT_DEATH = 'unimportantDeath'
IMPORTANT_KILL = 'importantKill'
UNIMPORTANT_KILL = 'unimportantKill'
DEFEAT = 'defeat'
SAFETY = 'safety'
CHECK = "check"

#list of tuples of moves
def getFeatures(moves): 
  if moves == [] or moves == None:
    return {}
  bfeatureWeights = {}
  wfeatureWeights = {}
  wfeatures = [] 
  bfeatures = [] 
  wheros = []
  bheros = []
  wfeatureWeights[DRAMATIC] = 0
  wfeatureWeights[DANGER] = 0
  wfeatureWeights[TRAVEL] = 0
  bfeatureWeights[DRAMATIC] = 0
  bfeatureWeights[DANGER] = 0
  bfeatureWeights[TRAVEL] = 0
  for i in range(len(moves)):
    move_tup = moves[i]
    for move in move_tup:
      if (not move):
        continue
      if move.isWhite:
         wfeatureWeights[DRAMATIC] += getDramaticWeight(move)
         wfeatureWeights[DANGER] += getDangerWeight( move )
         wfeatureWeights[TRAVEL] += getTravelWeight(move)
      else:
         bfeatureWeights[DRAMATIC] += getDramaticWeight(move)
         bfeatureWeights[DANGER] += getDangerWeight( move )
         bfeatureWeights[TRAVEL] += getTravelWeight(move)

      death = getDeathWeight( move )
      if death == 1:
        if move.isWhite:
          wfeatures.append( UNIMPORTANT_DEATH )
          bfeatures.append( UNIMPORTANT_KILL )
        else:
          bfeatures.append( UNIMPORTANT_DEATH )
          wfeatures.append( UNIMPORTANT_KILL )
      if death > 1:
        if move.isWhite:
          wfeatures.append( IMPORTANT_DEATH )
          bfeatures.append( IMPORTANT_KILL )
        else:
          bfeatures.append( IMPORTANT_DEATH )
          wfeatures.append( IMPORTANT_KILL )

      if getCheckWeight(move) > 0:
        if move.isWhite:
          wfeatures.append( CHECK )
        else:
          bfeatures.append( CHECK )

      if getDefeatWeight( move ) > 0:
        if move.isWhite:
          wfeatures.append( SAFETY )
          bfeatures.append( DEFEAT )
        else:
          bfeatures.append( SAFETY )
          wfeatures.append( DEFEAT )
      if move.capture:
        if move.isWhite:
          if move.capture in wheros:
            wfeatures.append(HERO)
          else:
            wheros.append( move.capture )
        else:
          if move.capture in bheros:
            bfeatures.append(HERO)
          else:
            bheros.append( move.capture )
         

  if bfeatureWeights[DRAMATIC] / len(moves) > 2:
    bfeatures.append( DRAMATIC )
  if wfeatureWeights[DRAMATIC] / len(moves) > 2:
    wfeatures.append( DRAMATIC )
  if bfeatureWeights[TRAVEL] / len(moves) > 2:
    bfeatures.append( TRAVEL )
  if wfeatureWeights[TRAVEL] / len(moves) > 2:
    wfeatures.append( TRAVEL )
  if bfeatureWeights[DANGER] / len(moves) > 2:
    bfeatures.append( DANGER )
  if wfeatureWeights[DANGER] / len(moves) > 2:
    wfeatures.append( DANGER )
  
  return (set(wfeatures), set(bfeatures))
    

def getDramaticWeight(move):
   return len( move.features["Threatened Pieces"] )
def getDangerWeight(move):
   return len( move.features["Targeted Pieces"] )

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

