# A  computer program analyses the price of a product in an online store. If the product price decreases by at least 10%, the program prints a purchase recommendation:

## Buy the product!!
# Product price reduced by 17%
##  Create such program. The current and previous price of the product are included in variables. Sample result:

# Current product price: 140.00
# Previous product price: 200.00
# Buy the product!!
# Product price reduced by 30%

pre_price = 200
curr_price = 100

# formula
diff = int(pre_price-curr_price)
discount = int(diff/pre_price/0.01)

if discount >= 10:
    print ("Buy the product!!")
    print (f"Product prize reduced by {discount}%.")
else:
    print(f"Price: {pre_price} ")
    print(f'Discount: {discount}%')