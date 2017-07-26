from core import rental_products, remove_stock

def main():
    print('Welcome to Shedlia\'s Atv and Side-By-Side Rental Agency')
    # give the user choices through numbers So it can be easier to choose what you want
    decision = input(''' What would you like:
    \t1. Atvs
    \t2. Side-by-Sides
    \t3. Both
    :''').strip()
    #user chooses through numbers what they want
    #if they choose the number 1 they get an atv in stock
    if decision == '1':
        rent_atv()
    elif decision == '2':
        rent_sbs()
    elif decision == '3':
        rent_both()

def rent_atv():
    #the variable 'how many' is used to see how many of the products the customer wants
    product_name = 'Atv'.strip()
    how_many = int(input('how many Atv\'s would you like?\n:'))
    sales_tax = .07 * how_many
    price = (rental_products[product_name]['price'] * how_many)
    total = price + sales_tax
    remove_stock(how_many,product_name,rental_products)
    print(rental_products)
    print('$:',total)
    
#if they choose the number 2 they get a side-by-side
#sbs stands for side-by-side
def rent_sbs():
    product_name = 'Side-by-Side'.strip()
    how_many = int(input('how many Side-by-Side\'s would you like?\n:'))
    # rental_products['Side-by-Side']['stock'] -= how_many
    remove_stock(how_many, product_name, rental_products)
    print(rental_products)
    
#if they choose the number 3 they get both an atv and side-by-side
def rent_both():
    rent_atv()

    rent_sbs()

if __name__ == '__main__':
    main()

