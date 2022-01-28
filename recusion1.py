# Write a program to find x to the power n (i.e. x^n). Take x and n from the user. 

def pow(x,y):
    if(y==0):
        return 1
    if(x==0):
        return 0
    return x * pow(x,y-1)  


x=int(input("enter the number "))
y=int(input("enter the power number "))
print(pow(x,y))

