# Count()
st="Python Programming"
print(st.count('o'))

#Anagram
st1="Elbow"
st2="Below"
st1=sorted(st1.lower())
st2=sorted(st2.lower())
print("st1 after sorting:",st1)
print("st2 after sorting:",st2)
if(st1==st2):
   print("The strings are Anagrams")
else:
   print("The strings are not Anagrams")

#Plindrome Number or Not
N="123321"
i=0
s=""
while i<len(N):
   s=N[i]+s
   i+=1
   if N==s:
      print("It is a Palindrome")
   else:
      print("It is not a Palindrome")

#Replace the String
st="Python Programming"
new_st=st.replace("Python","Java programming")
print(new_st)

#Replace the Spaces in string with Character
st="Once upon a time"
char='-'
st=st.replace('',char)
print("String after replacing spaces with given character:")
print (st)

#Lowercase char to Uppercase 
s="Python ProGRaMMing"
print(s.upper())

"""Converting Vowels to Uppercase
Name=input("Enter a String:")
res='aeiou'
for i in Name:
   if i in res:
      upr=i.upper()
      st=Name.replace(i,upr)
print("After converting:",st)"""

#Separating  Character
string="Python"
print("Individual characters from given string")
for i in range(0,len(string)):
   print(string[i],end=" ")

#Removing Blank Spaces
string="python programming"
print(string.replace(' ',''))

# String Concatenation By using Join()
S1="Harika"
S2="Edupalli"
Concat_Result=""
Concat_Result=Concat_Result.join([S1+S2])
print(Concat_Result)
# Stirng Concatenation
S1="Python"
S2="Programming"
S3=S1+S2
print(S3)

# Finding Vowels or Consonants
ch='o'
if ch in['a','e','i','o','u']:
   print("It is a Vowel")
else:
   print("It is a Consonant")

#Finding Digit or Not
ch="15"
if(ch.isdigit()):
   print( "It is a Digit")
else:
   print("It is not a Digit")

#Count of Vowels & Consonants
input="hsauybqxnljdieurnpqrbnorn"
vlist=['a','e','i','o','u']
vCount=0
cCount=0
for i in input:
   if i in vlist:
      vCount=vCount+1
   else:
      cCount=cCount+1
print("final count of vowels is:"+str(vCount))
print("final count of Consonants is:"+str(cCount))

#Highest Frequancy Character
str="This is really a string "
print("Max character:" + max(str))  

#Replacing character with '-'
St="Green"
new_St=St.replace("n","k")
print(new_St)

#Counting Alphabets,Digits,Special Characters
St="Hariramu@322*&"
alphabets=digits=special=0
for i in range(len(St)):
   if(St[i].isalpha()):
      alphabets=alphabets+1
   elif(St[i].isdigit()):
      digits=digits+1
   else:
      special=special+1
      print("total no of alphabets in this string",alphabets)
      print("total no of digits in this string",digits)
      print("total no of special in this string",special)

# Finding Digits Without using of  isdigit()
a="24546"
print( a.isdigit())

#Sum of integers in a string
a="Harika7254"
sum=0
for i in a:
   if(i.isnumeric()):
      sum+=int(i)
      print(sum)

#Non Repeating character in string
s=("Independance")
t=[]
for i in s:
   if s.count(i)<2:
      t.append(i)
      print(t)

#Copying String
St1="Hello World"
St2=""
for i in St1:
   St2=St2+i
print("The final string:St2=",St2)

 

      
 
