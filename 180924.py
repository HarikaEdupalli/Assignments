#Create a Guessing Game by using of Python
import random
print("Welcome to the Guessing Game")
print("Try guess the numbet in between 1 to 100")
number=random.randint(1,100)
guess=-1
if guess!=number:
    guess_num=input("Enter your Number")
    guess=int(guess_num)
    if guess<number:
        print("Too low,Try Again")
    elif guess>number:
        print("Too high,Try Again")
    else:
        print("Congratulations! You Guessed the number correctly!")    

#Adding an item to Dmart shopping bill

def function(dict_in,dict_price):
    n=int(input())
    for i in range(n):
        function_1(dict_in)
    count=0
    for i,j in dict_in.items():
        for a,b in dict_price.items():
            if i==a:
                count+=int(j)*int(b)
    return count
def function_1(dict_in):
    dict_in[input()]=input()


dict_in=eval(input())
dict_price=eval(input())
a=function(dict_in,dict_price)
print(a)
