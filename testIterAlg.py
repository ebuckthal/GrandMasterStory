from plot.iterator import PlotIterator
import skins.WarStory as skin
import chess.game

game = chess.game.randomGame()
iterator = PlotIterator(skin.plot, game)
print iterator.generateStory(debug=True)
