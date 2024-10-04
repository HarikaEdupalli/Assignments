#Single inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Animal Sound")
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        print("Bark") 
dog=Dog("Tan")
dog.speak()    

#Multiple Inheritance
class Teacher:
    def __init__(self,subject):
        self.subject=subject
    def display_teacher_info(self):
        print("Subject:",{self.subject})
class Researcher:
    def __init__(self,field):
        self.field=field
    def display_Researcher_info(self):
        print("Field:",{self.field})
class TeacherResearcher(Teacher,Researcher):
    def __init__(self,subject,field):
        Teacher.__init__(self,subject)
        Researcher.__init__(self,field)
    def dispaly_info(self):
        print("Teacher-Researcher information")
        self.display_teacher_info()
        self.display_Researcher_info()
tr=TeacherResearcher("Mathematics","Artificial Intelligence")
tr.dispaly_info()
#2
class Bird:
    def __init__(self,species):
        self.species=species
    def display_species(self):
        print("Species:",{self.species})
class Flyable:
    def fly(self):
        print("Flying")
class Eagle(Bird,Flyable):
    def __init__(self,species):
        super().__init__(species)
    def display_eagle_info(self):
        self.display_species()
        self.fly()
eagle=Eagle("Bald Eagle")
eagle.display_eagle_info()

#Multilevel Inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person_info(self):
        print("Name:",{self.name})
        print("age:",{self.age})
class Employee(Person):
    def __init__(self,name,age,salary):
        super(). __init__(name,age)
        self.salary=salary
    def display_employee_info(self):
        self.display_person_info()
        print("Salary:",{self.salary})
class Manager(Employee):
    def __init__(self,name,age,salary,department):
        super(). __init__(name,age,salary)
        self.department=department
    def display_manager_info(self):
        self.display_employee_info()
        print("Department:",{self.department})
manager=Manager("Ram",26,100000,"Marketing")
manager.display_manager_info()

#Heirarchical Inheritance
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_employee_info(self):
        print("Name:",{self.name})
        print("Salary:",{self.salary})
class Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language
    def display_developer_info(self):
        self.display_employee_info()
        print("Programming Language:",{self.programming_language})
class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super(). __init__(name,salary)
        self.team_size=team_size
    def display_manager_info(self):
        self.display_employee_info()
        print("Team Size:",{self.team_size})
class Intern(Developer):
    def __init__(self,name,salary,programming_language,internship_duration):
        super(). __init__(name,salary,programming_language)
        self.internship_duration=internship_duration
    def display_intern_info(self):
        self.display_developer_info()
        print("Internship Duration:", {self.internship_duration})
developer=Developer("Hari",50000,"Python")
manager=Manager("Ram",75000,10)
intern=Intern("Sai",60000,"Java",6)
print("Developer Information:")
developer.display_developer_info()
print("Manager Information:")
manager.display_manager_info()
print("Intern Information:")
intern.display_intern_info()

#2
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_vehicle_info(self):
        print("Brand:",{self.brand})
        print("Model:",{self.model})
class Car(Vehicle):
    def __init__(self,brand,model,num_doors):
        super(). __init__(brand,model)
        self.num_doors=num_doors
    def display_car_info(self):
        self.display_vehicle_info()
        print("Number of doors:",{self.num_doors})
class Bike(Vehicle):
    def __init__(self,brand,model,type):
        super(). __init__(brand,model)
        self.type=type
    def display_bike_info(self):
        self.display_vehicle_info()
        print("Type:",{self.type})
car=Car("Toyoto","Camry",4)
bike=Bike("Honda","CBR500R","Sport")
print("Car Information:")
car.display_car_info()
print("Bike Information:")
bike.display_bike_info()

#Hybrid Inheritance
class Device:
    def __init__(self,name):
        self.name=name
    def display_device_info(self):
        print("Name:",{self.name})
class Phone(Device):
    def __init__(self,name,phone_number):
        super(). __init__(name,phone_number)
        self.phone_number=phone_number
    def display_phone_info(self):
        self.display_device_info()
        print("Phone Number:",{self.phone_number})
class Tablet(Device):
     def __init__(self,name,screen_size):
        super(). __init__(name)
        self.screen_size=screen_size

     def display_tablet_info(self):
        self.display_device_info()
        print("screen_size:",{self.screen_size})
class SmartPhone(Phone, Tablet):
    def __init__(self,name,phone_number,screen_size,os):
        Phone. __init__(self,name,phone_number)
        Tablet. __init__(self,name,screen_size)
        self.os=os
    def display_smartphone_info(self):
        print("Smartphone Information:")
        self.display_phone_info()
        print(f"screen_Size:{self.screen_size} inches")
        print(f"Operating System:{self.os}")
smartphone=SmartPhone("iphone14","123-456-7890",16,"iOS16")
smartphone.display_smartphone_info()

#Basic Inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print("Personal Information:")
        print("Name:",{self.name})
        print("Age:",{self.age})
class Student(Person):
    def __init__(self,name,age,grade):
        super(). __init__(name,age)
        self.grade=grade
    def display_info(self):
        super(). display_info()
        print("Grade:",{self.grade})
person=Person("Ram",23)
student=Student("Hari",24,"A+")
person.display_info()
print()
student.display_info()













        
        







        