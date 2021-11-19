# Test project
# by Zaur Hamzayev
'''
numpy,pandas,odd and even numbers
mean and median of list
'''

import numpy as np
import pandas as pd

empty_list = []
n = int(input())

for x in range(0, n):
    empty_list.append(x**2)

print(empty_list)
print(sum(empty_list))

d = {'odd_numbers$':0, 'even_numbers$':0}
for z in empty_list:
    if z%2 == 0:
        d['odd_numbers$'] += 1
    elif z%2 != 0:
        d['even_numbers$'] += 1
    else:
        pass

print(d)

def median_list():
    print("Mean of list: ", sum(empty_list)//len(empty_list))
    print("Median of list: ", np.median(empty_list))
    return

median_list()

# I will write 10 in input