'''
Write a program which accept N numbers from user and store it into List. Accept one another  number from user and return frequency of that number from List.  
Input : Number of elements : 11  
Input Elements : 13 5 45 7 4 56 5 34 2 5 65  Element to search : 5  
Output : 3 
'''
'''
Function Name : fact
Description :  accept N numbers from user and store it into List. 
               Accept one another  number from user and return frequency of that number from List.  
Input : 13 5 45 7 4 56 5 34 2 5 65  Element to search : 5    
Output : 3 
Author : Bhavana Rachelli
Date : 02 July 2021
'''
def count(lst, x): 
    count = 0
    for i in lst: 
        if (i == x): 
            count = count + 1
    return count 

def main():
	
 lst = [13,5,45,7,4,56,5,34,2,5,65] 
 x = 5
 print('{} has occurred {} times'.format(x, count(lst, x)))
 
if __name__=="__main__":
 main() 