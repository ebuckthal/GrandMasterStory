#!/usr/bin/python 
import re
import sys
f = open(sys.argv[1], "rb")
data = f.read()
f.close()

o = open(sys.argv[1]+"_new", "wb")
linesize = 0
words = data.split(" ")
for word in words:
  linesize += len(word) + 1
  if linesize > 100: 
    o.write("\n")
    linesize = 0
  o.write(word+" ")
o.close()
