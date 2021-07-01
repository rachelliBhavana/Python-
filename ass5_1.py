'''
Write a recursive program which display below pattern.  
Input : 5  
Output : * * * * * 
'''
'''
Function Name : pat
Description :  recursive program which display below pattern.
Input : 5
Output : * * * * *
Author : Bhavana Rachelli
Date : 01 July 2021
'''
def pat(n):
 if(n<1):
    return 
 print("*",end=" ")
 pat(n-1) 

def main():
 
 print("enter the no:")
 value=int(input())
 pat(value)
 
 

if __name__=="__main__":
 main()