'''
Write a program which accept number from user and check whether that number is positive or  negative or zero.  
Input : 11 Output : Positive Number  
Input : -8 Output : Negative Number  
Input : 0 Output : Zero  
'''
def chk(no):
 if no>0:
    print("positive no.")
 elif no<0:
    print("negative no")
 elif no==0:
    print("no is zero")
	
def main():
  value=(int(input("enter the value"))) 
  chk(value)
 
if __name__=="__main__":
 main()