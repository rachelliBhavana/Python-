# A decorator to increase the value of function by 2.

def decor(fun):
	def inner():
		value = fun()
		return value+2
	return inner
	
def num():
    return 10

result_fun = decor(num)
print(result_fun())    		