# A lambda function that returns bigger number

max =lambda x,y: x if x>y else y 
a,b =[int(n) for n in input("Enter two nos : ").split(',')]
print("Bigger no = ",max(a,b))