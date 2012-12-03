import math
import chess
from chess.move import ChessMove
from chess.game import ChessGame 
from chess.board import Piece
# Plot Features
DEATH = "death"
CHECK = "check"
DEFEAT = "checkMate"
TRAVEL = "travel"
TRAVEL_FAR = "travelFar"
DRAMATIC = "dramatic"

# Game features - used for word substitution in skins
DEATHOF = "@DEATHOF" #stores features.pieceType value
# Game Pieces
PAWN = "@PAWN"
ROOK = "@ROOK"
KNIGHT = "@KNIGHT"
BISHOP = "@BISHOP"
QUEEN = "@QUEEN"
KING = "@KING"

def getWeightVector(game): 
  weightVector = []
  featureWeights = {}
  for i in range(game.totalMoves):
    move = game.getMove(i)
    featureWeights[DRAMATIC] = getDramaticWeight(move)
    featureWeights[DEATH] = getDeathWeight(move)
    featureWeights[CHECK] = getCheckWeight(move)
    featureWeights[DEFEAT] = getDefeatWeight(move)
    featureWeights[TRAVEL] = getTravelWeight(move)
    featureWeights[TRAVEL_FAR] = 0
    weightVector.append(featureWeights)

  return weightVector

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

