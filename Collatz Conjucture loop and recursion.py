# Collatz Conjectire

# Loop solution.
def process(x):
    counter = 0

    while x != 1:
        counter += 1

        if x % 2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1

        print(x)

    return counter

# Recursion solution.
def hailstone(n):
    print(n)
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    hailstone(n)


n = int(input("Write the number to start process: "))

print(f"To reach 1 from {n} takes {process(n)} steps\n")

hailstone(n)


