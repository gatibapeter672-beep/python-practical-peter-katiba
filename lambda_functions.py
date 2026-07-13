add = lambda a, b: a + b
print(add(2, 3))


mul = lambda a, b: a * b
print(mul(3, 4))

numbers = [5, 2, 8, 1]
print(sorted(numbers, key=lambda x: x))


nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)


squares = list(map(lambda x: x**2, nums))
print(squares)