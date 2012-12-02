import random, re

class PlotNode(object):
    """An action in the plot"""
    def __init__(self, name, nextNodes, features, templates, wordset):
        super(PlotNode, self).__init__()
        self.name = name
        self.nextNodes = nextNodes
        self.features = features
        self.templates = templates
        self.wordset = wordset
        
    def getReplacementForTag(self, tag, gameFeatures=None):
        if gameFeatures and (tag in gameFeatures):
            print tag, gameFeatures[tag]
            if gameFeatures[tag] in self.wordset:
                tag = gameFeatures[tag]
        return random.choice(self.wordset[tag])

    def generateText(self, gameFeatures=None):
        #optionally pass in features of move for smarter templating
        template = random.choice(self.templates)
        matches = re.finditer("@[a-zA-Z0-9]*", template)
        if matches:
            offset = 0 #offset after inserting or deleting
            for match in matches:
                s = match.start(0) + offset
                e = match.end(0) + offset
                tag = match.group(0)
                word = self.getReplacementForTag(tag, gameFeatures)
                offset += len(word) - len(match.group(0))
                template = template[:s] + word + template[e:] 
        return template
