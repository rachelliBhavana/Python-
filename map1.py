# A lambda function that returns sq of elements in a list.

lst = [1,2,3,4,5]
lst1 = list(map(lambda x: x*x, lst))
print(lst1)