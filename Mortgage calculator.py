# Mortgage calculator in yearly time



def yearly_pay(commission, year_percent, n, amount):

    year_list = []
    amount_left = amount + amount * commission
    years_left = n
    for i in range(1, n+1):
        pay = amount_left / years_left
        percent = amount_left * year_percent

        year_list.append(round((pay + percent), 2))
        years_left -= 1
        amount_left -= pay

    return year_list



def total_pay(list):
    summary = 0
    for i in range(len(list)):
        summary = summary + (list[i])

    return f"\nYour total pay for this mortgage is: $ {round(summary)}"



amount = int(input("How many $ do you need?: "))
n = int(input("How many years you want to pay?: "))

commission = 0.035     # Commission 3,5%
year_percent = 0.0326  # Yearly percent 2,82

year_list = yearly_pay(commission, year_percent, n, amount)
print(total_pay(year_list))
i = 1
for pay in yearly_pay(commission, year_percent, n, amount):
    print(f"Year {i}: $ {pay}")
    i += 1


