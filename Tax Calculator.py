# Tax Calculator


def tax_calc(tax, cost):

    return cost * tax


tax = float(input("Please enter tax rate in % format: "))
tax = tax * 0.01
cost = float(input("Please enter the cost of your item: "))

tax_to_pay = tax_calc(tax, cost)

print(f"Your total cost is ${cost + tax_to_pay} and the tax is ${round(tax_to_pay, 2)}")
