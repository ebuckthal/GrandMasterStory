import skin
import plot.features as features

#lists of words used by the templates
wordset = {
    }

#lists of templates used by the plot nodes
templates = [
]

nodes = [
  ("0 we're running through a office building and we find a bunch of weapons, pretty neat.", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], \
    [features.TRAVEL]), \
  
  ("1 Ted gets bit and turns into a zombie. He kills priness rainicorn before we kill him.", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.IMPORTANT_DEATH, features.IMPORTANT_KILL, features.DANGER, features.CHECK]), \
  
  ("2 remain in hiding, saw no zombies.", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    []), \
  
  ("3hiding out in place, slices a zombie's head off.", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.UNIMPORTANT_KILL, features.DANGER]), \
  
  ("4 hiding out, zombies break in and kill Ted, rest leave and go to new hiding area.", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.DRAMATIC, features.IMPORTANT_DEATH, features.UNIMPORTANT_DEATH]), \
  
  ("5 to protect the gang and ensure our safe survival, Ted distracts a group of zombies with a grenade strapped to himself. Ted dies.", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.HERO, features.IMPORTANT_DEATH, features.DRAMATIC, features.DANGER]), \
  
  ("6 princess ranicorn bot turns into a zombie", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.DANGER, features.UNIMPORTANT_DEATH]), \
  
  ("7 Ted sets up a bomb from a gasoline truck", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.DRAMATIC, features.HERO, features.DANGER, features.TRAVEL]), \
  
  ("8 Ted dies from a gasoline bomb truck he foolishly set up, but it kills quite a few zombies", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.HERO, features.IMPORTANT_DEATH, features.DRAMATIC, features.UNIMPORTANT_KILL]), \
  
  ("9 we're all really fucking scared", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    []), \
  
  ("10 Ted suggests that we all leave in the middle of the night to try to find a group of survivors", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.DANGER, features.TRAVEL]),\
  
  ("11 we find a radio and hear a message from humans looking for survivors", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.DRAMATIC, features.TRAVEL]), \
  
  ("12 ted got his arm bit off so we had to kill him before he turned into a zombie", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.IMPORTANT_DEATH, features.DANGER])\
  
  ("13 we are running low on the cheese we'd found from the cheese factory we're hiding in", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.DANGER, features.UNIMPORTANT_DEATH]), \
  
  ("14 the zombies broke in and we lost all our stuff, but we made it to a new location.", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.DRAMATIC, features.UNIMPORTANT_DEATH, features.TRAVEL]), \
  
  ("15 kill several zombies trying to break into stronghold", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.DANGER, features.HERO, features.UNIMPORTANT_KILL]), \
  
  ("ted sees the zombie queen in the lair. We break in a kill several zombies, but ted dies when the queen gets him." \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.HERO, features.UNIMPORTANT_KILL, features.IMPORTANT_DEATH, features.IMPORTANT_KILL, features.DRAMATIC]), \
  
  ("17 Ted bravely sacrifices himself to save the team", \
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], \
    [features.HERO, features.IMPORTANT_KILL, features.IMPORTANT_DEATH, features.DRAMATIC, features.TRAVEL]) \

  ("18 We kill the zombie overload and flowers shoot out of every zombie's eyeballs", \
    None, \
    [features.SAFETY])

  ("19 The zombie eat every last one of us. Ted is eaten by princess rainicorn.", \
    None, \
    [features.DEFEAT])
]

plot = skin.initPlot(nodes, templates, wordset)
