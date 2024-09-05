#Adding a Key to a dictionary
d={'Name':'Harika','ID':1234}
a={'Language':'Python'}
d.update(a)
print(d)
#Finding the value existing or not in dict
dict={'a':10,'b':20,'c':30}
if dict.get('d') is not None:
    print("Value is exist")
else:
    print("Value is not exist")
#Script to print a dict keys b/w 1-15 and values are squares of keys
dict={}
for i in range(1,16):
   dict[i]=i**2
print(dict)
# To create a dictionary from string
st=input("Enter a String:")
dict={}
for ch in st:
    if ch in dict:
        dict[ch]+=1
    else:
        dict[ch]=1
print(dict)
#Combining Two dictionaries by common keys
dict1={'a':1,'b':2,'c':3,'d':4}
dict2={'key1':100,'key2':300,'c':500,'key3':600}
for key in dict2:
    if key in dict1:
        dict2[key]=dict2[key]+dict1[key]
    else:
        pass
print(dict2)
#Merging two dictionaries
d1={1:'a',2:'b',3:'c',4:'d'}
d2={6:'a',7:'g',8:'h',9:'l'}
print(d1|d2)
# Sorting keys and Values
dict={'key1':100,'key2':300,'c':500,'key3':600}
print(dict.keys())
print(dict.values())
#Dictionary from string
st=input("Enter a String:")
dic={}
for ch in st:
    if ch in dic:
        dic[ch]+=1
    else:
        dic[ch]=1
print(dic)



