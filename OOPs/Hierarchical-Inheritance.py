class Parent():
    def show(self):
        print("parent class")

class Child1(Parent):
    def display(self):
      print("child1 class")

class Child2(Parent):
    def info(self):
      print("child2 class")

p = Parent()
c1 = Child1()
c2 = Child2()

p.show()
c1.show()
c1.display()
c2.show()
c2.info()