import random
from plot.node import PlotNode

def getChoice(options):
    choice = random.choice(options)
    options.remove(choice)
    return choice

def initWordset(wordset, constants, choices):
    if (constants):
        for key in constants:
            wordset[key] = [random.choice(constants[key])]
    if (choices):
        for (keys, options) in choices:
            for key in keys:
                wordset[key] = getChoice(options)

def initPlot(nodes, templates, wordset, constants=None, choices=None):
    initWordset(wordset, constants, choices)
    plotNodes = []
    for i in range(len(nodes)):
        n = nodes[i]
        plotNodes.append( PlotNode(n[0], n[1], n[2], templates[i], wordset) )
    return plotNodes