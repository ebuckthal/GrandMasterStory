#from chess.game import ChessGame
#from chess.board import Piece
import chess
from story import Story

game = chess.game.randomGame()
#game.printMoves()
#print game.info()

story = Story(game)
story.readStory()

# p = game.mostActivePieces(1)[0]
# moves = game.movesForPiece(p)

# print Piece.name[p]
# for move in moves:
#     move.printMove()

def rateMove( move ):
   rate = 0
   if move.capture != None:
      rate += 4
   if move.check:
      rate += 5
   features = move.features
   threat = len(move.features["Threatened Pieces"])
   target = len( move.features["Targeted Pieces"])
   if threat > 1:
      rate += 2
   if threat > target:
      rate += 2
   if move.castling != None:
      rate += 1
   if move.whiteScore > move.blackScore and move.isWhite:
      rate += 2
   if move.whiteScore < move.blackScore and not move.isWhite:
      rate += 2
   return rate

moveRating = []
for i in range(game.totalMoves):
   moveRating.append( rateMove(game.getMove(i)) )

def filter_ratings( ratings ):
   ret = []
   for i in range( len(ratings) ):
      if i < 2:
         ret.append(ratings[i])
         continue
      if ratings[i] == ratings[i-1] and ratings[i] == ratings[i-2]:
         continue
      ret.append(ratings[i])
   return ret
def filter_dispare( ratings, m ):
   ret = [] 
   for i in range(0,len(ratings),2):
      if i + 1 < len(ratings)-1:
         if ratings[i] - ratings[i+1] >= m or ratings[i+1] - ratings[i] >= m:
            ret.append((ratings[i], ratings[i+1]))
            continue
         if ratings[i] >= 8 or ratings[i+1] >= 8:
            ret.append((ratings[i], ratings[i+1]))
   return ret

print moveRating, '\n'
print filter( lambda x: x >= 3, moveRating ), '\n'
print filter( lambda x: x >= 4, moveRating ), '\n'
print filter( lambda x: x >= 5, moveRating ), '\n'
print filter_ratings( moveRating )
print filter_dispare( moveRating, 3 )

