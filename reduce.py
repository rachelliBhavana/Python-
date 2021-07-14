# A Lambda function  to calculate products of elements of a list.

from functools import *

lst = [1,2,3,4,5]
result = reduce(lambda x,y: x*y, lst)
print(result)