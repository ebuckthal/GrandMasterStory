import random, re
import chess.features as f 

class PlotNode(object):
    """An action in the plot"""
    def __init__(self, name, nextNodes, features, templates, wordset, resources, holistics, rememberings):
        super(PlotNode, self).__init__()
        self.name = name
        self.empty = False
        self.nextNodes = nextNodes
        self.features = features
        self.templates = templates
        self.resources = resources
        self.wordset = wordset
        self.holistics = holistics
        self.rememberings = rememberings
        self.moveGroupFeatures = []

    def getHolistics(self, gameFeaturesDict=None, gamePastFeaturesDict=None):

       wasWinning = gamePastFeaturesDict[f.LOSE] < gamePastFeaturesDict[f.WIN]

       willWin = gameFeaturesDict[0]['victory']

       if f.WIN in self.moveGroupFeatures:
         nowWinning = True
       else:
         nowWinning = False

       for ((was, will), text) in self.holistics:
          if was == wasWinning and will == willWin:

             if len(text) > 0:
               holistic = random.choice(text)
               text.remove(holistic) 

               return holistic

       return ''

    def getRememberings(self, gameFeaturesDict=None, gamePastFeaturesDict=None):
       #rememberings
       for (res, feature, temp) in self.rememberings:

          if len(self.resources[res][1]) > 0:

             if feature in self.moveGroupFeatures:

                tag = random.choice(self.resources[res][1])
                self.resources[res][1].remove(tag)

                template = random.choice(temp)

                string = self.replaceTemplateWithTag(template, self.getReplacementForTag(tag))
                print string
                print self.moveGroupFeatures

                return string 

       return  ''

    def replaceTemplateWithTag(self, text, word):
        matches = re.finditer("@[a-zA-Z0-9]*", text)
        if matches:
            offset = 0 #offset after inserting or deleting
            for match in matches:
                s = match.start(0) + offset
                e = match.end(0) + offset
                tag = match.group(0)
                offset += len(word) - len(match.group(0))
                text = text[:s] + word + text[e:] 
        return text


    def getReplacementForTag(self, tag, gameFeatures=None, depth=0):
        if gameFeatures and (tag in gameFeatures):
            if gameFeatures[tag] in self.wordset:
                tag = gameFeatures[tag]
        if (self.resources) and (tag in self.resources):
            word = random.choice(self.resources[tag][0])
            if (depth == 0):
                self.resources[tag][0].remove(word)
                self.resources[tag][1].append(word)
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

    def generateText(self, gameFeaturesDict=None, gamePastFeaturesDict=None):
        #optionally pass in features of move for smarter templating
        if (self.empty):
            return None
        template = random.choice(self.templates)
        self.templates.remove(template)
        if (len(self.templates) == 0):
            self.empty = True

        template = self.getHolistics(gameFeaturesDict, gamePastFeaturesDict) + ' ' + template
        template = self.getRememberings(gameFeaturesDict, gamePastFeaturesDict) + ' ' + template

        return self.replaceTags(template, gameFeaturesDict) 
