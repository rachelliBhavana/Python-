''''
Write a program which accept N numbers from user and store it into List. Return Minimum  number from that List.  
Input : Number of elements : 4  
Input Elements : 13 5 45 7  
Output : 5 
'''
'''
Function Name : minv
Description : accept N numbers from user and store it into List. Return Minimum of all  elements from that List.
Input : 1 2 3 4 5 
Output : 1
Author : Bhavana Rachelli
Date : 30 June 2021
'''

def minv(data):
 n=0
 i=0
 
 if i < len(data):
    n=data[i]
	
 return n	
	
    
def main():
 arr=[]
 
 size=int(input("enter the size of the array:"))
 
 for i in range(size): arr.append(int(input()))
 
 print("data is : ",arr)
 print("minimum is :",minv(arr))
 
 
 
if __name__=="__main__":
 main() 