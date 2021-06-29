'''
Write a program which accept N numbers from user and store it into List. Return addition of all  elements from that List.  
Input : Number of elements : 6  
Input Elements : 13 5 45 7 4 56  
Output : 130
'''
'''
Function Name : add
Description : accept N numbers from user and store it into List. Return addition of all  elements from that List.
Input : 1 2 3 4 5 
Output : 15
Author : Bhavana Rachelli
Date : 30 June 2021
'''

sum=0
i=0

def add(data):
   global sum
   global i
   if i<len(data):
        sum=sum+data[i]
        i=i+1
        add(data)		
   return sum 
def main():
	arr=[]
	size=int(input("Enter the size of array:"))
	for i in range(size):
		arr.append(int(input()))
	print("Data is : ",arr)
	print("Adition of array is : ",add(arr))

if __name__=="__main__": 
  main()