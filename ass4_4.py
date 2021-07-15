'''
Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
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

 even = list(filter(lambda no:  no%2==0, arr))
 print(even)
 sq = list(map(lambda no: no**2, even))
 print(sq)
 sum = reduce(lambda a, b: a + b, sq)
 print(sum)


if __name__=="__main__":
 main()