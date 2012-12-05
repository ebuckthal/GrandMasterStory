import skin
import chess.features as features

# random options to be used throughout the game
wordset = { "@ALIVECHAR" : ["@KILLCHAR"],
            "@ALLCHAR" : ["@CHAR1, @CHAR2, @CHAR3, and @CHAR4"],
            "@TOWN" : ["Paris", "London", "New York", "San Luis Obispo", "the small town of Ravenholdt", "San Francisco"],
            "@ZOMBIE" : ["Spitter Zombie", "Tank Zombie", "Charger Zombie", "Smoker Zombie", "Hunter Zombie", "Boomer Zombie", "Smoker Zombie", "Jockey Zombie"],
            "@KILLCHAR" : ["a zombie", "a disgusting, pussy rotting zombie", "what was once human", "a head-less zombie"],
            "@TRAVELED" : ["@KILLTRAVEL"],
            "@KILLTRAVEL" : ["walked", "ran", "jumped"], # default travel - walking
            "@DROVE" : ["drove", "sped"] # if car hasn't blown up
         }

# chooses a random option at the beginning of th game
constants = {
            "@BUILDING" : ["bombed-out apartment building", "run-down hospital", "police station", "crashed airplane"],
            "@CAR" : ["beat up jeep", "black hummer", "ford focus", "run-down ambulance", "police cruiser"]
          }

# maps keys to possible values for a story
choices = [ (["@CHAR1", "@CHAR2", "@CHAR3", "@CHAR4"], ["Mike", "Eric", "Nick", "Connor", "Ted", "Foaad"])
          ]

resources = {"@KILLCHAR" : ["@CHAR1", "@CHAR2", "@CHAR3", "@CHAR4"],
             "@KILLTRAVEL" : ["@DROVE"]

}

