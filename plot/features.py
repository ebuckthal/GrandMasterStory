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
  # for move in game.moves()
  #   featureWeights[DRAMATIC] = getDramaticWeight(move)
  #   featureWeights[DEATH] = getDeathWeight(move)
  #   etc. for all features
  #   weightVector.append(featureWeights)
  #   featureWeights.clear()

  return weightVector

def getDramaticWeight(move):
  pass

def getDeathWeight(move):
  pass

def getTravelWeight(move):
  pass 

# 
# more feature weightings 
# 
