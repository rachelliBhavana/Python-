'''
 Write a program which contains one function named as Add() which accepts two numbers  from user and return addition of that two numbers.  
Input : 11 5 Output : 16  
'''
'''
Function Name : Add
Description :  accept two nos from users and return addition of it.
Input : 11 , 5
Output : 16
Author : Bhavana Rachelli
Date : 12 July 2021
'''
def Add(no1,no2):
 sum=no1+no2
 return sum
 
def main():
  value1=int(input("enter 1st no :"))

  value2=int(input("enter 2nd no :"))

  ans=Add(value1,value2)
  print("addition is",ans)
  
if __name__=="__main__":
 main() 