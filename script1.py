from sys import*

def main():
  print("---------marvellous infosystem-------")
  print("script title"+argv[0])
  
  if(len(argv)!=2):
    print("insufficient arguments to the script")
    exit()
    
  if(argv[1]=="-u")or(argv[1]=="-U"):
    print("use the script as name.py parameters")
    
  if(argv[1]=="-h")or(argv[1]=="-H"):
    print("this is ademo automation script")  
  
if __name__=="__main__":
 main()