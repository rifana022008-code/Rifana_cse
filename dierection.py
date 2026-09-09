a=int(input("Enter a number:"))
if (a>20):
    print("error")
elif(a%4==0):
    print("North")
elif(a%4==1):
    print("East")
elif(a%4==2):
    print("south")
else:
    print("west")
