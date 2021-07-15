'''
.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that
numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000 
'''
from functools import*

def main():

 arr=[]
 print("enter the number of elements")
 size=int(input())
 
 for i in range(size):
        print("Enter Elements Number : ", i + 1)
        no = int(input())
        arr.append(no)

 ino = list(filter(lambda no:  no>=70 and no<=90, arr))
 print("List after filter: ",ino)
 
	
 adding = list(map(lambda no: no + 10, ino))
 print("List after map: ",adding)
 
 product = reduce(lambda a, b: a * b, adding)
 print("List after reduce: ",product)


if __name__=="__main__":
    main();