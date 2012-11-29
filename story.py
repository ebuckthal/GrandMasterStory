import random
from chess.game import ChessGame
from chess.move import ChessMove
from chess.board import Piece

class Story(object):
    """docstring for Story"""
    def __init__(self, chessGame):
        super(Story, self).__init__()
        self.game = chessGame
        self.characterMap = {}
        self.setupStory()

    def setupStory(self):
        pieces = self.game.mostActivePieces(10)
        for p in pieces:
            self.characterMap[p] = Character(self)

    def readStory(self):
        print 'Once upon a time...'
        for i in range(self.game.totalMoves):
            move = self.game.getMove(i)
            if move.piece in self.characterMap:
                print self.characterMap[move.piece].translateMove(move)


names = ['Bob', 'Joe', 'Jesus', 'Phil', 'Mary', 'Obama', 'Steve', 'Gary', 'George', 'Jessica', 'Helga']
def getName():
    name = random.choice(names)
    names.remove(name)
    return name

class Character(object):
    """docstring for Character"""
    def __init__(self, story):
        super(Character, self).__init__()
        self.name = getName()
        self.story = story

    def translateMove(self, chessMove):
        sentence = self.name + ' moved from ' + str(chessMove.location) + ' to ' + str(chessMove.dest)
        if chessMove.capture:
            if chessMove.capture in self.story.characterMap:
                sentence += ' and killed ' + self.story.characterMap[chessMove.capture].name
            else:
                sentence += ' and killed a random guy'
        sentence += '.'
        return sentence
        
