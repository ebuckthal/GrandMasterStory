import chessgame, random
from chessgame import ChessGame

gameDicts = eval(open("gameData.chs","rb").read())
game = ChessGame(gameDicts[0]) #ChessGame(random.choice(gameDicts))
print game.info()