#1
class Person:
    def __init__(self,name,age,gender):
# Initializes a Person Object
       self.name=name
       self.age=age
       self.gender=gender
    def update_age(self,new_age):
        self.age=new_age
    def display_info(self):
#Display person's information.
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
#Creating multiple instances of the person class
person1=Person("Hari",30,"Male")
person2=Person("Ram",25,"Male")
person3=Person("Sri",36,"Female")
#Display intial information
print("initial information:")
print("Person1:")
person1.display_info()
print("\nPerson2:")
person2.display_info()
print("\nPerson3:")
person3.display_info()
#Change the age of one person and display the updated information
person2.update_age(26)
print("\nUpdated information:")
print("person2:")
person2.display_info()


#2
class Company:
    total_employees=0 #Static variable to track total employees
    def __init__(self,name,department):
        self.name=name
        self.department=department
        Company.total_employees +=1 #Increment total_employees on each new employee
    def display_info(self):
        print("Name:",{self.name})
        print("Department:",{self.department})
    @classmethod
    def get_total_employees(cls):
        return cls.total_employees
# Create multiple employee instances
emp1=Company("Hari","Marketing")
print("Total Employees:",Company.get_total_employees())
emp2=Company("Hari","HR")
print("Total Employees:",Company.get_total_employees())
emp3=Company("Ram","IT")
print("Total Employees:",Company.get_total_employees())
# Check if changing total_employees in one instance affects other
emp1.total_employees=100 #Attempts to change total_employees
print("Emp1 Total Employees:",emp1.total_employees)
print("Emp2 Total Employees:",Company.get_total_employees())
#Dispaly employee information
print("Employee Information:")
emp1.display_info()
print()
emp2.display_info()
print()
emp3.display_info()

#3
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        area_length=self.length
        area_width=self.width
        area=area_length*area_width
        print(f"Rectangle Area:{area}square units")
      #creates instances of the rectangle class
rect1=Rectangle(5,3)
rect2=Rectangle(8,4)
rect3=Rectangle(10,2)
       #Calculate and print area of each rectangle
print("Rectangle 1(5*3):")
rect1.calculate_area()
print("Rectangle 2(8*4):")
rect2.calculate_area()
print("Rectangle 3(10*2):")
rect3.calculate_area()

#4
class Employee:
    bonus=0.1 #static variable for bonus(10%)
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def total_salary(self):
        return self.salary+(self.salary*Employee.bonus)   #calculates the total salary including bonus.
#create employee instances with different salaries
emp1=Employee("Har",50000)
emp2=Employee("Ram",60000)
emp3=Employee("Sai",70000)
#print initial total salary
print("Initial Total Salaries:")
print(f"{emp1.name}:${emp1.total_salary():.2f}")
print(f"{emp2.name}:${emp2.total_salary():.2f}")
print(f"{emp3.name}:${emp3.total_salary():.2f}")
Employee.bonus=0.15 #change the bonus amount to 15%(Static Variable)
#print updated total salaries
print("\nUpdate Total Salaries(15% bonus):")
print(f"{emp1.name}:${emp1.total_salary():.2f}")
print(f"{emp2.name}:${emp2.total_salary():.2f}")
print(f"{emp3.name}:${emp3.total_salary():.2f}")

      













       

          

