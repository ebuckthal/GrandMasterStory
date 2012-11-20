import copy
from board import Board
from board import Piece

class ChessMove(object):
   """docstring for ChessMove"""
   def __init__(self, move, lastMove, isWhite=True):
      super(ChessMove, self).__init__()
      # shared between white and black
      self.whiteScore = 0
      self.blackScore = 0
      self.board = None 
      # individual
      self.moveString = move
      self.notes = ''
      self.isWhite = isWhite
      self.check = False #True / False for check
      self.mate = False #True / False for checkmate
      self.capture = None #piece that was captured
      self.castling = None #'Q' or 'K' for king or queen side
      self.promotion = None #promotion type Ex.'Q'
      self.location = None #location tuple (col,row)
      self.dest = None #destination tuple (col,row)
      self.piece = None #piece being moved
      self.pieceType = None #pieceType Ex. 'Q', 'K'..
      #setup
      self.setup(lastMove)
      self.applyMove(move)
     
   def setup(self, lastMove):
      if lastMove:
         self.board = copy.deepcopy(lastMove.board)
         self.whiteScore = lastMove.whiteScore
         self.blackScore = lastMove.blackScore
      else:
         self.board = Board()

   def applyMove(self, move):
      self.parseMove(move)
      if self.dest:
         self.determinePiece()
         self.updateBoard()
      elif self.castling:
         self.applyCastling()

   def parseMove(self, move):
      if 'O-O-O' in move:
         self.castling = 'Q'
      elif 'O-O' in move:
         self.castling = 'K'
      elif '-' in move:
         self.notes += move + '\n'
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
      self.dest = self.board.stringToLoc(self.dest)
      possible = Piece.piecesForType(self.pieceType, self.isWhite)
      if possible:
         for p in possible:
            loc = self.board.locationOfPiece(p)
            if loc == None:
               self.notes += 'Error: piece location not found\n'
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
            self.board[0][0] = Piece.NONE
            self.board[2][0] = Piece.WHITE_KING_E
            self.board[3][0] = Piece.WHITE_ROOK_A
            self.board[4][0] = Piece.NONE
         else:
            self.board[4][0] = Piece.NONE
            self.board[5][0] = Piece.WHITE_ROOK_H
            self.board[6][0] = Piece.WHITE_KING_E
            self.board[7][0] = Piece.NONE
      else:
         if self.castling == 'Q':
            self.board[0][7] = Piece.NONE
            self.board[2][7] = Piece.BLACK_KING_E
            self.board[3][7] = Piece.BLACK_ROOK_A
            self.board[4][7] = Piece.NONE
         else:
            self.board[4][7] = Piece.NONE
            self.board[5][7] = Piece.BLACK_ROOK_H
            self.board[6][7] = Piece.BLACK_KING_E
            self.board[7][7] = Piece.NONE

   def updateBoard(self):
      if not self.location:
         self.notes += 'Error: no move to make\n'
         return

      self.board.setPieceAt(self.location, Piece.NONE)

      if (self.capture):
         self.capture = self.board.pieceAt(self.dest)
         self.board.capturePiece(self.capture)
         if (self.isWhite):
            self.whiteScore += Piece.value[self.capture]
         else:
            self.blackScore += Piece.value[self.capture]

      self.board.setPieceAt(self.dest, self.piece)

   def printBoard(self):
      self.board.printOut()

   def printMove(self):
      print 'Move:', self.moveString
      if self.capture:
         print 'Captured:', Piece.name[self.capture]
      if self.check:
         print 'Check.'
      if self.mate:
         print 'Check Mate!'
      print self.notes
      self.printBoard()
      print '-'*40
