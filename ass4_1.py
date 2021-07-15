'''
Write a program which contains one lambda function which accepts one parameter and return
power of two.
Input : 4 Output : 16
Input : 6 Output : 64 
'''
sq = lambda x:x**2

def main():
	ivalue = int(input("Enter no : "))
	iret = sq(ivalue)
	print(iret)	

if __name__=="__main__":
 main()	