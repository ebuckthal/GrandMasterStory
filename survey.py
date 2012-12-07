from plot.iterator import PlotIterator
import chess.game
import skins.Zombie
import random

print "=============== INSTRUCTIONS! =================\n"

print "One of the stories is generated from the chess game, the other is generated from a random chess game.\n"

print "Go to http://chesstempo.com/pgn-viewer.html (or Google for PGN Viewer) and COPY-PASTE the PGN notation into the text field. The PGN viewer will automatically walk through the game for you.\n"

print "Guess which chess game generated the story! Thanks for you help!\n"

for s in range(50):


  game = []
  game.append(chess.game.randomGame())
  game.append(chess.game.randomGame())

  
  print "|||||||||||||||||||||||||||||||||||||||||||||||||||"
  print "|||||||||||||||| S U R V E Y %02d |||||||||||||||||||" % (s) 
  print "|||||||||||||||||||||||||||||||||||||||||||||||||||\n"
  
  i = 0
  for g in game:
    pgn = g.makePGN()
    if pgn.endswith('1/2'):
      pgn = pgn[:-3]

    print "--------- BEGINNING OF PGN %d for %02d ---------\n" % (i, s)
    print pgn
    print "\n----------- END OF PGN %d for %02d -------------\n" % (i, s)
    i = i + 1
  
  iterator = PlotIterator(skins.Zombie.plot, game[random.randint(0,len(game)-1)], separator="\n\n")
  print iterator.generateStory()
  
  print "|||||||||||||||||||||||||||||||||||||||||||||||||||"
  print "|||||||||| E N D  O F  S U R V E Y %02d |||||||||||||" % (s)
  print "|||||||||||||||||||||||||||||||||||||||||||||||||||\n"

  reload(skins.Zombie)
  

