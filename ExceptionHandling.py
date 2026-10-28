try:
    a = int(input("Enter any number"))
    print(10/a)
except ZeroDivisionError:
    print("error")
except ValueError:
    print("invalid number")