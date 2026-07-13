def add(a, b):
    return a + b


def area(length, width):
    return length * width

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def display(name, course):
    print("Name:", name)
    print("Course:", course)

# Testing
print(add(2, 3))
print(area(5, 4))
print(is_prime(7))
print(factorial(5))
display("Peter", "CS")