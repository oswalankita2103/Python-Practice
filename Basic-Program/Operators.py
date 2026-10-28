#1______________________________________Arithmetic operators_____________________________
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
#2______________________________________Comparison operators_____________________________
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True
#3______________________________________Assignment operators_____________________________
x = 10

x += 5
print(x)  # 15

x *= 2
print(x)  # 30

x -= 10
print(x)  # 20
#4______________________________________Logical operators_____________________________
age = 22
has_id = True

print(age >= 18 and has_id)  # True
print(age < 18 or has_id)    # True
print(not has_id)            # False
#5______________________________________Bitwise operators_____________________________
a = 5   # Binary: 0101
b = 3   # Binary: 0011

print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(~a)      # -6
print(a << 1)  # 10
print(a >> 1)  # 2
#6______________________________________Membership Operators_____________________________
numbers = [10, 20, 30, 40]

print(20 in numbers)      # True
print(50 in numbers)      # False
print(50 not in numbers)  # True
#7______________________________________Identity Operators_____________________________
a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)      # True
print(a is c)      # False
print(a == c)      # True
print(a is not c)  # True

