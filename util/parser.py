# Author: Connor Lange
# rclange@calpoly.edu
import sys, os
import re

def parseAttributes(text):
  attribs = {}

  for line in text.split("\r\n"):
    m = re.match("\[(.+?)\s(.+?)\]", line)
    if m:
      attribs[m.group(1)] = m.group(2) 

  return attribs 

def parseGameMoves(text):
  lastMove = text.split(" ")[-1]
  text += "\n" # make regex work
  moves = re.findall("\d+\.(.+?)\s+(.+?)\s+?", text) 
  # check last item of last tuple 
  if moves[-1][-1] != lastMove: 
    moves[-1] = (moves[-1][0], moves[-1][1], lastMove)

  return moves

def main():
  chessFile = open(sys.argv[1], 'rb')
  # regex
  data = chessFile.read()
    
  # storage
  games = []

  parts = data.split("\r\n\r\n")
  for i in range(0, len(parts)-1, 2):
    attribs = parseAttributes(parts[i])
    moves = parseGameMoves(parts[i+1])
    attribs["moves"] = moves
    games.append(attribs)

  output = open("gameData.chs", "wb")
  output.write(repr(games))
  output.close()

if __name__ == "__main__":
  main()
