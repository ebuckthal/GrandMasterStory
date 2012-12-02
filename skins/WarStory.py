import skin
import plot.features as features

# random options to be used throughout the game
wordset = { "@KILLED" : ["blown up", "shot", "knifed"],
            "@WALKED" : ["strolled", "walked"],
            "@WHILE" : ["While cleaning his gun,", ""],
            "@PLACE" : ["Bunkers", "Tree"]
         }

# chooses a random option at the beginning of th game
constants = {
            "@LOCATION" : ["Afghanistan", "Korea", "France"],
            "@VILLAIN" : ["Nazis", "Communists", "Russians", "North Koreans", "Storm Troopers"],
            "@CITY" : ["Paris", "Stattenburger", "Hell"],
            "@HOME" : ["'Merican"]
          }

# maps keys to possible values for a story
choices = [ (["@CHAR1", "@CHAR2", "@CHAR3"], ["Private Ryan", "Sanchez", "Lieutenant Dan", "Forest", "Bubba"])
          ]

# lists of templates used by the plot nodes
templates = [
["""The @VILLAIN were pushing into @LOCATION as part of the biggest military operation in the history of the human race,\
 and everything was about to come to a head in the city of @CITY with a battle over a single bombed-out apartment building.""",
"""In the city of @CITY, @LOCATION the @HOME army was preparing for an incoming invasion of @VILLAIN.\
 The battle was to focus around a single bombed-out apartment building.""",
"""Years ago in @LOCATION, as part of a large scale military operation, the @VILLAIN were staging to take over the city of @CITY.\
 All fighting had came to a head at a single bombed-out apartment building."""],
["""@CHAR1 and his platoon was tasked with the thankless job of retaking the building after the @VILLAIN had seized it. \
To get a snapshot of what their mindset was like heading in, it's helpful to know that the assignment was considered an \
extremely dangerous one by the @HOME army, and that the @HOME army's slogan at the time was "die for the @HOME honor."
Somehow, the slogan failed to raise morale."""],
["""Doing the quick math, @CHAR1 realized his only chance was to throw his whole platoon into the meat grinder,\
 and hope that the speed with which they passed through left at least a few alive. He lost all but four men in the assault,\
  but eventually his plan worked and they took the building. Had they known they were dealing with a man who considered \
  four people surviving a success, the @VILLAIN probably would have realized that they were in for some serious shit.\
 Having barely enough survivors to outfit a respectable zombie movie, @CHAR1 could only station one soldier to each floor."""],
["""The building was subjected to relentless fire--as were the civilians huddled in its basement--\
but @CHAR1's unit held out long enough to be reinforced by a still-tiny 25 men. \
His men were given machine guns, rifles, mortars, barbed-wire, anti-tank mines, some body armor and\
 a PTRS-41 anti-tank rifle which @CHAR1 personally used to snipe a dozen tanks from the rooftop.\
  They basically used what little equipment they had to convert the apartment into a goddamn anti-@VILLAIN death machine\
   that could annihilate whatever came at it from a kilometer in every direction."""],
["""As long as everyone conserved their ammo and manned their posts, the only real danger posed to the building\
 came from flamethrowers. Fortunately, with legendary snipers like 19-year-old @CHAR2 on the top floor, this \
 usually resulted in a Viking funeral for the @VILLAIN."""],
["""Wave after wave of the @VILLAIN army hammered the building. And died."""],
["""Later, @CHAR1's men could boast that they killed more @VILLAIN defending their one\
 building than the French killed in the entire fall of Paris. And unfortunately for French egos,\
 they were still alive to boast--by February 2 the next year, the battle was over.\
 @CHAR1 was named a Hero, and the building he defended was made into a monument."""]
 ]

# list of plot nodes initialized with name, nextNode indexes, and features
# the index in this list must correspond to the index of the correct template above
nodes = [
    ('Setting', [1], None),
    ('Introduction', [2], None),
    ('Defend', [3], None),
    ('Reinforements', [4], None),
    ('Char 2', [5], None),
    ('Deaths', [6], None),
    ('Conclusion', None, None)
]

plot = skin.initPlot(nodes, templates, wordset, constants, choices)
