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
        
    def generateText(self):
        #optionally pass in features of move for smarter templating
        template = random.choice(self.templates)
        matches = re.finditer("@[a-zA-Z0-9]*", template)
        if matches:
            offset = 0 #offset after inserting or deleting
            for match in matches:
                s = match.start(0) + offset
                e = match.end(0) + offset
                word = random.choice(self.wordset[match.group(0)])
                offset += len(word) - len(match.group(0))
                template = template[:s] + word + template[e:] 
        return template
