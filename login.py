username=str(input("username:"))
password=str(input("password:"))
status=str(input("status:"))
role=str(input("role:"))
list=[usename,password,status,role]
print(["login success","fail"][username=='admin' and password=='123'])


