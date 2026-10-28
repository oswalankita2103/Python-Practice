class GrandParant():
    def show(self):
        print("grandparent class")

class Parent(GrandParant):
    def display(self):
        print("parent class")

class Child(Parent):
    def info(self):
        print("child class")

#create object of all classes
g = GrandParant()
p = Parent()
c = Child() 

# grandparent class menthod calling
g.show()

# parent class menthod calling
p.show()
p.display()
# chid class menthod calling
c.show()
c.display()
c.info()