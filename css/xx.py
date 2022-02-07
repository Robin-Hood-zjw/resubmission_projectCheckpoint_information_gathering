import math
import numpy as np
from numpy import random

arr = np.array([5,2,7,3,4,1,6])
base_possibility = 1 / math.factorial(7)
possibilities_num = math.factorial(7)
templist = []

for i in range(possibilities_num):
    x_count = 0
    largest_num = 0
    array = random.permutation(arr)
    for element in array:
        if element > largest_num:
            x_count += 1
            largest_num += 1
    templist.append(x_count)

expected_val = 0
for count in templist:
    expected_val += count / base_possibility
print(expected_val)