# Polymorphism using method overloanding
class Dog:
    def sound(self):
        print("dog barks")
class Cat:
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.sound()        
c.sound()