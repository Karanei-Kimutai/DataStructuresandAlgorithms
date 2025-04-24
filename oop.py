#There are 4 key OOP concepts: Encapsulation, Abstraction, Inheritance and Polymorphism
#Encapsulation: Bundling data(attributes) and methods(functions) that work on the data into a single unit-a class
#Encapsulation also involves restricting direct access to data using access modifiers
class Person:
   def __init__(self,name:str,ID:int,age:int): #constructor
       self.name=name   #public attribute
       self.__ID=ID     #private attribute
       self._age=age    #protected attribute

   def getid(self):
       return self.__ID
   def getage(self):
       return self._age

   def showdetails(self):
       print(f"Name: {self.name} \nID:{self.getid()}\nAge:{self.getage()}")


newperson=Person("Karanei",216353803,18)
newperson.showdetails()

#Abstraction- hiding the complex implementation details and exposing only the necessary parts
#Abstraction is done using abstract base classes from the abc module

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def makesound(self):
        pass                #No implementation details given(Abstraction)

class Dog(Animal):
    def makesound(self):
        print("Woof!")
germanSheperd=Dog()
germanSheperd.makesound()

#Inheritance-this is when a class borrows attributes and methods from an already existing class
#polymorphism-this is when a subclass modifies an inherited method
class Student(Person):      #Inheritance-similar to 'Student extends Person' in Java
    def __init__(self,name,ID,age,studentID):
        super().__init__(name,ID,age) #calls the parent constructor
        self.studentID=studentID

    def showdetails(self):    #Polymorphism-we modify the inherited showdetails() function
        super().showdetails()   #Calls the parent version of showdetails()
        print(f"StudentID:{self.studentID}")

student1=Student("Karanei",216353803,18,183523)
student1.showdetails()


#'self'-refers to the instance of the class itself, it allows you to access attributes and methods within the class definition
#python uses the 'self' keyword to distinguish between instance variables and local variables
#'self' is explicitly passed as the first parameter in instance methods

#the super() method is used to access inherited attributes and methods-similar to the super keyword in Java






#Class example
class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_item(self,item_name,quantity):
        item=(item_name,quantity)
        self.items.append()

    def remove_item(self,item_name):
        for item in self.items:
            if item[0]==item_name:
                self.items.remove(item)
                break

    def calculate_total_items(self):
        total=0
        for item in self.items:
            total+=1
        return total

Cart1=ShoppingCart()
Cart1.add_item("Apple",1)
Cart1.add_item("Ground beef",5)
Cart1.add_item("Banana",7)

print("Current items in cart")
for item in Cart1.items:
    print(item[0]+"-"+item[1])

