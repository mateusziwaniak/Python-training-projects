# Happy numbers.


# Function to get number from user(optional).
def get_number():
    while True:
        try:
            n = int(input("Please give a positive integer: "))
            if n > 0:
                return n
            else:
                print("\n\nThat's, not positive integer number, please try again.")
        except TypeError:
            print("\n\nThat's, not positive integer number, please try again.")


# Function to square n
def n_to_power(n):
    n = str(n)
    result = 0
    for i in range(len(n)):
        result += int(n[i]) ** 2
    return result


# Function to check if number is never ends. - Don't need it.
"""
def never_ends(number, list):

    if number in list:
        return False
    else:
        list.append(number)
"""


# Function to check if number is Happy number. If no it means it's never ends.
def check_number(number):
    exist_list = []
    i = 1
    while True:

        if number == 1:
            print(f"{num} is a Happy Number and I found it in {i} iteration")
            return True
        elif number in exist_list:
            return False
        else:
            exist_list.append(number)
            number = n_to_power(number)
        i += 1


counter = 1
num = 1

while counter < 8:

    if check_number(n_to_power(num)) is True:
        counter += 1
    else:
        print(f"{num} is never ending story...")
    print()
    num += 1
