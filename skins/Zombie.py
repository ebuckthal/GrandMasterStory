import skin
import chess.features as features

# random options to be used throughout the game
wordset = { "@ALIVECHAR" : ["@KILLCHAR"],
            "@ALLCHAR" : ["@CHAR1, @CHAR2, @CHAR3, and @CHAR4"],
            "@TOWN" : ["Paris", "London", "New York", "San Luis Obispo"],
            "@ZOMBIE" : ["Spitter Zombie", "Tank Zombie", "Charger Zombie", "Smoker Zombie"],
            "@KILLCHAR" : ["a person"]
         }

# chooses a random option at the beginning of th game
constants = {
            "@BUILDING" : ["single bombed-out apartment building", "run-down hospital", "police station"],
          }

# maps keys to possible values for a story
choices = [ (["@CHAR1", "@CHAR2", "@CHAR3", "@CHAR4"], ["Mike", "Eric", "Nick", "Connor", "Ted", "Fooad"])
          ]

resources = {"@KILLCHAR" : ["@CHAR1", "@CHAR2", "@CHAR3", "@CHAR4"]

}

#lists of templates used by the plot nodes
templates = [
["@ALLCHAR, were the only surviving humans in @TOWN. They decided they needed to venture \
out of the @BUILDING they were hiding in to find food and ammunition."],
#boarding
["The wind kicked up and @ALIVECHAR shivered."],
#danager
["Out of nowhere the group was cornered by a @ZOMBIE."],
#dramatic
["@ALIVECHAR stumbles across a hidden cache of weapons and ammunition."],
#hero
["There was a loud bang as a @ZOMBIE with a whole horde of zomibes crashed threw the wall be @ALIVECHAR and @ALIVECHAR pinning them to the wall. In an amazing show of bravery @ALIVECHAR shot the zomibies pinning them to the wall and saved everyone."],
#important kill
["@ALIVECHAR manages to bludgeons to death a @ZOMBIE with his bear hands."],
#UNIMPORTANT_KILL
["@ALIVECHAR is supprised by a @ZOMBIE and bearly manages to wound it with his crossbow before managing to get away."],
#IMPORTANT_DEATH", \
["A hudge @ZOMBIE threw @KILLCHAR to the ground and tore off his head."],
#UNIMPORTANT_DEATH", \
["@ALIVECHAR gets severely wounded by a zombie."],
#TRAVEL
["@ALLCHAR charge in to a @BUILDING that was accross the street."],
#CHECK
["Off in the distance, the group sees a boat tied to the dock. They desiced to try and take it to safety."],
#SAFETY
["@ALLCHAR stumble exaushed on to the boat and sail off the coast leaving behind the hordes of zomibes trying to eat them."],
#Defeat
["Suddenly the group is cornered by the biggest horde of zombies that they have ever seen lead by a @ZOMBIE. @ALLCHAR are torn apart brutally and killed."],
#boarding
["A cloud moved to block the moon. It got unbarably dark."],
#boarding
["The group heard a growl and froze."],
#important kill, Travel
["As the group ran through the street, @ALIVECHAR shot a @ZOMBIE in the face killing it."],
#CHECK, important kill
["They where less the 300 yards to the boat that was there safety when a @ZOMBIE jumped them. @ALIVECHAR shot his crossbow and hit the zombie in the eye."],
#Dramatic, important kill
["@ALIVECHAR shot a gas tank attached to a car which explosed killing many zomibes."],
#important kill, unimportant death
["@ALIVECHAR was badly wounded in the arm while killing a zombie"]
]

nodes = [
  ("0 Intro", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    []), \
  
  ("1 Boring...", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    []), \
  
  ("2 danger.", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.DANGER]), \
  
  ("3 dramatic.", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.DRAMATIC]), \
  
  ("4 hero .", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.HERO, features.IMPORTANT_KILL, features.UNIMPORTANT_KILL]), \
  
  ("5 important kill .", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.IMPORTANT_KILL]), \
  
  ("6 UNIMPORTANT_KILL", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.UNIMPORTANT_KILL]), \
  
  ("7 IMPORTANT_DEATH", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.IMPORTANT_DEATH]), \
  
  ("8 UNIMPORTANT_DEATH", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.UNIMPORTANT_DEATH]), \
  
  ("9 TRAVEL", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.TRAVEL]), 
  
  ("10 check", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.CHECK]),
  
  ("11 SAFETY", \
    None, \
    [features.SAFETY]), 
  
  ("12 defeat", \
    None, \
    [features.DEFEAT]),
  ("13 Boring...2", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    []), \
  ("14 Boring...3", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    []), \
  ("15 Important Kill, Travel", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.IMPORTANT_KILL, features.TRAVEL]), \
  ("16 Check Important Kill", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.CHECK, features.IMPORTANT_KILL]), \
  ("17 Dramatic, Important kill", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.DRAMATIC, features.IMPORTANT_KILL]), \
  ("18 Important Kill Unimportant death", \
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.IMPORTANT_KILL, features.UNIMPORTANT_DEATH]), \
]

plot = skin.initPlot(nodes, templates, wordset, constants, choices, resources)
