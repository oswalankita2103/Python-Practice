#__________________________________INT DATATYPE________________________________________
age = 22
print(age)
print(type(age))
#__________________________________FLOAT DATATYPE________________________________________
price = 99.50
print(price)
print(type(price))
#__________________________________STRING DATATYPE________________________________________
name = "Ankita"
print(name)
print(type(name))
#__________________________________BOOLEAN DATATYPE________________________________________
is_student = True
print(is_student)
print(type(is_student))
#__________________________________COMPLEX DATATYPE________________________________________
num = 3 + 5j
print(num)
print(type(num))
print(num.real)
print(num.imag)
#__________________________________LIST DATATYPE________________________________________
numbers = [10, 20, 30, 40]

numbers[0] = 100

print(numbers)
print(type(numbers))
#__________________________________TUPLE DATATYPE________________________________________
colors = ("Red", "Green", "Blue")

print(colors)
print(type(colors))
print(colors[0])
#__________________________________RANGE DATATYPE________________________________________
numbers = range(1, 6)

print(list(numbers))
print(type(numbers))
#__________________________________DICTIONARY DATATYPE________________________________________
student = {
    "name": "Ankita",
    "age": 22,
    "marks": 85
}

print(student)
print(type(student))
print(student["name"])
#__________________________________SET DATATYPE________________________________________
numbers = {10, 20, 20, 30, 40}

print(numbers)
print(type(numbers))
#__________________________________FROZEN SET DATATYPE________________________________________
numbers = frozenset([10, 20, 30, 30])

print(numbers)
print(type(numbers))