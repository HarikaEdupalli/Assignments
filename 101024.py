#1
class Vehicle:
    def __init__(self,Brand,Year):
        self.Brand=Brand
        self.Year=Year
    def get_info(self):
        return f"{self.Brand},{self.Year}"
class Car(Vehicle):
    def __init__(self,Brand,Year,Number_of_doors):
        super().__init__(Brand,Year)
        self.Number_of_doors=Number_of_doors
    def get_info(self):
        return f"{super().get_info()},{self.Number_of_doors}"
class Motorcycle(Vehicle):
    def __init__(self,Brand,Year,has_side_car):
        super().__init__(Brand,Year)
        self.has_side_car=has_side_car
    def get_info(self):
        side_car_info="with side car" if self.has_side_car else "with out side car"
        return f"{super().get_info()},{side_car_info}"
car=Car("Toyoto",2022,4)
motorcycle=Motorcycle("Honda",2021,False)
print(car.get_info())
print(motorcycle.get_info())

#2
class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Woof")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
class Cow(Animal):
    def make_sound(self):
        print("Moo")
def play_sound(animal:Animal):
    animal.make_sound()
dog=Dog()
cat=Cat()
cow=Cow()
play_sound(dog)
play_sound(cat)
play_sound(cow)

#3
class BankAccount:  #Abstract class
    def __init__(self,account_number,initial_balance):
        self.account_number=account_number
        self.balance=initial_balance
    def deposite(self,amount): # Abstract method
        self.balance+=amount
        print(f"Deposited ${amount}into account{self.account_number}.New balance:${self.balance}")
    def get_balance(self):
        print(f"Account{self.account_number}balance:${self.balance}")
    def withdraw(self,amount):
        raise                 # by using of raise keyword Not implemented error to indicate abstract methods.
class SavingsAccount(BankAccount):
    def withdraw(self,amount): #Abstract method
        if self.balance-amount<500:
            print("Savings account balance coonnot go below $500")
        else:
            self.balance-=amount
            print(f"withdraw ${amount}from account{self.account_number}.New balance:${self.balance}")
class CurrentAccount(BankAccount):
    def withdraw(self,amount):
        if self.balance-amount<-1000: # withdraw() method allows balance to go negative(upto $1000 overdraft)
            print("Current account overdraft llimit is $1000")
        else:
            self.balance-=amount
            print(f" withdraw ${amount}from account{self.account_number}.New balance:${self.balance}")
savings_account=SavingsAccount("sav123",1000)
current_account=CurrentAccount("cur457",500)
savings_account.deposite(500)
savings_account.withdraw(800) # Balance cannot go below $500
current_account.deposite(1000)
current_account.withdraw(1500) #overdraft allowed upto $1000
current_account.withdraw(2000) # withdraw limit exceeds

#4
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_details(self):
        return (f"Name:{self.name},Salary:${self.salary}")
    def get_salary(self):
        return self.salary
    def increase_salary(self,percentage):
            self.salary+=(self.salary*percentage/100)
            return self.salary
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def get_details(self):
        return(f"{super().get_details()},Department:{self.department}")
class Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language
    def get_details(self):
        return(f"{super().get_details()},Programming_language:{self.programming_language}")
manager=Manager("Ram",80000,"HR") # Creating Instances
developer=Developer("Sai",50000,"Python")
print(manager.get_details())  #Getting employee detaills
print(developer.get_details())
print(f"Manager salary after 10% increase:${manager.increase_salary(10)}")    #Increase salary
print(f"Developer salary after 15% increase:${developer.increase_salary(15)}")

#5
class LibraryItem():
    def borrow(self):
        pass
    def return_item(self):
        pass
class Book(LibraryItem):
    def __init__(self,title,author,num_copies):
        self.title=title
        self.author=author
        self.num_copies=num_copies
        self.borrowed=False
    def borrow(self):
        if self.num_copies>0 and not self.borrowed:
            self.num_copies-=1
            self.borrowed=True
            print(f"Borrow book:{self.title}by {self.author},{self.num_copies}")
        else:
            print(f"Book unavailable:{self.title}by{self.author},{self.num_copies}")
    def return_item(self):
        if self.borrowed:
            self.num_copies+=1
            self.borrowed=False
            print(f"Returned book:{self.title}by{self.author},{self.num_copies}")
        else:
            print(f"Book already available:{self.title}by{self.author},{self.num_copies}")
class DVD(LibraryItem):
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        self.borrowed=False
    def borrow(self):
        if not self.borrowed:
            self.borrowed=True
            print(f"Borrow DVD:{self.title} by {self.director},{self.duration}")
        else:
            print(f"DVD already borrowed:{self.title} by {self.director},{self.duration}")
    def return_item(self):
        if self.borrowed:
            self.borrowed=False
            print(f"Returned DVD:{self.title} by {self.director},{self.duration}")
        else:
            print(f"DVD already available:{self.title}  by {self.director},{self.duration,}")
def borrow_item(item:LibraryItem): #Function borrrow_item()
        item.borrow()
def return_item(item:LibraryItem):  #Function return_item()
        item.return_item()
book=Book("Harry Potter","J.K. Rowling",5)   #Create Instances
dvd=DVD("Spider-Man","sam Raimi","1321 mins")
borrow_item(book)  #Borrow and return items
borrow_item(dvd)
return_item(book)
return_item(dvd)

#6
class Media:
    def play(self):
        pass
class Audio(Media):
    def __init__(self,file_name):
        self.file_name=file_name
    def play(self):
        print(f"Playing audio:{self.file_name}.mp3")
class Video(Media):
    def __init__(self,file_name):
        self.file_name=file_name
        print(f"Playing video:{self.file_name}.mp4")
class Livestream(Media):
    def __init__(self,stream_name):
        self.stream_name=stream_name
    def play(self):
        print(f"Playing livestream:{self.stream_name}.link Available")
def start_media(media:Media):  #Function start_media()
    media.play()
audio=Audio("Song")
video=Video("Movie")
livestream=Livestream("live_stream")
start_media(audio)
start_media(video)
start_media(livestream)











    


