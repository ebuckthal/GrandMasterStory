import copy, random

class ChessGame(object):
   """docstring for ChessGame"""
   def __init__(self, gamedict):
      super(ChessGame, self).__init__()
      self.gameDict = gamedict
      self.whiteMoves = []
      self.blackMoves = []
      self.setupMoves()

   def setupMoves(self):
      lastMove = None
      for move in self.gameDict['moves']:
         if len(self.blackMoves) > 0:
            lastMove = self.blackMoves[-1]
         self.whiteMoves.append(ChessMove(move[0], lastMove))
         self.blackMoves.append(ChessMove(move[1], self.whiteMoves[-1], False))

   def info(self):
      info = str(len(self.whiteMoves)) + ' moves.\n'
      if len(self.whiteMoves) > len(self.blackMoves):
         info += "Final score " + str(self.whiteMoves[-1].whiteScore) + '-' + str(self.whiteMoves[-1].blackScore)
      else: 
         info += "Final score " + str(self.blackMoves[-1].whiteScore) + '-' + str(self.blackMoves[-1].blackScore)
      return info

class ChessMove(object):
   """docstring for ChessMove"""
   def __init__(self, move, lastMove, isWhite=True):
      super(ChessMove, self).__init__()
      # shared between white and black
      self.whiteScore = 0
      self.blackScore = 0
      self.board = None
      # individual
      self.isWhite = isWhite
      self.check = False
      self.mate = False
      self.capture = None
      self.castling = None
      self.promotion = None
      self.location = None
      self.dest = None
      self.piece = None
      self.pieceType = None
      #setup
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
      self.parseMove(move)
      if self.dest:
         self.determinePiece()
         self.updateBoard()
      elif self.castling:
         self.applyCastling()

      self.printBoard()
      print '-'*40

   def parseMove(self, move):
      print 'Move:', move
      if 'O-O-O' in move:
         self.castling = 'Q'
      elif 'O-O' in move:
         self.castling = 'K'
      elif '-' in move:
         print move
      else:
         skip = False
         for i in range(len(move) - 1, -1, -1):
            if skip:
               skip = False
               continue
            if move[i] == '+':
               self.check = True
            elif move[i] == '#':
               self.mate = True
            elif i > 0 and move[i-1:i] == '=':
               self.promotion = move[i]
               skip = True
            elif i > 0 and not self.dest:
               self.dest = move[i-1:i+1]
               skip = True
            elif move[i] == 'x':
               self.capture = True
            else:
               if i > 0:
                  self.piece = move[i]
                  self.pieceType = move[i-1:i]
               else:
                  self.pieceType = move[i]

   def determinePiece(self):
      self.dest = stringToLoc(self.dest)
      possible = Piece.piecesForType(self.pieceType, self.isWhite)
      if possible:
         for p in possible:
            loc = locationOfPieceOnBoard(p, self.board)
            if loc == None:
               print 'Error: piece location not found'
               continue
            if self.piece:
               if self.piece.isalpha(): #in column
                  if loc[0] != ord(self.piece) - 97:
                     continue
               else: #in row
                  if loc[1] != int(self.piece) - 1:
                     continue
            if self.pieceType == 'R':
               if (loc[0] == self.dest[0] or loc[1] == self.dest[1]):
                  self.piece = p
                  self.location = loc
                  break
            elif self.pieceType == 'N':
               if ((loc[0] + 2 == self.dest[0] and (loc[1] + 1 == self.dest[1] or loc[1] - 1 == self.dest[1])) or
                (loc[0] - 2 == self.dest[0] and (loc[1] + 1 == self.dest[1] or loc[1] - 1 == self.dest[1])) or
                (loc[1] + 2 == self.dest[1] and (loc[0] + 1 == self.dest[0] or loc[0] - 1 == self.dest[0])) or
                (loc[1] - 2 == self.dest[1] and (loc[0] + 1 == self.dest[0] or loc[0] - 1 == self.dest[0]))):
                  self.piece = p
                  self.location = loc
                  break
            elif self.pieceType == 'B':
               if ((loc[0]+loc[1]) % 2 == (self.dest[0]+self.dest[1]) % 2):
                  self.piece = p
                  self.location = loc
                  break
            elif self.pieceType == 'Q':
               if (loc[0] == self.dest[0] or loc[1] == self.dest[1] or 
                  ((loc[0]+loc[1]) % 2 == (self.dest[0]+self.dest[1]) % 2)):
                  self.piece = p
                  self.location = loc
                  break
            elif self.pieceType == 'K':
               self.piece = p
               self.location = loc
               break
            else: #pawn
               if self.capture:
                  if ((self.dest[0] == loc[0] + 1 or self.dest[0] == loc[0] - 1) and 
                     (self.dest[1] == loc[1] + 1 or self.dest[1] == loc[1] - 1)):
                     self.piece = p
                     self.location = loc
                     break
               else:
                  if (loc[0] == self.dest[0] and self.dest[1] <= loc[1] + 2 and self.dest[1] >= loc[1] - 2):
                     self.piece = p
                     self.location = loc
                     break
      else:
         return

   def applyCastling(self):
      if self.isWhite:
         if self.castling == 'Q':
            self.board[0][0] = -1
            self.board[2][0] = Piece.WHITE_KING_E
            self.board[3][0] = Piece.WHITE_ROOK_A
            self.board[4][0] = -1
         else:
            self.board[4][0] = -1
            self.board[5][0] = Piece.WHITE_ROOK_H
            self.board[6][0] = Piece.WHITE_KING_E
            self.board[7][0] = -1
      else:
         if self.castling == 'Q':
            self.board[0][7] = -1
            self.board[2][7] = Piece.BLACK_KING_E
            self.board[3][7] = Piece.BLACK_ROOK_A
            self.board[4][7] = -1
         else:
            self.board[4][7] = -1
            self.board[5][7] = Piece.BLACK_ROOK_H
            self.board[6][7] = Piece.BLACK_KING_E
            self.board[7][7] = -1

   def updateBoard(self):
      if not self.location:
         print 'Error: no move to make'
         return

      self.board[self.location[0]][self.location[1]] = -1

      if (self.capture):
         self.capture = pieceOnBoard(self.dest, self.board)
         global deadPieces
         deadPieces.append(self.capture)
         if (self.isWhite):
            self.whiteScore += Piece.value[self.capture]
         else:
            self.blackScore += Piece.value[self.capture]

      self.board[self.dest[0]][self.dest[1]] = self.piece

   def printBoard(self):
      for row in range(7,-1,-1):
         rowstring = ''
         for col in range(8):
            rowstring += ' ' + Piece.abbreviation(self.board[col][row]) + ' '
         print rowstring

