'''
Write a recursive program which display below pattern.  
Input : 5  
Output : 5 4 3 2 1
'''
'''
Function Name : rec
Description :  recursive program which display below pattern.
Input : 5
Output : 5 4 3 2 1 
Author : Bhavana Rachelli
Date : 01 July 2021
'''
def rec(ino):
 if(ino>0):
  print(ino,end=" ")
  rec(ino-1)
def main():
 
 print("enter the no:")
 value=int(input())
 rec(value)
 
 

if __name__=="__main__":
 main()