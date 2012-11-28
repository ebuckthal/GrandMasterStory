import random
from chess.game import ChessGame
from chess.board import Piece

gameDicts = eval(open("gameData.chs","rb").read())
game = ChessGame(random.choice(gameDicts))
game.printMoves()
print game.info()

# p = game.mostActivePieces(1)[0]
# moves = game.movesForPiece(p)

# print Piece.name[p]
# for move in moves:
#     move.printMove()