import skin
import chess.features as features

# random options to be used throughout the game
wordset = { "@ALIVECHAR" : ["@KILLCHAR"],
            "@ALLCHAR" : ["@CHAR1, @CHAR2, @CHAR3, and @CHAR4"],
            "@TOWN" : ["Paris", "London", "New York", "San Luis Obispo", "the small town of Haldenburg"],
            "@ZOMBIE" : ["Spitter Zombie", "Tank Zombie", "Charger Zombie", "Smoker Zombie"],
            "@KILLCHAR" : ["a zombie"],
            "@TRAVELED" : ["@KILLTRAVEL"],
            "@KILLTRAVEL" : ["walked", "ran"], # default travel - walking
            "@DROVE" : ["drove"] # if car hasnt blown up
         }

# chooses a random option at the beginning of th game
constants = {
            "@BUILDING" : ["bombed-out apartment building", "run-down hospital", "police station"],
            "@CAR" : ["beat up jeep", "black hummer", "ford focus"]
          }

# maps keys to possible values for a story
choices = [ (["@CHAR1", "@CHAR2", "@CHAR3", "@CHAR4"], ["Mike", "Eric", "Nick", "Connor", "Ted", "Fooad"])
          ]

resources = {"@KILLCHAR" : ["@CHAR1", "@CHAR2", "@CHAR3", "@CHAR4"],
             "@KILLTRAVEL" : ["@DROVE"]

}

#lists of templates used by the plot nodes
templates = [
#intro
["@ALLCHAR, were the only surviving humans in @TOWN. They decided they needed to venture \
out of the @BUILDING they were hiding in to find food and ammunition.",
"In @TOWN, the last of the survivors of the zombie apocalypse gathered. @ALLCHAR had been \
hiding in a @BUILDING for the past three days and needed to venture out for more food and ammunition."],
# move outside
["The group ran outside into their @CAR."],
#boring
["The wind kicked up; @ALIVECHAR shivered. There was a faint howl in the distance.", 
"A cloud moved across the sky, blocking the moon; it got unbearably dark.",
"Walking down the street, @ALIVECHAR stumbled over a trashcan making a loud clamor that echoed into the distance.", 
"The group heard a loud growling noise nearby."],
#danger
["Out of nowhere the group was cornered by a @ZOMBIE."],
#dramatic
["@ALIVECHAR stumbles across a hidden cache of weapons and ammunition."],
#hero
["There was a loud bang as a @ZOMBIE with a whole horde of zomibes crashed threw the wall be @ALIVECHAR and @ALIVECHAR pinning them to the wall. In an amazing show of bravery @ALIVECHAR shot the zomibies pinning them to the wall and saved everyone."],
#important kill
["@ALIVECHAR manages to bludgeons to death a @ZOMBIE with his bear hands."],
#UNIMPORTANT_KILL
["@ALIVECHAR is surprised by a @ZOMBIE and bearly manages to wound it with his crossbow before managing to get away."],
#IMPORTANT_DEATH", \
["A huge @ZOMBIE threw @KILLCHAR to the ground and tore off his head."],
#UNIMPORTANT_DEATH", \
["@ALIVECHAR gets severely wounded by a zombie.", 
"While they @KILLTRAVEL across the bridge a large mutant zombie smashed the front of their car, throwing them out."],
#TRAVEL
["The group @TRAVELED down the street toward the grocery store."],
#CHECK
["Off in the distance, the group sees a boat tied to the dock. They desiced to try and take it to safety."],
#important kill, Travel
["As the group ran through the street, @ALIVECHAR shot a @ZOMBIE in the face killing it."],
#CHECK, important kill
["They where less the 300 yards to the boat that was there safety when a @ZOMBIE jumped them. @ALIVECHAR shot his crossbow and hit the zombie in the eye."],
#Dramatic, important kill
["@ALIVECHAR shot a gas tank attached to a car which explosed killing many zomibes."],
#important kill, unimportant death
["@ALIVECHAR was badly wounded in the arm while killing a zombie"],
#SAFETY
["@ALLCHAR stumble exhausted on to the boat and sail off the coast leaving behind the hordes of zomibes trying to eat them."],
#Defeat
["Suddenly the group is cornered by the biggest horde of zombies that they have ever seen lead by a @ZOMBIE. @ALLCHAR are torn apart brutally and killed."],


# move inside
[""],
#boring
["The wind kicked up; @ALIVECHAR shivered. There was a faint howl in the distance.", 
"A cloud moved across the sky, blocking the moon; it got unbearably dark.",
"Walking down the street, @ALIVECHAR stumbled over a trashcan making a loud clamor that echoed into the distance.", 
"The group heard a loud growling noise nearby."],
#danger
["Out of nowhere the group was cornered by a @ZOMBIE."],
#dramatic
["@ALIVECHAR stumbles across a hidden cache of weapons and ammunition."],
#hero
["There was a loud bang as a @ZOMBIE with a whole horde of zomibes crashed threw the wall be @ALIVECHAR and @ALIVECHAR pinning them to the wall. In an amazing show of bravery @ALIVECHAR shot the zomibies pinning them to the wall and saved everyone."],
#important kill
["@ALIVECHAR manages to bludgeons to death a @ZOMBIE with his bear hands."],
#UNIMPORTANT_KILL
["@ALIVECHAR is surprised by a @ZOMBIE and bearly manages to wound it with his crossbow before managing to get away."],
#IMPORTANT_DEATH", \
["A huge @ZOMBIE threw @KILLCHAR to the ground and tore off his head."],
#UNIMPORTANT_DEATH", \
["@ALIVECHAR gets severely wounded by a zombie."],
#TRAVEL
["@ALLCHAR charge in to a @BUILDING that was accross the street."],
#CHECK
["Off in the distance, the group sees a boat tied to the dock. They desiced to try and take it to safety."],
#important kill, Travel
["As the group ran through the street, @ALIVECHAR shot a @ZOMBIE in the face killing it."],
#CHECK, important kill
["They where less the 300 yards to the boat that was there safety when a @ZOMBIE jumped them. @ALIVECHAR shot his crossbow and hit the zombie in the eye."],
#Dramatic, important kill
["@ALIVECHAR shot a gas tank attached to a car which explosed killing many zomibes."],
#important kill, unimportant death
["@ALIVECHAR was badly wounded in the arm while killing a zombie"],
#SAFETY
["@ALLCHAR stumble exhausted on to the boat and sail off the coast leaving behind the hordes of zomibes trying to eat them."],
#Defeat
["Suddenly the group is cornered by the biggest horde of zombies that they have ever seen lead by a @ZOMBIE. @ALLCHAR are torn apart brutally and killed."]
]

