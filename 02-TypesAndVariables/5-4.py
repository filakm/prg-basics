amount_str = input('Input your amount to calculate its VAT(23%): ')
amount = float(amount_str)
vat = round(amount*0.23,2)
print(f'Your VAT(23%) for {amount} is: {vat}')