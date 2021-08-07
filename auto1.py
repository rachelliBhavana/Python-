from sys import *
import os

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

if __name__=="__main__":
  main()