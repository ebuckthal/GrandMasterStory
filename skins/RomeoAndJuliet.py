import skin
import plot.features as features

#lists of words used by the templates
wordset = {"@KILLED" : ["slayed", "killed"],
           "@BEAUTIFUL" : ["lovely", "beautiful", "gorgeous", "pretty"],
           "@WALKED" : ["strolled", "walked"]}

#lists of templates used by the plot nodes
templates = [
["""Intro."""],

["""As Benvolio strolled down a street in Verona, he was waylaid by a rogue group of Capulet \
thugs. "Thou art trespassing on Capulet grounds!", shrieked the thugs as they stabbed his \
limp body and celebrated their victory."""],

["""Benvolio was one of the most prominent Montague members. A strong-willed, beautiful, and \
courageous young man. His duty was to patrol the streets near the Montague stronghold, but \
he had a bad habit to find trouble and ventured down a side street leading up to the Capulet \
fortress. He realized there was no escape when he heard footsteps behind him. He was cornered. \
He valiantly drew his dagger and slashed down two Capulet thugs before taking a dagger to the \
stomach from Tybalt. "My only regret is my one life to give for the Montague name," he spat \
with his last breath."""],

["""The love-stricken Romeo pleaded with his father to court the lovely Juliet. However, \
Montague, still grieving after the loss of Benvolio, forbade Romeo from venturing \
anywhere near Capulet territory."""],

["""Meanwhile, Romeo distanced himself from the ongoing conflict. He hated the bloodshed \
between the two families and he had completely lost himself after catching the eye of \
the fair Capulet daughter, Juliet. His father forbade the love between the two, but to \
Romeo that made the idea of Juliet titillating and rebellious. His father ordered Romeo \
to remain in the Montague household especially to protect Romeo who would face certain \
death if a Capulet discovered his love."""],

["""Romeo was not one to follow rules and the Montague house was easy to sneak out of. \
In the dead of night he was able to see Juliet from the courtyard below her balcony."""],

["""Ignoring his father's warnings, Romeo snuck out that night on a mission to catch a \
potential glimpse of the fair Juliet. To his surprise he sees Juliet standing out on her \
balcony as he scurries in the brush below. "Wherefore are thou Romeo!" sang Juliet. "I \
am here, fair lady!" replied Romeo. Their eyes locked in a deep love-filled gaze, but a \
rustling in the shadows frightened Romeo to retreat."""],

["""Capulet's wife heard Juliet's brief dialog with Romeo and knew he daughter must \
be punished fro such insolence. She tells her husband, the Capulet patriarch, of the \
meeting."""],

["""Capulet is furious when his wife details the meeting between Romeo and Juliet in \
spite of the feud between their families. Juliet's love was in his mind a weakness of \
his family's and it must be stopped. The very idea of his daughter's infatuation with \
a disgusting Montague imp sent shivers down his spine, but he wanted to use this to his \
advantage."""],

["""Capulet has an idea. He writes a letter to Romeo disguised as Juliet to meet him in \
the city plaza the next day."""],

["""Capulet formulates a cunning plan to lure Montague into a trap using Romeo's blind \
love for Juliet as bait. He has a scribe create a letter in Juliet's name to Romeo \
with a a plan to meet as anonymous city-goers the city plaza just as the sun sets \
the next day."""],

["""Romeo reads the letter and ventures out into the city wearing clothes from his \
house's servants as a disguise. Capulet traps him with several thugs in the plaza. \
However, Romeo's father has been alerted of his absence and several Montague soldiers \
are ready to fight just as Romeo finds himself trapped."""],

["""Romeo is ecstatic when he reads the letter. As Romeo carefully sneaks out under his \
curfew to catch a glimpse of his lover, his heart is pounding with excitement. \
His clothing is from the servant's quarters and disguises himself, but Capulet \
follows him up the street to a trap. Luckily for Romeo, his father is alerted of \
his absence. "This letter says he will be in the city plaza at dusk, and it's dusk \
now! Get out there and get my men!" Montague says as he rushes out to find his son. \
He sees Capulet and his men around Romeo but jumps in with swords to defend his \
family. The two patriarchs quarrel briefly with daggers drawn."""],

["""A bright flash stuns Montague just as reinforcements from the family arrive, but \
Capulet lunges and slices Montague's hand, rendering him unable to fight and allowing \
Capulet and his men to escape."""],

[""""This isn't the time to fight, Capulet!" Montague shouts. We shouldn't be fighting \
here or now and not over my son like this. "You know he's in love with my daughter \
and I won't allow it," Capulet replies. Montague is embarrassed, but Capulet has \
already ordered his men to step back, they don't want to risk a street fight in \
such a popular location."""],

["""Romeo is saved. Montague is furious."""],

["""Romeo is saved, but Montague is filled with rage. "The last straw has been \
drawn!" he furiously shouted towards the retreated Capulet. """],

["""In order to permanently separate Juliet and Romeo, Capulet arranges a marriage \
between his daughter Juliet and the Count Paris."""],

["""Capulet and Juliet bicker over her obsession with Romeo! "But father this \
transcends the silly quarrel between you and Montague. Romeo and I are destined \
for each other!" Capulet orders Juliet to remain in the fortress and arranges for \
her marriage to the Count Paris. Juliet is furious, "You can't do this! My live is \
but my own!" """],

["""Once Romeo hears of the proposed marriage of Juliet, his heart swells and he \
irrationally decides that he and Juliet must depart from the city. The only \
way their love can be realized is without the frivolous arguments between their \
opposing families."""],

["""Romeo struggles with internal conflict. His heart is so infatuated with Juliet \
that he would do anything to be with her. On the other hand he wants to serve \
his family and live as a proud Montague patriarch potentially ruling the family \
eventually. He eventually resolves that leaving this life is the only thing he \
wants. He plans to depart with the fair Juliet."""],

["""Quickly, Romeo grabs a dagger and a bag with a few days supplies and rushes to \
find Juliet under the guise of night."""],

["""Romeo gathers up his last belongings including a heralded dagger from the family's \
common room. He makes plans to wait at the balcony until he is able to find Juliet \
again and take her with him. "Together at last, Juliet! Wait not but for me!" """],

["""Romeo spots his cousin, Mercutio out in the city. From a distance, he sees the \
Capulet solider Tybalt stand up to Mercutio. Tybalt, eager to prove his worth for \
the Capulet family, stabs Mercutio and slowly watches him die."""],

["""In the night, Romeo's cousin Mercutio is out with no regard for the family curfew. \
He runs into the Capulet thug Tybalt and the two exchange nasty words. "You be \
at the end of my dagger for what happened to Benvolio!" Mercutio tells Tybalt. \
Tybalt is offended and the two lunge at each other. A couple of clashes of dagger \
foreshadow Tybalt's fatal stabbing of Mercutio. "I have perished!" Mercutio \
pants as he slowly falls to the ground."""],

["""Without hesitation, Romeo dashes into the street with his dagger out. He jumps \
what seems like 20 feet and strikes down Tybalt. Tybalt is able to get up \
and threatens Romeo."""],

["""Romeo's heart sank and his fists tightened. He knew that Tybalt could not get \
away with this. He snatched the dagger from his waist and charged into the street \
at Tybalt. "You've killed another Montague! This world is but a place of blood and \
rivalry!" Romeo pleads, but disregarding the possible retaliation from Capulet's \
family, he shoves his dagger towards Tybalt and Tybalt deflects it. "You can't win, \
this poor fool had it coming. We both know that Verona is Capulet's city." """],

["""With a quick move, Romeo finishes Tybalt's life."""],

["""Romeo throws his dagger in a unpredicted move and Tybalt is unable to escape is \
hungry point. The knife has punctured his chest and Tybalt falls. "I am but one \
Capulet, you will not be able to defeat us all!" Romeo leaves the dagger in Tybalt \
and street with two bodies."""],

["""Tybalt retreats quickly as city soldiers catch the two fighting. Romeo realizes \
that being caught fighting might mean the end of him and Juliet, so he too vanishes."""],

["""The two hear city soldiers running down the street. "This isn't over!" screams \
Tybalt as he dashes off. Romeo was not interested in trouble for breaking his curfew, \
so he leaves Mercutio's body in search of Juliet."""],

["""Juliet, unwilling to marry the Count Paris, confides in Friar Lawrence about poisons. \
The apothecary is willing to trade poison for some of Capulet's riches."""],

["""Juliet's internal struggle realizes itself when she thinks Romeo is dead. She decides \
that without Romeo, she too does not to want to remain in this life. She confides in \
the Friar Lawrence and then purchases a single serving of poison to seal her fate."""],

["""Before Juliet has time to prepare the poison, Romeo appears and Juliet prepares to \
jump down to the courtyard to escape. """],

["""Romeo catches Juliet in the midst of her suicide. "Juliet, I'm here! What are \
you doing? Is that poison?" Juliet stops herself and is overcome with tears from her \
severe emotional trauma. "Juliet we can escape. Come with me and all this trouble \
will be over, but be quick before someone finds us here." Juliet agrees and throws \
a rope down to the courtyard she kept in case the need to escape emerged."""],

["""Romeo's fate is almost predetermined. Capulet appears and quickly rushes towards \
Romeo, taking him down once and twice. Romeo is bloodied and weak."""],

[""""Not so fast, beautiful Romeo!" Capulet sneers. Romeo's heart stops suddenly. He \
does not intend to turn around and face Capulet alone. Romeo left his dagger at \
Mercutio's body so he runs off behind a dark corner. Luckily, Romeo finds a \
box of broomsticks. He grabs one to at least defend himself. Juliet screams at her \
father, "Not my Romeo! He does not deserve death!" """],

["""Romeo cannot recuperate. He fills his thoughts with Juliet as Capulet's dagger \
proves Romeo's mortality. Romeo had been doomed from the beginning and Juliet \
quickly imbibes the poison."""],

["""Capulet corners Romeo and carefully blocks Capulet's dagger with his broomstick. \
There is an attempt to escape and Romeo dashes, but is caught in Capulet's dagger. \
He falls to the ground as Capulet stands over him. His leg is badly injured and \
Capulet's immense force stands above him. "This treachery with the Montague's has \
gone on far too long. Your defeat will be a message that this city is ours and \
there is no way we are willing to give up." Just then a dozen Capulet thugs wrap \
around the fight and drag the damaged Romeo away. Juliet is heartbroken. She cannot \
think to see Romeo's dying body and takes the poison herself. "I cannot be in this \
world without Romeo!" """],

["""Romeo gathers up his strength, revitalized by the love of Juliet. Juliet tosses \
down into the grass and Romeo is already confident he has won. He uncaps the poison \
and tosses it into Capulet's face with one motion. Capulet is knocked to the ground \
and Juliet has descended the rope to the courtyard. The two lovers carefully slip \
out of the city. """],

["""Juliet runs into her room and finds the vial of poison. She makes her way back \
to the window and tosses the vial below. "Romeo! Use the vial!" she yells. Romeo \
looks up just in time and snatches the poison from the air. "Not so fast, Romeo! \
If you take that poison--I win!" Without hesitation Romeo unplugs the vial and \
tosses the poison into Capulet's face. "My eyes! What devil's magic is this poison!" \
Capulet makes one final motion to stab Romeo. He lunges towards our hero and plunges \
the dagger into Romeo's leg. Capulet is unable to recover, and Romeo looks up to \
Juliet. "Quickly Romeo! Help me down!" Juliet and Romeo attempt to sneak out of the \
city unnoticed."""],

["""Romeo narrowly escapes the trap."""]
]

