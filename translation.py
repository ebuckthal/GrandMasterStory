import random

class Character:
  name
  meetActions = []
  killActions = []
  specialtyActions = []
  prefixFlavors = []
  postfixFlavors = []

  def __init__(self, name, meetActions, killActions, specialtyActions, prefixFlavors, postfixFlavors):
    self.name = name
    self.meetActions = meetActions
    self.killActions = killActions
    self.specialtyActions = specialtyActions
    self.prefixFlavors = prefixFlavors
    self.postfixFlavors = postfixFlavors

  def generateEvent(self, ChessMove, AliveCharacters):
    move = random.randint(0,2)
    if move = 0:
      r = random.randint(0, len(meetActions))
      action = meetAction[r]
    elif move = 1:
      r = random.randint(0, len(killActions))
      action = killActions[r]
    else:
      r = random.randint(0, len(specialtyActions))
      action = specialtyActions[r]

    prefix = prefixFlavors[random.randint(0, len(prefixFlavors))]
    postfix = postfixFlavors[random.randint(0, len(postfixFlavors))]

    target = AliveCharacters[random.randint(0, len(AliveCharacters))]

    return prefix + ' ' + name + ' ' + action + ' ' + AliveCharacters + ' ' + postfix + '.'


def __main__():

  name = 'romeo'
  killActions = ['greet', 'meet', 'surprise']



  c = Character(name, meetActions, killActions, specialtyActions, prefixFlavors, postfixFlavors)

  alive = ['a', 'b', 'c', 'd', 'e']
