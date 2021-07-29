def main():
  employee={11:{"name":"piyush","age":30},21:{"name":"raj","age":31},31:{"name","amar","age":32}}
  
  print("employee information is:")
  for eid,einfo in employee.items():
    print("employee id is ",eid)
    for key in einfo:
        print(key,einfo[key])
if __name__=="__main__":
 main() 