import skin
import chess.features as features

# random options to be used throughout the game
wordset = { "@UNIT" : ["@CHAR1 and his platoon", "@CHAR1's unit", "@CHAR1's men", "@CHAR1 and his men"],
            "@SLOGAN" : ["\"die for the @HOME honor.\"", "\"don't come back without honor.\"", "\"Fight for the homeland!\""],
            "@REINFORCEMENTS" : ["a still-tiny 25 men", "a school bus of children", "twenty French maids"],

            "@DIDSTUFF" : ["@WALKED down the road"],
            "@KILLED" : ["blown up", "shot", "knifed"],
            "@WALKED" : ["strolled", "walked"],
            "@WHILE" : ["While cleaning his gun,", ""],
            "@PLACE" : ["Bunkers", "Tree"],
            features.DEATHOF : ["enemy soldier"],
            features.KNIGHT : ["flamethrower"],
            features.PAWN : ["kitten"],
            features.BISHOP : ["jeep"]
         }

# chooses a random option at the beginning of th game
constants = {
            "@MENLEFT" : ["four", "five"],
            "@BUILDING" : ["single bombed-out apartment building", "run-down hospital"],
            "@LOCATION" : ["Afghanistan", "Korea", "France"],
            "@VILLAINS" : ["Nazis", "Communists", "Russians", "North Koreans", "Storm Troopers"],
            "@CITY" : ["Paris", "Stattenburger", "Hell"],
            "@HOME" : ["American", "Swiss", "French"],
          }

# maps keys to possible values for a story
choices = [ (["@CHAR1", "@CHAR2", "@CHAR3"], ["Private Ryan", "Sanchez", "Lieutenant Dan", "Forest", "Bubba"])
          ]

# lists of templates used by the plot nodes
templates = [
["""The @VILLAINS were pushing into @LOCATION as part of the biggest military operation in the history of the human race,\
 and everything was about to come to a head in the city of @CITY with a battle over a @BUILDING.""",
"""In the city of @CITY, @LOCATION the @HOME army was preparing for an incoming invasion of @VILLAINS.\
 The battle was to focus around a @BUILDING.""",
"""Years ago in @LOCATION, as part of a large scale military operation, the @VILLAINS were staging to take over the city of @CITY.\
 All fighting had came to a head at a @BUILDING."""],
["""@UNIT were tasked with the thankless job of retaking the building after the @VILLAINS had seized it.""",
"""@UNIT were the only troops in the area, so were assigned the task of retaking the building from the control of the @VILLAINS."""],
["""To get a snapshot of what their mindset was like heading in, it's helpful to know that the assignment was considered an \
extremely dangerous one by the @HOME army, and that the @HOME army's slogan at the time was @SLOGAN
Somehow, the slogan failed to raise morale."""],
["""Doing the quick math, @CHAR1 realized his only chance was to throw his whole platoon into the meat grinder,\
 and hope that the speed with which they passed through left at least a few alive. He lost all but @MENLEFT men in the assault,\
  but eventually his plan worked and they took the building. Had they known they were dealing with a man who considered \
  @MENLEFT people surviving a success, the @VILLAINS probably would have realized that they were in for some serious shit.\
 Having barely enough survivors to outfit a respectable zombie movie, @CHAR1 could only station one soldier to each floor."""],
["""The building was subjected to relentless fire--as were the civilians huddled in its basement--\
but @UNIT held out long enough to be reinforced by @REINFORCEMENTS. \
His men were given machine guns, rifles, mortars, barbed-wire, anti-tank mines, some body armor and\
 a PTRS-41 anti-tank rifle which @CHAR1 personally used to snipe a dozen tanks from the rooftop.\
  They basically used what little equipment they had to convert the building into a goddamn anti-@VILLAINS death machine\
   that could annihilate whatever came at it from a kilometer in every direction."""],
["""As long as everyone conserved their ammo and manned their posts, the only real danger posed to the building\
 came from flamethrowers. Fortunately, with legendary snipers like 19-year-old @CHAR2 on the top floor, this \
 usually resulted in a Viking funeral for the @VILLAINS."""],
["""Wave after wave of the @VILLAINS army hammered the building. And died."""],
["""Later, @UNIT could boast that they killed more @VILLAINS defending their one\
 building than the French killed in the entire fall of Paris. And unfortunately for French egos,\
 they were still alive to boast--by February 2 the next year, the battle was over.\
 @CHAR1 was named a Hero, and the building he defended was made into a monument."""]
 ]

# list of plot nodes initialized with name, nextNode indexes, and features
# the index in this list must correspond to the index of the correct template above
nodes = [
    ('Setting', [1], None),
    ('Introduction', [2], None),
    ('Slogan', [3], None),
    ('Defend', [4], None),
    ('Reinforcements', [5], None),
    ('Char 2', [6], None),
    ('Deaths', [7], None),
    ('Conclusion', None, None)
]

plot = skin.initPlot(nodes, templates, wordset, constants, choices)
