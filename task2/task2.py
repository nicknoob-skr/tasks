import math
import sys

program_name = sys.argv
argument1 = program_name[1]
argument2 = program_name[2]

f = open(argument1, 'r').read()
d = open(argument2, 'r').read()

figur = f.split('\n')
dot = d.split('\n')

x1y1 = figur[0].split(' ')    
x2y2 = figur[1].split(' ')
x3y3 = figur[2].split(' ')
x4y4 = figur[3].split(' ')

x1, y1, x2, y2, x3, y3, x4, y4 = x1y1[0], x1y1[1], x2y2[0], x2y2[1], x3y3[0], x3y3[1], x4y4[0], x4y4[1]

for i in dot:
    pXpY = i.split()
    pX = pXpY[0]
    pY = pXpY[1]
    
    AB = (float(x2) - float(x1))*(float(pY) - float(y1)) - (float(y2) - float(y1))*(float(pX) - float(x1))
    BC = (float(x3) - float(x2))*(float(pY) - float(y2)) - (float(y3) - float(y2))*(float(pX) - float(x2))
    CD = (float(x4) - float(x3))*(float(pY) - float(y3)) - (float(y4) - float(y3))*(float(pX) - float(x3))
    DA = (float(x1) - float(x4))*(float(pY) - float(y4)) - (float(y1) - float(y4))*(float(pX) - float(x4))
    
    if AB < 0 and BC < 0 and CD < 0 and DA < 0:
        print("2")
    elif AB > 0 or BC > 0 or CD > 0 or DA > 0:
        print("3")
    elif pX == x1 and pY == y1 or pX == x2 and pY == y2 or pX == x3 and pY == y3 or pX == x4 and pY == y4:
        print("0")
    elif AB == 0 or BC == 0 or CD == 0 or DA == 0:
        print("1")
    