deadPieces = []

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
   types = {'R':[8, 15], 'N':[9, 14], 'B':[10, 13], 'Q':[11], 'K':[12]}
   @staticmethod
   def abbreviation(piece):
      if piece < 0:
         return "   "
      else:
         return Piece.abbrev[piece]

   @staticmethod
   def isPawn(piece):
      if piece in range(0,8) or piece in range(16,24):
         return True
      return False

   @staticmethod
   def piecesForType(ptype, isWhite):
      if ptype in ['R', 'N', 'B', 'Q', 'K']:
         if isWhite:
            return [p for p in Piece.types[ptype] if not (p in deadPieces)]
         else:
            return [p+16 for p in Piece.types[ptype] if not ((p+16) in deadPieces)]
      else:
         if isWhite:
            return [p for p in range(0,8) if not (p in deadPieces)]
         else:
            return [p for p in range(16,24) if not (p in deadPieces)]

      
def stringToLoc(strloc):
   v1 = ord(strloc[0]) - 97
   v2 = int(strloc[1]) - 1
   return (v1, v2)

def pieceOnBoard(loc, board):
   return board[loc[0]][loc[1]]

def locationOfPieceOnBoard(piece, board):
   for col in range(8):
      for row in range(8):
         if (board[col][row] == piece):
            return (col,row)
   return None

def startingBoard():
   global deadPieces
   deadPieces = []
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
