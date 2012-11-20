
deadPieces = []

class Piece:
   NONE = -1
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
   def isWhite(piece):
      if piece < 16:
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

class Board(list):
   """docstring for Board"""
   def __init__(self):
      super(Board, self).__init__()
      global deadPieces
      deadPieces = []
      for i in range(8):
         self.append([-1] * 8)
      #fill in board
      for c in range(8): #white pieces
         self[c][0] = c + 8
      for c in range(8): #white pawns
         self[c][1] = c
      for c in range(8): #black pawns
         self[c][6] = c + 16
      for c in range(8): #black pieces
         self[c][7] = c + 24

   def capturePiece(self,piece):
      global deadPieces
      deadPieces.append(piece)

   def setPieceAt(self, loc, piece):
      self[loc[0]][loc[1]] = piece

   def pieceAt(self,loc):
      return self[loc[0]][loc[1]]

   def stringToLoc(self, strloc):
      v1 = ord(strloc[0]) - 97
      v2 = int(strloc[1]) - 1
      return (v1, v2)

   def locationOfPiece(self, piece):
      for col in range(8):
         for row in range(8):
            if (self[col][row] == piece):
               return (col,row)
      return None

   def printOut(self):
      for row in range(7,-1,-1):
         rowstring = ''
         for col in range(8):
            rowstring += ' ' + Piece.abbreviation(self[col][row]) + ' '
         print rowstring