nodes = [
    # list of plot nodes initialized with name, templates, nextNodeID, and feature
    ('0Intro',                       [1,2,3,4,5,6],       None),

    ('1Benvollo slain',              [3,4,5,6,7,8,9,10],      [features.DEATH]),
    ('2Benvollo slain dramatically', [3,4,5,6,7,8,9,10],      [features.DRAMATIC, features.DEATH]),

    ('3Montague forbids',            [5,6,7,8,9,10],      None),
    ('4Montague forbids d',          [5,6,7,8,9,10],      [features.DRAMATIC]),

    ('5Romeo visits Juliet',         [7,8,9,10],      features.TRAVEL),
    ('6Romeo visits Juliet d',       [7,8,9,10],      [features.TRAVEL, features.DRAMATIC]),

    ('7capulet wife sees Romeo',     [9,10],     None),
    ('8capulet wife sees Romeo D',   [9,10],     [features.DRAMATIC]),

    ('9capulet wife tells capulet',  [11,12],    None),
    ('10capulet wife tells c d',      [11,12],    [features.DRAMATIC]),

    ('11capulet tries to trick r',    [13,14,41],    None),
    ('12capulet tries to trick r d',  [13,14,41],    [features.DRAMATIC]),

    ('13r falls for trick',           [15,16,17,18,19,20],    None),
    ('14r falls for trick d',         [15,16,17,18,19,20],    [features.DRAMATIC]),

    ('15capulet injures montague',    [17,18,19,20],    [features.DEATH]),
    ('16capulet injures montague d',  [17,18,19,20],    [features.DRAMATIC, features.DEATH]),

    ('17montague wants to kill c',    [19,20],    None),
    ('18montague wants to kill c d',  [19,20],    [features.DRAMATIC]),

    ('19romeo hears j marriage',      [21,22],    None),
    ('20romeo hears j marriage d',    [21,22],    [features.DRAMATIC]),

    ('21romeo decides to run',        [23,24,29,30],    [features.TRAVEL]),
    ('22romeo decides to run d',      [23,24,29,30],    [features.TRAVEL, features.DRAMATIC]),

    ('23romeo sees mercutio die',     [25,26,27,28],    [features.DEATH]),
    ('24romeo sees mercutio die d',   [25,26,27,28],    [features.DEATH, features.DRAMATIC]),

    ('25romeo fights tybalt 14a',     [29,30],    [features.DEATH]),
    ('26romeo fights tybalt 14a d',   [29,30],    [features.DEATH, features.DRAMATIC]),

    ('27romeo fights tybalt 14a',     [29,30],    None),
    ('28romeo fights tybalt 14a d',   [29,30],    [features.DRAMATIC]),

    ('29juliet gets poison',          [31,32],    None),
    ('30juliet gets poison d',        [31,32],    [features.DRAMATIC]),

    ('31romeo goes to juliet',        [33,34],    [features.TRAVEL]),
    ('32romeo goes to juliet d',      [33,34],    [features.TRAVEL, features.DRAMATIC]),

    ('33romeo is confronted by c',    [35,36,37,38,39,40],    None),
    ('34romeo is confronted by c d',  [35,36,37,38,39,40],    [features.DRAMATIC]),

    ('35romeo is scared' ,            [37,38,39,40],    None),
    ('36romeo is scared d',           [37,38,39,40],    [features.DRAMATIC]),

    ('37romeo defeats capulet',       None,    [features.DEATH]),
    ('38romeo defeats capulet d',     None,    [features.DEATH, features.DRAMATIC]),

    ('39capulet defeats romeo',       None,    None),
    ('40capulet defeats romeo',       None,    [features.DRAMATIC]),

    ('41romeo escapes trap',          [17,18,19,20],  None)

]

plot = skin.initPlot(nodes, templates, wordset)