#lists of templates used by the plot nodes
templates = [
#intro
["@ALLCHAR, had banded together survivors of the human race in @TOWN. The zombie apocalypse started 2 months ago, but they knew more humans were still alive. \
They collectively decided they needed to leave the @BUILDING because supplies and ammunition were running low.",
"In @TOWN, one rough group of odd characters were banded together. The zombie apocalypse started only months ago, but @ALLCHAR had been \
hiding in a @BUILDING for the past three days and needed to venture out for more food and ammunition. Some still thought more people were out there."],
# move outside
["The group ran outside into their @CAR", 
"Zombies broke past their barricades. They all had to move quickly outside and luckily into their @CAR"],
#boring
["The wind kicked up; @ALIVECHAR shivered. There was a faint howl in the distance.", 
"@ALIVECHAR mentioned the gathering of zombies in the distance.",
"Everyone was quiet. The zombies hearing was very sensitive.",
"The gang saw an old barricaded @BUILDING. Obvious signs of human struggle were everywhere.",
"The streets were filled with zombies crawling on top of a @CAR"
"A cloud moved across the sky, blocking the moon; it got unbearably dark.",
"Walking down the street, @ALIVECHAR stumbled over a trashcan making a loud clamor that echoed into the distance.", 
"The group heard a loud growling noise nearby."],
#danger
["Out of nowhere the group was cornered by a @ZOMBIE.",
 "In the window above, a @ZOMBIE spotted them.",
 "The gang turned a corner and found themselves in a staring contest with a @ZOMBIE.",
 "Some zombies had the strength of a dozen average zombies and right now, @ALIVECHAR was staring one down.",
 "The gang was sprinting between shadowed corners, but @ALIVECHAR tripped briefly and alerted the nearby @ZOMBIE."],
#dramatic
["@ALIVECHAR stumbles across a hidden cache of weapons and ammunition."
 "There had been a group of people here before. Guns and ammunition were in stacks but there were no people to be found. Something about it wasn't right, but the gang took what they could.",
 "In a moment of hope, @ALIVECHAR found a stash of batteries, bottled water, and a broken radio. Maybe fixing the radio could reveal another human group?",
 "The group was together and out of zombie danger. They barricaded a steel door behind them and took a moment to recuperate.",
 "@ALIVECHAR reloaded his gun. Danger was near, but the last few zombies didn't stand a chance against his shot gun.",
 "More guns! @ALIVECHAR threw down his baseball bat and picked up something with a little more power."],
#hero
["There was a loud bang as a @ZOMBIE with a whole horde of zombies crashed threw the wall be @ALIVECHAR and @ALIVECHAR pinning them to the wall. \
In an amazing show of bravery @ALIVECHAR shot the zombies pinning them to the wall and saved everyone.",
"@ALIVECHAR shot a zombie standing next to an burnt police cruiser. Unluckily the car alarm still worked. Every zombie in the area started rushing towards @ALIVECHAR. \
A @ZOMBIE took the front of the crowd, crushing several of his zombie allies. @ALIVECHAR set up a propane tank trap and ran as fast as possible. Impossibly, he shot over \
his shoulder and set off the bomb just in time. The group was safe.",
"@ZOMBIE jumped out from a window above @ALIVECHAR, crushing his leg and throwing dust into the air. @ALIVECHAR pushed the zombie off with the but of his gun and delivered a fatal blast.",
"@ALLCHAR fixed up a barricade in an attempt to escape the rushing horde, but it wasn't going to hold. There were too many zombies. @ALIVECHAR set up a distraction. \
Blasting away all the zombies from a nearby window.",
"In a tight street, @ZOMBIE and @ZOMBIE approached the group from either side. @ALIVECHAR killed both with amazing marksmanship.",
"@ALIVECHAR set up a gasoline filled trap while the others stood back in case the zombies surprised him. @ALIVECHAR caught the attention of a horde of zombies and led them straight into \
the trap which turned into an inferno with a quick shot from @ALIVECHAR 's gun. The zombies burned slowly; the smell was awful."],
#important kill
["@ALIVECHAR managed to bludgeon a @ZOMBIE to death with his bare hands.",
 "@ALIVECHAR destroyed a @ZOMBIE by rolling a refrigerator out of a third-story window with pinpoint accuracy.",
 "By complete surprise, @ALIVECHAR found a zombie gathering and remove it with a skillful toss of a grenade.",
 "A @ZOMBIE approaches @ALLCHAR, but @ALIVECHAR deals a devastating blow to protect the group."],
#UNIMPORTANT_KILL
["@ALIVECHAR is surprised by a @ZOMBIE and barely manages to wound it with his crossbow before managing to get away.",
"A single zombie runs blindly at @ALIVECHAR, who bashes the demon down cleanly with the strike of a club.",
"A smattering of zombies missing essential limbs helplessly lie in a pile near @ALIVECHAR. He methodically puts them out of pain.",
"@ALLCHAR plow though a collection of zombies, easily dismantling each one."],
#IMPORTANT_DEATH", \
["A huge @ZOMBIE threw @KILLCHAR to the ground and tore off his head. Blood everywhere.",
"From an unnoticed portal, a @ZOMBIE crawls through and bites @KILLCHAR. @ALIVECHAR blasts the zombie away, but it is too late for his bitten comrade. @ALLCHAR watch him slowly turn, \
but @ALIVECHAR decides to put him out of misery.",
"A horde of zombies rush all around @ALLCHAR. @ALIVECHAR slices several zombies with his drawn sword, but one bites @KILLCHAR. Soon, the zombie horde was ripping his flesh apart.",
"@ALIVECHAR is grabbed through a window by a @ZOMBIE. @ALLCHAR attempt to remove it, but more hands keep coming and eventually their comrade is gone."],
#UNIMPORTANT_DEATH", \
["@ALIVECHAR is severely wounded by a rampaging zombie, but he'll make it.", 
"While they @KILLTRAVEL across the bridge a large mutant zombie smashed the front of their car, throwing them out."],
#TRAVEL
["The group @TRAVELED down the street toward the grocery store.",
"@ALLCHAR agree they haven't yet found safety. Moving seems like the best option.",
"@ALLCHAR want to find a new hideout before dark, so they quickly move across town in search of shelter."],
#CHECK
["Off in the distance, the group sees a boat tied to the dock. Could the ocean give them refuge?",
"A helicopter circles overhead. @ALLCHAR wave furiously, but incoming zombies force them indoors. Who was in that helicopter?",
"The survivors hear gunshots nearby. And shouting! Could there be more people nearby?"],
#important kill, Travel
["As the group ran through the street, @ALIVECHAR shot a @ZOMBIE in the face killing it.",
"@ALLCHAR knew they needed to cross town. While maneuvering the streets, a @ZOMBIE grabs @ALIVECHAR but @ALIVECHAR quickly destroys the zombie.",
"With a newly-equipped rifle, @ALIVECHAR blasts a @ZOMBIE from the center of it's zombie horde.",
"@ALIVECHAR steadies his rifle and shoots a @ZOMBIE cleanly from yards away.",
"Zombies chase @ALLCHAR up a narrow street. At the end stands a @ZOMBIE formidably. @ALIVECHAR jumps off the top of a car, guns blazing and destroys the threat.",
"@ALIVECHAR @DROVE their cars over a @ZOMBIE completely destroying the large zombie, but their car isn't looking too good."],
#CHECK, important kill
["They where less the 300 yards to the boat that was there safety when a @ZOMBIE jumped them. @ALIVECHAR shot his crossbow and hit the zombie in the eye.",
"With the escape boat in sight, a @ZOMBIE jumps out and surprises @ALLCHAR. @ALIVECHAR quickly cuts the zombie's head off."],
#Dramatic, important kill
["@ALIVECHAR shoots a gas tank attached to a car which explodes killing a @ZOMBIE and igniting the combustible zombies nearby.",
"@ALIVECHAR pushes the remaining survivors out of the car, then drives it head on into a @ZOMBIE and jumps out at the last second. In the dust, @ALLCHAR see that the car trick worked perfectly.",
"A @ZOMBIE rushes towards the survivors, followed by zombie stragglers. @ALIVECHAR dodges several swipes by another @ZOMBIE, then @ALIVECHAR shoots both zombie threats."],
#important kill, unimportant death
["@ALIVECHAR was badly wounded in the arm while killing a @ZOMBIE."
"It takes almost all of the ammunition @ALIVECHAR has, but he finally brings down a @ZOMBIE."],
#SAFETY
["@ALLCHAR blast the last few remaining zombies from the dock attached to the boat. They jump in and untie the boat. The characters feel safe for once as the boat slowly drifts into the ocean."],
#Defeat
["Suddenly the group is surrounded by the biggest horde of zombies that they have ever seen led by a @ZOMBIE. @ALLCHAR are torn apart brutally and killed."],


# move inside
[""],
#boring
["The wind kicked up; @ALIVECHAR shivered. There was a faint howl in the distance.", 
"@ALIVECHAR mentioned the gathering of zombies in the distance.",
"Everyone was quiet. The zombies hearing was very sensitive.",
"The gang saw an old barricaded @BUILDING. Obvious signs of human struggle were everywhere.",
"The streets were filled with zombies crawling on top of a @CAR"
"A cloud moved across the sky, blocking the moon; it got unbearably dark.",
"Walking down the street, @ALIVECHAR stumbled over a trashcan making a loud clamor that echoed into the distance.", 
"The group heard a loud growling noise nearby."],
#danger
["Out of nowhere the group was cornered by a @ZOMBIE.",
"Several zombies crawl in through the windows and look for the survivors.",
"The survivors hold their breath and stare at the @ZOMBIE looking through the open door for them.",
"A @ZOMBIE spots @ALIVECHAR and calls to the rest of his zombie horde."],
#dramatic
["@ALIVECHAR stumbles across a hidden cache of weapons and ammunition."],
#hero
["There was a loud bang as a @ZOMBIE with a whole horde of zombies crashed threw the wall be @ALIVECHAR and @ALIVECHAR pinning them to the wall. In an amazing show of bravery @ALIVECHAR shot the zomibies pinning them to the wall and saved everyone."],
#important kill
["@ALIVECHAR manages to bludgeons to death a @ZOMBIE with his bear hands."],
#UNIMPORTANT_KILL
["@ALIVECHAR is surprised by a @ZOMBIE and barely manages to wound it with his crossbow before managing to get away."],
#IMPORTANT_DEATH", \
["A huge @ZOMBIE threw @KILLCHAR to the ground and tore off his head."],
#UNIMPORTANT_DEATH", \
["@ALIVECHAR gets severely wounded by a zombie."],
#TRAVEL
["@ALLCHAR charge in to a @BUILDING that was across the street."],
#CHECK
["Off in the distance, the group sees a boat tied to the dock. They decided to try and take it to safety."],
#important kill, Travel
["As the group ran through the street, @ALIVECHAR shot a @ZOMBIE in the face killing it."],
#CHECK, important kill
["They where less the 300 yards to the boat that was there safety when a @ZOMBIE jumped them. @ALIVECHAR shot his crossbow and hit the zombie in the eye."],
#Dramatic, important kill
["@ALIVECHAR shot a gas tank attached to a car which exploded killing many zombies."],
#important kill, unimportant death
["@ALIVECHAR was badly wounded in the arm while killing a zombie"],
#SAFETY
["@ALLCHAR stumble exhausted on to the boat and sail off the coast leaving behind the hordes of zombies trying to eat them."],
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
