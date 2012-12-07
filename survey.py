from plot.iterator import PlotIterator
import chess.game
import skins.Zombie as skin
import random

game = []
game.append(chess.game.randomGame())
game.append(chess.game.randomGame())

iterator = PlotIterator(skin.plot, game[random.randint(0,len(game)-1)], separator="\n\n")

for g in game:
  pgn = g.makePGN()
  if pgn.endswith('1/2'):
    pgn = pgn[:-3]
  print pgn + '\n\n'

print iterator.generateStory()
