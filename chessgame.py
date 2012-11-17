import copy

class ChessGame(object):
   """docstring for ChessGame"""
   def __init__(self, gamedict):
      super(ChessGame, self).__init__()
      self.gameDict = gamedict
      self.moves = []
      self.setupMoves()

   def setupMoves(self):
      lastMove = None
      for move in self.gameDict['moves']:
         if len(self.moves) > 0:
            lastMove = self.moves[-1]
         self.moves.append(ChessMove(move,lastMove))

   def info(self):
      return str(len(self.moves)) + ' moves.'

class ChessMove(object):
   """docstring for ChessMove"""
   def __init__(self, move, lastMove):
      super(ChessMove, self).__init__()
      self.board = None
      self.whiteScore = 0
      self.blackScore = 0
      self.setup(lastMove)
      self.applyMove(move)
     
   def setup(self, lastMove):
      if lastMove:
         self.board = copy.deepcopy(lastMove.board)
         self.whiteScore = lastMove.whiteScore
         self.blackScore = lastMove.blackScore
      else:
         self.board = startingBoard()

   def applyMove(self, move):
      print 'TODO apply move: ', move

   def printBoard(self):
      for col in range(8):
         rowstring = ''
         for row in range(8):
            rowstring += ' ' + Piece.abbreviation(self.board[row][col]) + ' '
         print rowstring

class Piece:
   WHITE_PAWN_A, WHITE_PAWN_B, WHITE_PAWN_C, WHITE_PAWN_D, WHITE_PAWN_E, WHITE_PAWN_F, WHITE_PAWN_G, WHITE_PAWN_H = range(0,8)
   WHITE_ROOK_A, WHITE_KNIGHT_B, WHITE_BISHOP_C, WHITE_QUEEN_D, WHITE_KING_E, WHITE_BISHOP_F, WHITE_KNIGHT_G, WHITE_ROOK_H = range(8,16)
   BLACK_PAWN_A, BLACK_PAWN_B, BLACK_PAWN_C, BLACK_PAWN_D, BLACK_PAWN_E, BLACK_PAWN_F, BLACK_PAWN_G, BLACK_PAWN_H = range(16,24)
   BLACK_ROOK_A, BLACK_KNIGHT_B, BLACK_BISHOP_C, BLACK_QUEEN_D, BLACK_KING_E, BLACK_BISHOP_F, BLACK_KNIGHT_G, BLACK_ROOK_H = range(24,32)
   name = ["WHITE_PAWN_A", "WHITE_PAWN_B", "WHITE_PAWN_C", "WHITE_PAWN_D", "WHITE_PAWN_E", "WHITE_PAWN_F", "WHITE_PAWN_G", "WHITE_PAWN_H",
            "WHITE_ROOK_A", "WHITE_KNIGHT_B", "WHITE_BISHOP_C", "WHITE_QUEEN_D", "WHITE_KING_E", "WHITE_BISHOP_F", "WHITE_KNIGHT_G", "WHITE_ROOK_H",
            "BLACK_PAWN_A", "BLACK_PAWN_B", "BLACK_PAWN_C", "BLACK_PAWN_D", "BLACK_PAWN_E", "BLACK_PAWN_F", "BLACK_PAWN_G", "BLACK_PAWN_H",
            "BLACK_ROOK_A", "BLACK_KNIGHT_B", "BLACK_BISHOP_C", "BLACK_QUEEN_D", "BLACK_KING_E", "BLACK_BISHOP_F", "BLACK_KNIGHT_G", "BLACK_ROOK_H"]
   abbrev = ["WPa", "WPb", "WPc", "WPd", "WPe", "WPf", "WPg", "WPh",
                   "WRa", "WNb", "WBc", "WQd", "WKe", "WBf", "WNg", "WRh",
                   "BPa", "BPb", "BPc", "BPd", "BPe", "BPf", "BPg", "BPh",
                   "BRa", "BNb", "BBc", "BQd", "BKe", "BBf", "BNg", "BRh"]
   value = [1, 1, 1, 1, 1, 1, 1, 1, 
            5, 3, 3, 9, 100, 3, 3, 5,
            1, 1, 1, 1, 1, 1, 1, 1, 
            5, 3, 3, 9, 100, 3, 3, 5]
   @staticmethod
   def abbreviation(piece):
      if piece < 0:
         return "   "
      else:
         return Piece.abbrev[piece]
      

def startingBoard():
   board = []
   for i in range(8):
      board.append([-1] * 8)
   #fill in board
   for c in range(8): #white pieces
      board[c][0] = c + 8
   for c in range(8): #white pawns
      board[c][1] = c
   for c in range(8): #black pawns
      board[c][6] = c + 16
   for c in range(8): #black pieces
      board[c][7] = c + 24
   return board

