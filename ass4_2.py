'''
Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
Input : 4 3 Output : 12
Input : 6 3 Output : 18 
'''
mul=lambda ino1,ino2:ino1*ino2

def main():
 ivalue1=int(input("enter the 1st no:"))
 ivalue2=int(input("enter the 2nd no:"))
 iret=mul(ivalue1,ivalue2)
 print(iret)
 
if __name__=="__main__":
 main()