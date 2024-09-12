#python program for nested tuple flattened into single tuple
t=eval(input("Enter the Tuple"))
tup1=sorted(t,key=lambda X:X[1])
print(tuple(tup1))

#Sort a tuple based on second element
tuple_1=eval(input("Enter the Tuple"))
list1=[]
for i in tuple_1:
    str1=str(i)
    if len(str1)==1:
        list1.append(int(str1))
    else:
        str1=list(i)
        for i in str1:
            list1.append(i)
print(list1)
