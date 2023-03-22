
print('How many years will you be saving?')
years = int(input('Enter years: '))

print('How much money is currenlt in your account?')
principal = float(input('Enter current amount in account: '))

print('How much money do you plan on investing monthly?')
monthly_invest = float(input('Enter amount: '))

print('Waht do you estimate will be the yearly intrest of the investment?')
interst = float(input('Enter interest in decimal number (10% = 0.1): '))

print(' ')

monthly_invest = monthly_invest * 12
final_amount = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = principal

    final_amount = (final_amount + monthly_invest) * (1 + interst)

print('This is how much money you would have in your acoount after {} years: '
      .format(years) + str(final_amount))
