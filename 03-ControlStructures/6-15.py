# EAN-13 (European Article Number) is a barcode for marking goods. 
# The first 3 digits (590) usually indicate goods manufactured in Poland. 
# Write a program that checks whether the EAN-13 number entered from the keyboard consists of exactly 13 characters (digits). 
# Print a message if the number is correct. Additionally, only when the article number is correct, print a message when the product was manufactured in Poland.
#  Sample result:

# Enter EAN-13 article number: 5901230094938
# Article number is correct
# Article manufactured in Poland

number = input('Enter EAN-13 articale number: ')

if len(number) == 13: 
    if number.isdigit():
        print('Article number is correct')
        if number.startswith("590"):
                print('article was manufactured in Poland')
    else:
        print('incorrect only digits')
else:
     print('code can only be 13 characters')