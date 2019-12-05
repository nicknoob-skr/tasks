import numpy as np
import sys

program_name = sys.argv
argument = program_name[1] 

file = open(argument, 'r').read()
strings = file.split('\n')

res = list(map(float, strings))
a = np.percentile(res, 90)
b = np.median(res)
c = np.max(res)
d = np.min(res)
f = np.mean(res)

print('%.2f' % a)
print('%.2f' % b)
print('%.2f' % c)
print('%.2f' % d)
print('%.2f' % f)
