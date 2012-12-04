import skin
import chess.features as features

# random options to be used throughout the game
wordset = { "@ALIVECHAR" : ["@KILLCHAR"],
            "@ALLCHAR" : ["@CHAR1, @CHAR2, @CHAR3, and @CHAR4"],
            "@TOWN" : ["town"],
            "@ZOMBIE" : ["zombie"],
            "@KILLCHAR" : ["a person"]
         }

# chooses a random option at the beginning of th game
constants = {
            "@BUILDING" : ["single bombed-out apartment building", "run-down hospital"],
          }

# maps keys to possible values for a story
choices = [ (["@CHAR1", "@CHAR2", "@CHAR3", "@CHAR4"], ["Mike", "Eric", "Nick", "Connor", "Bob", "Sally"])
          ]

resources = {"@KILLCHAR" : ["@CHAR1", "@CHAR2", "@CHAR3", "@CHAR4"]

}

#lists of templates used by the plot nodes
templates = [
["@ALLCHAR, were the only surviving humans in @TOWN. They decided they needed to venture \
out of the @BUILDING they were hiding in to find food and ammunition."],
["The wind kicked up and @ALIVECHAR shivered."],
["Out of nowhere the group was cornered by a @ZOMBIE."],
#dramatic
["@ALIVECHAR stumbles across a hidden cache of weapons."],
#hero
["@ALIVECHAR manages to kill a @ZOMBIE and a @ZOMBIE while saving @ALIVECHAR from a gruesome death."],
#important kill
["@ALIVECHAR bludgeons to death a @ZOMBIE."],
#UNIMPORTANT_KILL
["@ALIVECHAR wounds a @ZOMBIE with his crossbow."],
#IMPORTANT_DEATH", \
["@KILLCHAR gets torn to shreds by a zombie."],
#UNIMPORTANT_DEATH", \
["@ALIVECHAR gets severely wounded by a zombie."],
#TRAVEL
["The goup travels to the neareset building."],
#CHECK
["They are mere feet from the helicopter pad."],
#SAFETY
["The group enters the helicopter and flies away to safety."],
#Defeat
["They are surrounded by zombies and one by one torn to shreds."]
]

nodes = [
  ("0 Intro", \
    [1,2,3,4,5,6,7,8,9,10,11,12], \
    []), \
  
  ("1 Boring...", \
    [1,2,3,4,5,6,7,8,9,10,11,12], \
    []), \
  
  ("2 danger.", \
    [1,2,3,4,5,6,7,8,9,10,11,12], \
    [features.DANGER]), \
  
  ("3 dramatic.", \
    [1,2,3,4,5,6,7,8,9,10,11,12], \
    [features.DRAMATIC]), \
  
  ("4 hero .", \
    [1,2,3,4,5,6,7,8,9,10,11,12], \
    [features.HERO, features.IMPORTANT_KILL, features.UNIMPORTANT_KILL]), \
  
  ("5 important kill .", \
    [1,2,3,4,5,6,7,8,9,10,11,12], \
    [features.IMPORTANT_KILL]), \
  
  ("6 UNIMPORTANT_KILL", \
    [1,2,3,4,5,6,7,8,9,10,11,12], \
    [features.UNIMPORTANT_KILL]), \
  
  ("7 IMPORTANT_DEATH", \
    [1,2,3,4,5,6,7,8,9,10,11,12], \
    [features.IMPORTANT_DEATH]), \
  
  ("8 UNIMPORTANT_DEATH", \
    [1,2,3,4,5,6,7,8,9,10,11,12], \
    [features.UNIMPORTANT_DEATH]), \
  
  ("9 TRAVEL", \
    [1,2,3,4,5,6,7,8,9,10,11,12], \
    [features.TRAVEL]), 
  
  ("10 check", \
    [1,2,3,4,5,6,7,8,9,10,11,12], \
    [features.CHECK]),
  
  ("11 SAFETY", \
    None, \
    [features.SAFETY]), 
  
  ("12 defeat", \
    None, \
    [features.DEFEAT])
]

plot = skin.initPlot(nodes, templates, wordset, constants, choices, resources)
