# Fizz Buzz


def three_mult(n):
    return n % 3 == 0


def five_mult(n):
    return n % 5 == 0


for i in range(1, 101):
    if three_mult(i) and five_mult(i):
        print("FizzBuzz")
    elif three_mult(i):
        print("Fizz")
    elif five_mult(i):
        print("Buzz")
    else:
        print(i)
