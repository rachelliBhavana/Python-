'''
Write a recursive program which display below pattern.  
Input : 5  
Output : 1 2 3 4 5 
'''
'''
Function Name : pat
Description :  recursive program which display below pattern.
Input : 5
Output : 1 2 3 4 5 
Author : Bhavana Rachelli
Date : 01 July 2021
'''
i=0
def pat(n):
  global i
  if(i<n):
        print(i+1,end=" ")
        i=i+1
        pat(n)
  
def main():
 
 print("enter the no:")
 value=int(input())
 pat(value)
 
 

if __name__=="__main__":
 main()
    