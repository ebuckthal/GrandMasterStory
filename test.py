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