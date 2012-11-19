from move import ChessMove

class ChessGame(object):
   """docstring for ChessGame"""
   def __init__(self, gamedict):
      super(ChessGame, self).__init__()
      self.gameDict = gamedict
      self.whiteMoves = []
      self.blackMoves = []
      self.finalScore = (0,0)
      self.setup()

   def setup(self):
      lastMove = None
      for move in self.gameDict['moves']:
         if len(self.blackMoves) > 0:
            lastMove = self.blackMoves[-1]
         self.whiteMoves.append(ChessMove(move[0], lastMove))
         self.blackMoves.append(ChessMove(move[1], self.whiteMoves[-1], False))

      # determine final score
      if len(self.whiteMoves) > len(self.blackMoves):
         self.finalScore = (self.whiteMoves[-1].whiteScore, self.whiteMoves[-1].blackScore)
      else: 
         self.finalScore = (self.blackMoves[-1].whiteScore, self.blackMoves[-1].blackScore)

   def info(self):
      info = str(len(self.whiteMoves)) + ' moves.\n'
      info += 'Final Score: ' + str(self.finalScore[0]) + '-' + str(self.finalScore[1])
      return info

   def gameStats(self):
      moves = self.gameDict['moves']
      stats = {}     

      # checks
      stats['wCheck'] = len(filter(lambda x: "+" in x[0], moves))
      stats['bCheck'] = len(filter(lambda x: "+" in x[1], moves))
      stats['wToBCheckRatio'] = max(1.0, float(stats['wCheck']))/max(1.0, float(stats['bCheck']))

      # promotions (pawn => queen)
      stats['wPromote'] = len(filter(lambda x: "=" in x[0], moves))
      stats['bPromote'] = len(filter(lambda x: "=" in x[1], moves))
      stats['wToBPromoteRatio'] = max(1.0, float(stats['wPromote']))/max(1.0, float(stats['bPromote']))

      # capture of pieces
      stats['wCapture'] = len(filter(lambda x: 'x' in x[0], moves))
      stats['bCapture'] = len(filter(lambda x: 'x' in x[1], moves))
      stats['wToBCaptureRatio'] = max(1.0, float(stats['wCapture']))/max(1.0, float(stats['bCapture']))

      # castles 
      stats['wKCastle'] = len(filter(lambda x: 'O-O' in x[0] and 'O-O-O' not in x[0], moves))
      stats['bKCastle'] = len(filter(lambda x: 'O-O' in x[1] and 'O-O-O' not in x[1], moves))

      stats['wQCastle'] = len(filter(lambda x: 'O-O-O' in x[0], moves))
      stats['bQCastle'] = len(filter(lambda x: 'O-O-O' in x[1], moves))

      # specific parts of the game
      # ==== EARLY (FIRST 1/3) ====
      stats['wEarlyCap'] = len(filter(lambda x: 'x' in x[0], moves[:len(moves)/3]))
      stats['bEarlyCap'] = len(filter(lambda x: 'x' in x[1], moves[:len(moves)/3]))

      stats['wEarlyCheck'] = len(filter(lambda x: '+' in x[0], moves[:len(moves)/3]))
      stats['bEarlyCheck'] = len(filter(lambda x: '+' in x[1], moves[:len(moves)/3]))

      # ==== LATE (LAST 1/3) ====
      stats['wLateCap'] = len(filter(lambda x: 'x' in x[0], moves[2*len(moves)/3:]))
      stats['bLateCap'] = len(filter(lambda x: 'x' in x[1], moves[2*len(moves)/3:]))

      stats['wLatePromote'] = len(filter(lambda x: '=' in x[0], moves[2*len(moves)/3:]))
      stats['bLatePromote'] = len(filter(lambda x: '=' in x[1], moves[2*len(moves)/3:]))


      # Outcome
      if '1/2' in self.gameDict['Result']:
         stats['outcome'] = "tie"
      elif '1-0' in self.gameDict['Result']:
         stats['outcome'] = "white"
      elif '0-1' in self.gameDict['Result']:
         stats['outcome'] = "black"
      else: 
         stats['outcome'] = None

      print sorted(stats.iteritems(), key=lambda x: x[0])
      return stats