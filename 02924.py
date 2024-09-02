#Creating Empty list 
t=("Harika",1.5,True,20,[])
print(type(t))
print(type(t[4]))
print(t[4])
#Unpack a tuple into several variables
person=("Harika",23,"Andhra")
name,age,state=person
print(name,age,state)
#Adding items to a tuple
T1=(2,4,6,5,1,7,87)
l=list(T1)
print(l)
l.append(30)
print(l)
T1=tuple(l)
print(T1)
#Converting Tuple into String
t=(25,1.5,True,20)
St=str(t)
print(St)
print(type(St))
#Finding Most Frequent element
t=(2,4,6,3,7,2,5,2,4,5,2)
print(t.count(2))
print(t.count(3))
print(t.count(5))


