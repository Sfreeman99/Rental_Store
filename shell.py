from core import *
from disk import *
def main():
    print('Welcome to Shedlia\'s Atv and Side-By-Side Rental Agency')
    # give the user choices through numbers So it can be easier to choose what you want
    decision = input(''' What would you like:
    \t1. Rent
    \t2. Return
    :''').strip()
    #user chooses through numbers what they want
    #if they choose the number 1 they get an atv in stock
    if decision == '1':
        rent()
    elif decision == '2':
        return_item()

def rent():
    #the variable 'how many' is used to see how many of the products the customer wants
    category = input('What do you want to rent:\n\t1. Atv\n\t2. Side-by-Side\n\t3. Scooter\n\t4. Bike\n:')
    rental_products = read_inventory()
    if category == '1':
        product_name = 'Atv'.strip()
        
        how_many = int(input('how many Atvs would you like?\n:'))
    
        new_inventory = remove_stock(how_many,product_name,rental_products)

        write_inventory(new_inventory)

        total_amount = total(how_many, product_name, rental_products)
    
        print('$:',total_amount)

        print('With tax added that would be $:', round(sales_tax(total_amount), 3))

        history(product_name, new_inventory)
    
    elif category == '2':
        product_name = 'Side-by-Side'.strip()
    
        how_many = int(input('how many Side-by-Sides would you like?\n:'))
    
        new_inventory = remove_stock(how_many,product_name,rental_products)

        write_inventory(new_inventory)

        total_amount = total(how_many, product_name, rental_products)
    
        print('$:',total_amount)

        print('With tax added that would be $:', round(sales_tax(total_amount), 3))
    
    elif category == '3':
        
        product_name = 'Scooter'.strip()
    
        how_many = int(input('how many Scooters would you like?\n:'))
    
        new_inventory = remove_stock(how_many,product_name,rental_products)

        write_inventory(new_inventory)

        total_amount = total(how_many, product_name, rental_products)
    
        print('$:',total_amount)

        print('With tax added that would be $:', round(sales_tax(total_amount), 3))
    
    elif category == '4':
        product_name = 'Bike'.strip()
    
        how_many = int(input('how many Bikes would you like?\n:'))
    
        new_inventory = remove_stock(how_many,product_name,rental_products)

        write_inventory(new_inventory)

        total_amount = total(how_many, product_name, rental_products)
    
        print('$:',total_amount)

        print('With tax added that would be $:', round(sales_tax(total_amount), 3))
    

#if they choose the number 2 they get a side-by-side
#sbs stands for side-by-side
    
if __name__ == '__main__':
    main()

