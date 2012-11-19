import random
from chess.game import ChessGame

gameDicts = eval(open("gameData.chs","rb").read())
game = ChessGame(random.choice(gameDicts))
print game.info()