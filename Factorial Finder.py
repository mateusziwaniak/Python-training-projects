# Factorial finder using both loops

# for loop
def factorial_for(n):

    if n == 0:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i

        return result
# while loop
def factorial_while(n):

    result = 1
    if n == 0:
        return 1
    else:
        i = 1
        while i < n+1:
            result *= i
            i += 1
        return result


n = int(input())

print(factorial_while(n))

