import numpy as np
import os
import sys

program_name = sys.argv
argument1 = program_name[1]
directory = argument1

path_f = []
for d, dirs, files in os.walk(argument1):
    for f in files:
        path = os.path.join(d,f)
        path_f.append(path)

Cash1 = path_f[0]
Cash2 = path_f[1]
Cash3 = path_f[2]
Cash4 = path_f[3]
Cash5 = path_f[4]

cash1 = open(Cash1, 'r').read()
cash2 = open(Cash2, 'r').read()
cash3 = open(Cash3, 'r').read()
cash4 = open(Cash4, 'r').read()
cash5 = open(Cash5, 'r').read()

cash1_str = cash1.split('\n')
cash2_str = cash2.split('\n')
cash3_str = cash3.split('\n')
cash4_str = cash4.split('\n')
cash5_str = cash5.split('\n')


i1 = float(cash1_str[0]) + float(cash2_str[0]) + float(cash3_str[0]) + float(cash4_str[0]) + float(cash5_str[0])
i2 = float(cash1_str[1]) + float(cash2_str[1]) + float(cash3_str[1]) + float(cash4_str[1]) + float(cash5_str[1])
i3 = float(cash1_str[2]) + float(cash2_str[2]) + float(cash3_str[2]) + float(cash4_str[2]) + float(cash5_str[2])
i4 = float(cash1_str[3]) + float(cash2_str[3]) + float(cash3_str[3]) + float(cash4_str[3]) + float(cash5_str[3])
i5 = float(cash1_str[4]) + float(cash2_str[4]) + float(cash3_str[4]) + float(cash4_str[4]) + float(cash5_str[4])
i6 = float(cash1_str[5]) + float(cash2_str[5]) + float(cash3_str[5]) + float(cash4_str[5]) + float(cash5_str[5])
i7 = float(cash1_str[6]) + float(cash2_str[6]) + float(cash3_str[6]) + float(cash4_str[6]) + float(cash5_str[6])
i8 = float(cash1_str[7]) + float(cash2_str[7]) + float(cash3_str[7]) + float(cash4_str[7]) + float(cash5_str[7])
i9 = float(cash1_str[8]) + float(cash2_str[8]) + float(cash3_str[8]) + float(cash4_str[8]) + float(cash5_str[8])
i10 = float(cash1_str[9]) + float(cash2_str[9]) + float(cash3_str[9]) + float(cash4_str[9]) + float(cash5_str[9])
i11 = float(cash1_str[10]) + float(cash2_str[10]) + float(cash3_str[10]) + float(cash4_str[10]) + float(cash5_str[10])
i12 = float(cash1_str[11]) + float(cash2_str[11]) + float(cash3_str[11]) + float(cash4_str[11]) + float(cash5_str[11])
i13 = float(cash1_str[12]) + float(cash2_str[12]) + float(cash3_str[12]) + float(cash4_str[12]) + float(cash5_str[12])
i14 = float(cash1_str[13]) + float(cash2_str[13]) + float(cash3_str[13]) + float(cash4_str[13]) + float(cash5_str[13])
i15 = float(cash1_str[14]) + float(cash2_str[14]) + float(cash3_str[14]) + float(cash4_str[14]) + float(cash5_str[14])
i16 = float(cash1_str[15]) + float(cash2_str[15]) + float(cash3_str[15]) + float(cash4_str[15]) + float(cash5_str[15])

my_list = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16]

a = np.max(my_list)
b = int(my_list.index(a)) + 1
print(b)


