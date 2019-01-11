


def checksum(account_number):

    account_number = account_number[::-1]
    sum_odd = 0
    sum_even = 0

    for i in range (0, len(account_number), 2):
        sum_odd += int(account_number[i])

    for i in range (1, len(account_number), 2):
        if (int(account_number[i]) * 2) > 9:
            temp = int(account_number[i]) * 2
            temp = str(temp)
            sum_even += int(temp[0]) + int(temp[1])
        else:
            sum_even += int(account_number[i]) * 2
    sum = sum_even + sum_odd

    if sum % 10 == 0:
        return True
    else:
        return False



account_number = "5396037621418097"
print(f"Your card number is: {account_number}\n")

validation = checksum(account_number)
if validation and len(account_number) == 16:
    print("Your card is valid!")
else:
    print("Your card is not valid!")






