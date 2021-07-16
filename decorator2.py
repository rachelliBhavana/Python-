# A python program to apply a decorator using @ symbol

def decor(fun):
	def inner():
		value=fun()
		return value+2
	return inner
	
@decor
def num():
    return 20

print(num())    		