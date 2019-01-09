# Print next Prime number with limit defined by user.


def prime_number(n):

    for i in range(2, n+1):
        counter = 0

        for j in range(1, i+1):

            if i % j == 0:
                counter += 1

        if counter == 2:
            if i == 2:
                print(i)
                continue
            while True:
                next = input("Do you want next Prime Number? (y/n)")
                if next.lower() == "y":
                    print(i)
                    break
                elif next.lower() == "n":
                    return "Good Bye"
                else:
                    print("Please answer y for yes or n for no.")



n = int(input("What is the limit of prime numbers?"))
print(prime_number(n))

