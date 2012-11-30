from plot.node import PlotNode
import plot.features as features

#lists of words used by the templates
wordset = {"@KILLED" : ["slayed", "killed"],
           "@BEAUTIFUL" : ["lovely", "beautiful", "gorgeous", "pretty"],
           "@WALKED" : ["strolled", "walked"]}

#lists of templates used by the plot nodes
templates = [
    ["""As Benvolio @WALKED down a street in Verona, he was waylayed by a rogue group of Capulet thugs. "Thou art tresspassing on Capulet grounds!", shrieked the thugs as they senselessly beat his corpse."""],
    ["""The lovestricken Romeo pleaded with his father to court the @BEAUTIFUL Juliet. However, Montague, still grieving after the loss of Benvolio, forbade Romeo from venturing anywhere near Capulet territory."""],
    ["""Ignoring his father's warnings, Romeo snuck out that night on a mission to catch a potential glimpse of the fair Juliet. To his surprise he sees Juliet standing out on her balcony as he scurries in the brush below. "Wherefore are thou Romeo!" sang Juliet. "I am here, fair lady!" replied Romeo. Their eyes locked in a deep love-filled gaze, but a rustling in the shadows frightened Romeo to retreat."""],
    ["""Capulet is furious when he was told by his wife that Romeo and Juliet had been seeing eachother in spite of the feud. Capulet hated the idea of his daughter's infatuation with a disgusting Montague imp."""],
    ["""Capulet formulates a genious plan to lure Montague into a trap using Romeo's blind love for Juliet as bate. He summons Juliet"""]
]

nodes = [
    # list of plot nodes initialized with name, templates, nextNodeID, and features
    ('Benvollo slain',              [1],        [features.DEATH]),
    ('Montague forbids',            [2,3],      None),
    ('Romeo visits',                [3],        None),
    ('Capulet heard of betrayal',   None,       None)
]

def initPlot():
    plotNodes = []
    for i in range(len(nodes)):
        n = nodes[i]
        plotNodes.append( PlotNode(n[0], n[1], n[2], templates[i], wordset) )
    return plotNodes

plot = initPlot()