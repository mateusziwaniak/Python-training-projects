# Binary to Decimal number calculator / Decimal to Binary

def bin_to_dec(number):

    decimal = 0
    number = str(number)
    number = number[::-1]

    for i in range(0, len(number)):
        if number[i] == "1":
            decimal += 2 ** i
            i += 1

        else:
            i += 1
            continue

    return decimal


def dec_to_bin(dec_number):

    bin = ""
    while dec_number > 0:

        if dec_number % 2 == 0:
            bin += "0"
        elif dec_number % 2 == 1:
            bin += "1"
        dec_number = dec_number // 2

    return bin



bin_number = dec_to_bin(1023)
bin_number = bin_number[::-1]

print(bin_to_dec(1111111111))
print(bin_number)