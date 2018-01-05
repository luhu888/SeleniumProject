# -*- coding: utf-8 -*-
# __author__=luhu
for i in range(1, 10):
    for j in range(1, i+1):
        print('{1}x{0}={2}'.format(i, j, i*j), end='\t')
    print()