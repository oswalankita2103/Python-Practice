num = int(input("Enter any number"))
origanalNum = num
rev=0
while num > 0:
    rem = num%10
    rev = rev*10+rem
    num = num//10

if origanalNum == rev:
    print("palindrom")
else:
    print("not palindrom")