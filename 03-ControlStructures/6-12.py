#In one of the online stores, a 25% discount is charged for each product purchased over two. 
# Write a program that calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard. Sample result:

#Number of products purchased: 5
#Product price: 40
#Amount to pay: 170.00

num_of_prod = int(input('Number of products: '))
prod_price = int(input('product prize: '))

if num_of_prod >= 3:
    discount = prod_price-0.25*prod_price
    prod_price_1 = 2*prod_price+(num_of_prod-2)*discount
    print(f'number of product: {num_of_prod}')
    print(f'product price: {prod_price}')
    print(f'Amount to pay: {prod_price_1}')