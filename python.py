print("My name is Ahmad")



'''This is a comment
written in
more than just one line'''

#Two types work in market: Product based, Preoject based
#casting
# outside function variable is Global variable , use anywhere in any function
#inside function, variables are local, not use in another function
x=int(input("Enter a number:"))
def my_function ():
    y=7
    x=5
    return x+y
value = my_function()
print(value)

def add():
    y= 8
    return x+y
c= add()
print(c)

marks = int(input("Enter the marks:"))
if marks >= 85:
    print("Grade A")

else:
    print("F Grade")

gpa = float(input("Enter the GPA:"))
iq = float (input("Enter the iq level"))
if gpa>=3.5 and iq>=80:
    print("Yes, you get job")
else: 
    print("You fail.")
    

########LOOPS IN PYTHON 
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Square of {num} is {num**2}")



count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1  # Decrease count
print("Blast Off! 🚀")


numbers = [1, 3, 5, 8, 9, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break  # Stop loop after first even number
    
    
for i in range(1, 10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)


for i in range(1, 4):  # Rows (1 to 3)
    for j in range(1, 11):  # Columns (1 to 10)
        print(f"{i} * {j} = {i*j}")
    print("-" * 15)  # Separator


    
##########PYTHON OOP (OBJECT ORIENTED PROGRAMMING)

class Car:  
    def __init__(self, brand, color):  
        self.brand = brand  # Attribute
        self.color = color  # Attribute
    
    def show_info(self):  # Method
        print(f"This car is a {self.color} {self.brand}.")
        
# Creating objects
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

car1.show_info()  # Output: This car is a Red Toyota.
car2.show_info()  # Output: This car is a Blue Honda.


#ENCAPSULATION
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):  # Getter method
        return self.__balance

# Creating object
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # ❌ This will give an error



#INHERITANCE
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):  # Inheriting from Animal
    def speak(self):  
        return "Woof! Woof!"

dog = Dog()
print(dog.speak())  # Output: Woof! Woof!


#POLYMORPHISM
class Bird:
    def fly(self):
        return "Some birds can fly."

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high!"

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly!"

# Using polymorphism
birds = [Sparrow(), Penguin()]
for bird in birds:
    print(bird.fly())

# Output:
# Sparrow flies high!
# Penguins cannot fly!





