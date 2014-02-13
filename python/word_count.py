# word_count.py
# Jared Bronen
# COMP 23 - Lab 2

import sys

if __name__ == '__main__':
    file = sys.argv[-1]

try:
    f = open(file, "r")
except IOError:
    print "Could not find file"
    exit()
    
a = []
b = []

for line in f:
    for word in line.split():
      a.append(word.lower())
      
a.sort()

b = set(a)
b = list(b)
b.sort()

for i in b:
    print i, a.count(i)

print "There are ", len(a), "words in this file"
f.close()
