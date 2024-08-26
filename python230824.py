a=int(input("Enter Balance:"))
b=int(input("enter Deposite"))
c=int(input("Enter withdraw:"))
if(a<0):
    print("Balance")
elif(b<=a):
    print("Deposite")
elif(c>b):
    print("Withdraw")
else:
    print("Exit")


