#Polymorphism using Inheritance 
class Animal:
    def sound(self):
        print("Animal make a sound")
class Dog(Animal):
    def sound(self):
       print("dog barks")
class Cat(Animal):
    def sound(self):
         print("Cat meows")

animal = [Dog(),Cat(),Animal()]
for a in animal:
    a.sound()