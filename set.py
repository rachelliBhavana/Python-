def main():
 arr={10,20.5,"hello",10}
 print(type(arr))
 print(arr)
 print(len(arr))
 for value in arr:
    print(value)
    
 if"hello" in arr:
    print("hello is there")
 arr.add(20)
 print(arr)
 arr.discard(20.5)
 print(arr)
    
if __name__=="__main__":
 main()