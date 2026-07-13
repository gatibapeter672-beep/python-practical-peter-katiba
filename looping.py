for i in range(1, 21):
    print(i)


num = int(input("Enter number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print("Sum:", sum)


for i in range(1, 51):
    if i % 2 == 0:
        print(i)

    