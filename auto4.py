from sys import *
import os
import hashlib

def Calculatechecksum(path,blocksize=1024):
    fd=open(path,'rb')
    hobj=hashlib.md5()
    
    buffer=fd.read(blocksize)
    while len(buffer)>0:
        hobj.update(buffer)
        buffer=fd.read(blocksize)
    fd.close()
    return hobj.hexdigest()    

def DirectoryTraversal(path):
    print("content of directory are")
    
    duplicate={}
    for Folder,Subfolder,Filename in os.walk(path):
        print("Directory name is: "+Folder)
        for sub in Subfolder:
            print("Subfolder of "+Folder+"is"+sub)
        for file in Filename:
            print("File name is: "+file)        
            actualpath=os.path.join(Folder,file)
            hash=Calculatechecksum(actualpath)
            print(hash)
            
            if hash in duplicate:    
                duplicate[hash].append(actualpath)
            else:    #there is no checksum
                duplicate[hash]=[actualpath]
    return duplicate 

def DisplayDuplicate(duplicate):
    output=list(filter(lambda x:len(x)>1,duplicate.values()))
    if(len(output)>0):
        print("there are duplicate files")
    else:
        print("there are no duplicate")
        return
        
    print("list of duplicate files:")
    icnt=0
    for result in output:
        for path in result:
            icnt+=1
            if icnt>=2:
                print("%s"%path)
        icnt=0
        
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
   arr={}     
   arr=DirectoryTraversal(argv[1]) 
   DisplayDuplicate(arr)   

if __name__=="__main__":
  main()