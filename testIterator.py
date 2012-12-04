from plot.iterator import PlotIterator
import chess.game
#import skins.RomeoAndJuliet as skin
import skins.Zombie as skin
#import skins.WarStory as skin

game = chess.game.randomGame()
iterator = PlotIterator(skin.plot, game)
print iterator.generatePlot()