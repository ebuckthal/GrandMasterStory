import random, re

class PlotNode(object):
    """An action in the plot"""
    def __init__(self, name, nextNodes, features, templates, wordset, resources):
        super(PlotNode, self).__init__()
        self.name = name
        self.empty = False
        self.nextNodes = nextNodes
        self.features = features
        self.templates = templates
        self.resources = resources
        self.wordset = wordset
        
    def getReplacementForTag(self, tag, gameFeatures=None, depth=0):
        if gameFeatures and (tag in gameFeatures):
            if gameFeatures[tag] in self.wordset:
                tag = gameFeatures[tag]
        if (self.resources) and (tag in self.resources):
            word = random.choice(self.resources[tag])
            if (depth == 0):
                self.resources[tag].remove(word)
                if len(self.resources[tag]) == 0: #remove list 
                    self.resources.pop(tag)
            return word
        return random.choice(self.wordset[tag])

    def replaceTags(self, text, gameFeaturesDict=None, depth=0):
        matches = re.finditer("@[a-zA-Z0-9]*", text)
        if matches:
            offset = 0 #offset after inserting or deleting
            for match in matches:
                s = match.start(0) + offset
                e = match.end(0) + offset
                tag = match.group(0)
                word = self.getReplacementForTag(tag, gameFeaturesDict, depth)
                word = self.replaceTags(word, gameFeaturesDict, depth+1)
                offset += len(word) - len(match.group(0))
                text = text[:s] + word + text[e:] 
        return text

    def generateText(self, gameFeaturesDict=None):
        #optionally pass in features of move for smarter templating
        if (self.empty):
            return None
        template = random.choice(self.templates)
        self.templates.remove(template)
        if (len(self.templates) == 0):
            self.empty = True
        return self.replaceTags(template, gameFeaturesDict)
