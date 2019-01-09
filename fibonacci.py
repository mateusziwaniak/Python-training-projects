# Print Fibonaci numbers to Nth

def fibonacci(n):

    list = [0, 1]
    for i in range(2, n):
        list.append(list[i-1] + list[i-2])

    for i in range(n):
        list[i] = str(list[i])

    return  " - ".join(list)

n = int(input("Write how many numbers you want."))
print(fibonacci(n))