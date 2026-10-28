class Calculator:
    def add(self,a,b=0,c=0):
        return a+b+c;

cal = Calculator()
print(cal.add(10,30))
print(cal.add(10,50,60))
print(cal.add(20))