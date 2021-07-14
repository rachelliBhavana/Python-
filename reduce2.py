# Calculate the sum of numbers from 1 to 50 using reduce() function.

from functools import *

sum = reduce(lambda a,b: a+b, range(1,51))
print(sum)