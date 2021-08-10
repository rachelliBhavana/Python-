import os
import time
import psutil
from sys import *

def processdisplay(FolderName="Marvellous"):
    
    data=[]
    
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    else:
        print("destination directiory is already there")
        exit()
        
    return data
    
    for proc in psutil.process_iter():
        value=proc.as_dict(attrs=['pid','name','username'])
        data.append(value)
        
    return data    
    
def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : "+argv[0])

    if(len(argv) != 2):
        print("Insufficient arguments")
        exit()
    
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name Directory_Name")
        exit()
        
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : It is used to create log file of running processess")
        exit()
            
    processdisplay(argv[1])
    
if __name__ == "__main__":
    main()