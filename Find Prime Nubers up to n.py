# Find all prime numbers up to n - number given by user


# make a list up to n numbers.
def make_list(n):
    to_n_list = []
    for i in range(2, n+1):
        to_n_list.append(i)

    return to_n_list


# take a full list and return list with only prime numbers
def give_primes(n):
    result = []
    for i in range(len(n)):
        if n[i] == 0:
            continue
        else:
            result.append(n[i])
            divider = n[i]
            for j in range(i, len(n), divider):
                n[j] = 0

    result2 = []
    for i in result:
        if i != 0:
            result2.append(i)

    return result2


number = int(input("Please give me number up to you want get all prime numbers: "))
x = make_list(number)
primes = give_primes(x)

print(f"This is the list of prime numbers up to {number}: {primes}")
print(f"Total numeber of prime numbers up to {number} is {len(primes)}")  # Print how many prime numbers you get up to n number.