nodes = [
  ("0 Intro", \
    [1], \
    []),

  ("1 Move Outside", \
    [2], \
    []),

  # Outside
  ("2 Boring...", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    []), \
  
  ("3 danger.", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.DANGER]), \
  
  ("4 dramatic.", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.DRAMATIC]), \
  
  ("5 hero .", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.HERO, features.IMPORTANT_KILL, features.UNIMPORTANT_KILL]), \
  
  ("6 important kill .", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.IMPORTANT_KILL]), \
  
  ("7 UNIMPORTANT_KILL", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.UNIMPORTANT_KILL]), \
  
  ("8 IMPORTANT_DEATH", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.IMPORTANT_DEATH]), \
  
  ("9 UNIMPORTANT_DEATH", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.UNIMPORTANT_DEATH]), \
  
  ("10 TRAVEL", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.TRAVEL]), 
  
  ("11 check", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.CHECK]),

  ("12 Important Kill, Travel", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.IMPORTANT_KILL, features.TRAVEL]),

  ("13 Check Important Kill", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.CHECK, features.IMPORTANT_KILL]), 

  ("14 Dramatic, Important kill", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.DRAMATIC, features.IMPORTANT_KILL]), 

  ("15 Important Kill Unimportant death", \
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], \
    [features.IMPORTANT_KILL, features.UNIMPORTANT_DEATH]),

  ("16 SAFETY", \
    None, \
    [features.SAFETY]), 
  
  ("17 defeat", \
    None, \
    [features.DEFEAT]),

  # Inside (get to the roof)
  ("18 Get inside...", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.TRAVEL, features.DRAMATIC]), \

  ("19 Boring...", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    []), \
  
  ("20 danger.", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.DANGER]), \
  
  ("21 dramatic.", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.DRAMATIC]), \
  
  ("22 hero .", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.HERO, features.IMPORTANT_KILL, features.UNIMPORTANT_KILL]), \
  
  ("23 important kill .", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.IMPORTANT_KILL]), \
  
  ("24 UNIMPORTANT_KILL", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.UNIMPORTANT_KILL]), \
  
  ("25 IMPORTANT_DEATH", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.IMPORTANT_DEATH]), \
  
  ("26 UNIMPORTANT_DEATH", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.UNIMPORTANT_DEATH]), \
  
  ("27 TRAVEL", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.TRAVEL]), 
  
  ("28 check", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.CHECK]),

  ("29 Important Kill, Travel", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.IMPORTANT_KILL, features.TRAVEL]),

  ("30 Check Important Kill", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.CHECK, features.IMPORTANT_KILL]), 

  ("31 Dramatic, Important kill", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.DRAMATIC, features.IMPORTANT_KILL]), 

  ("32 Important Kill Unimportant death", \
    [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34], \
    [features.IMPORTANT_KILL, features.UNIMPORTANT_DEATH]),

  ("33 SAFETY", \
    None, \
    [features.SAFETY]), 
  
  ("34 defeat", \
    None, \
    [features.DEFEAT]),
]

plot = skin.initPlot(nodes, templates, wordset, constants, choices, resources)
