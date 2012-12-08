from plot.iterator import PlotIterator
import chess.game
import skins.Zombie
import random


f = open('surveyKey.txt', 'w+')


print "=============== INSTRUCTIONS! =================\n"

print "One of the stories is generated from the chess game, the other is generated from a random chess game.\n"

print "Go to http://chesstempo.com/pgn-viewer.html (or Google for PGN Viewer) and COPY-PASTE the PGN notation into the text field. The PGN viewer will automatically walk through the game for you.\n"

print "Guess which chess game generated the story! Thanks for you help!\n"

for s in range(20):

  sol = ''

  game = []
  game.append(chess.game.randomGame())
  game.append(chess.game.randomGame())

  
  print "|||||||||||||||||||||||||||||||||||||||||||||||||||"
  print "|||||||||||||||| S U R V E Y %02d |||||||||||||||||||" % (s) 
  print "|||||||||||||||||||||||||||||||||||||||||||||||||||\n"
  
  print "--------- BEGINNING OF PGN %02d ---------\n" % (s)
  choice = random.randint(0, len(game)-1)
  f.write(str(s) + ' ' + str(choice) + '\n')
  
  pgn = game[choice].makePGN()
  if pgn.endswith('1/2'):
    pgn = pgn[:-3]

  print pgn

  print "\n----------- END OF PGN %02d -------------\n" % (s)
  
  i = 1
  for g in game:
    iterator = PlotIterator(skins.Zombie.plot, g, separator="\n\n")
    print '============ BEGINNGING OF STORY %d ================' % (i)
    print iterator.generateStory()
    print '=============== END OF STORY %d ====================' % (i)
    i = i + 1
   
  
  
  print "|||||||||||||||||||||||||||||||||||||||||||||||||||"
  print "|||||||||| E N D  O F  S U R V E Y %02d |||||||||||||" % (s)
  print "|||||||||||||||||||||||||||||||||||||||||||||||||||\n"

  reload(skins.Zombie)
  
f.close()

