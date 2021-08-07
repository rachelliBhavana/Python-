#auto.py demo   ----compile

from sys import *
import os

def DirectoryTraversal(path):
    print("content of directory are")
    
    for Folder,Subfolder,Filename in os.walk(path):
        print("Directory name is: "+Folder)
        for sub in Subfolder:
            print("Subfolder of "+Folder+"is"+sub)
        for file in Filename:
            print("File name is: "+file)        
    
def main():
   print("Directory traversal script")
   
   if(len(argv)!=2):
        print("error:invalid no of arguments")
        exit()
   if(argv[1]=="-h")or(argv[1]=="-H"):
        print("it is a directory cleaner script")
        exit()
   if(argv[1]=="-u")or(argv[1]=="-U"):
        print("usage:provifde the absolute path of the target directory")
        exit()        
        
   DirectoryTraversal(argv[1])     

if __name__=="__main__":
  main()