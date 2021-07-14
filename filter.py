# A lambda that returns even numbers from list.

lst = [10,23,46,70,99]
lst1 = list(filter(lambda x: (x % 2 == 0), lst))
print(lst1)