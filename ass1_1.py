'''
Write a program which contains one function named as ChkNum() which accept one  parameter as number. If number is even then it should display “Even number” otherwise  display “Odd number” on console.  
Input : 11 Output : Odd Number  
Input : 8 Output : Even Number 
'''
'''
Function Name : ChkNum
Description :  check the no is odd or even.
Input : 11
Output : Odd Number 
Author : Bhavana Rachelli
Date : 12 July 2021
'''
def ChkNum(no):
   if (no%2==0):
        print("Even Number")
   else:
	    print("Odd Number")
def main():
	  
 value=(int(input("enter the number")))
 ChkNum(value)

if __name__=="__main__":
 main() 