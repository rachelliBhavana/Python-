'''
Write a recursive program which accept number from user and return  summation of its digits.  
Input : 879  
Output : 24 
'''
'''
Function Name : sum
Description :  recursive program which accept number from user and return  summation of its digits.  
Input : 798
Output : 24 
Author : Bhavana Rachelli
Date : 02 July 2021
'''
def sum(n):
 if(n==0):
    return 0
 else:
    return(n%10)+sum(n//10)
	
def main():
 
 print("enter the no:")
 value=int(input())
 ret=sum(value)
 print("sum is :",ret)
 

if __name__=="__main__":
 main()