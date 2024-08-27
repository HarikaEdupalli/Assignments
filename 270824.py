#Accessing String
S="Learning Python"
print(S[2])
print(S[5])

#Indexing String
s="Learning Python"
print(s[0:12:2]) 

l=len(s)
for i in range(1):
    if(s[i]=="P"):
        print(i)
#manipulating String (Concatenation ,Repetation)
S1="Python"
S2="Django"
print(S1+S2)
print(S1+" "+S2)

print((S1+" ")*10)
print(S1*5 +S2*5)
#String Methods: Find
word="Learning Pyhton is very easy"
print(word.find("P"))
print(word.find("h"))
#Count()
word="Learning Pyhton is very easy"
print(word.count("r"))
#Strip()
w="learning"
print(len(w))
w1=w.strip()
print(len(w))
#rstrip()
w="learning"
w1=w.rstrip()
print(len(w1))
#Split()
w="Learning Pyhton is very easy"
print(word.split("e"))
w="Learning Pyhton is very easy"
print(len(word))
l=word.split("n")
print(len(l))

#Slicing for String Collection
st="Pyhton is easy"
print(st[-14:-9+1])
print(st[-1:-14-1:-1])
print(st[-9:-14-1:-1])








   




