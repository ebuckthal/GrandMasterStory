from plot.iterator import PlotIterator
#import skins.RomeoAndJuliet as skin
import skins.WarStory as skin

iterator = PlotIterator(skin.plot)
print iterator.generateStory()