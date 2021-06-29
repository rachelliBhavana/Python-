'''
Write a program which accept N numbers from user and store it into List. Return Maximum  number from that List.  
Input : Number of elements : 7  
Input Elements : 13 5 45 7 4 56 34  
Output : 56  
'''
'''
Description : accept N numbers from user and store it into List. Return Maximum of all  elements from that List.
Input : 1 2 3 4 5 
Output : 5
Author : Bhavana Rachelli
Date : 30 June 2021
'''
def main():
	arr=[]
	size=int(input("Enter the size of array"))
	for i in range(size):
		arr.append(int(input()))
	print("Data is : ",arr)
	print("Maximum number is : ",max(arr))	


if __name__ == '__main__':
		main()	