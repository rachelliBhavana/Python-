'''
Write a recursive program which accept number from user and return its  factorial.  
Input : 5  
  
Output : 120
'''
'''
Function Name : fact
Description :  recursive program which accept number from user and return its  factorial.  
Input : 5    
Output : 120 
Author : Bhavana Rachelli
Date : 02 July 2021
'''
def fact(n):
 if(n==0):
    return 1
 return n * fact(n-1)	
 

def main():
 
 print("enter the no:")
 value=int(input())
 ret=fact(value)
 print("factorial is:",ret)
 

if __name__=="__main__":
 main()