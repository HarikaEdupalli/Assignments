#1
output=[]
for num in range(2000,3201):
    if num%7==0 and num%5!=0:
        output.append(num)
print(output)

#2
num=int(input("enter the number"))
nDict={}
for i in range(1,num+1):
    nDict[i]=i*i
print(nDict)    

#3
Num=(input("Enter the comma separated numbers:"))
Num_split=Num.split(',')
num_tuple=tuple(Num_split)
print(num_tuple)
print(Num_split)

#4
Words=input("Enter the words:")
Words_list=Words.split(",")
Words_list.sort()
print((', ').join(Words_list))

#5
word=input("Enter the data:")
word=list(word)
Le,Di=0,0
for i in word:
    if i.isalpha():
        Le=Le+1
    if i.isdigit():
        Di=Di+1
    else:
            pass
print("Letters:",Le)
print("Digits:",Di)

#6
word=input("Enter the data:")
word=list(word)
U,L=0,0
for i in word:
     if i.isupper():
          U=U+1
     if i.islower():
          L=L+1
else:
     pass
print("Upper:",U)
print("Lower:",L)

#7

total=0
while True:
     deposite_withdraw_transac=input()
     if deposite_withdraw_transac==" ":
         break
     else:
          deposite_withdraw_transac=deposite_withdraw_transac.split(" ")
          if deposite_withdraw_transac[0]=="D":
               total=total+int(deposite_withdraw_transac[1])
          elif deposite_withdraw_transac[0]=="W":
               total=total-int(deposite_withdraw_transac[1])
print(total)               

        
                  
    