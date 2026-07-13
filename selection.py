score = int(input("Enter score: "))

if score >= 50:
    print("Pass")
else:
    print("Fail")


num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest:", a)
elif b > c:
    print("Largest:", b)
else:
    print("Largest:", c)


    