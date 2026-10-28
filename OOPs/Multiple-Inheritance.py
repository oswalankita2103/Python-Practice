class Father():
    def show(self):
        print("father class")

class Mother():
    def display(self):
        print("mother class")

class Child(Father,Mother):
    def info(self):
        print("child class") 

f = Father()
m = Mother()
c = Child()

f.show()
m.display()
c.show()
c.display()
c.info()