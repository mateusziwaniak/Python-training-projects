# Collatz Conjectire


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


n = int(input("Write the number to start process: "))

print(f"To reach 1 from {n} takes {process(n)} steps")
