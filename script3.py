import psutil
from sys import *

def processdisplay():
    print("list of running processess")
    
    data=[]
    for proc in psutil.process_iter():
        value=proc.as_dict(attrs=['pid','name','username'])
        data.append(value)
        
    return data    
    
def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : "+argv[0])

    arr=processdisplay()
    for element in arr:
        print(element)
    
if __name__ == "__main__":
    main()
