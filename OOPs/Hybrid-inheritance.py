class A:                          #parent claa 
    def show(self):
        print("Class A ")
class B(A):                       #class B inherit class A properties
    def display(self):
        print("Class B ")
class C(A):                       #class C inherit class A properties
    def info(self):
        print("Class C ")
class D(B,C):                     #class D inherit class B and class C properties 
    def result(self):
        print("Class D ")

d = D()
d.show()
d.display()
d.info()
d.result()
