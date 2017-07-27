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
        # rent()
        rent_2()
    elif decision == '2':
        return_item()

# def rent():
    #the variable 'how many' is used to see how many of the products the customer wants
    category = input('What do you want to rent:\n\t1. Atv\n\t2. Side-by-Side\n:')
    rental_products = read_inventory()
    print(rental_products)
    if category == '1':
        product_name = 'Atv'.strip()
        
        how_many = int(input('how many Atv\'s would you like?\n:'))
    
        new_inventory = remove_stock(how_many,product_name,rental_products)

        write_inventory(new_inventory)

        tax = sales_tax(how_many)
    
        print('$:',total(how_many, product_name, tax, rental_products))
    
    if category == '2':
        product_name = 'Side-by-Side'.strip()
    
        how_many = int(input('how many Atv\'s would you like?\n:'))
        
        new_inventory = remove_stock(how_many,product_name,rental_products)
        
        write_inventory(new_inventory)
        
        remove_stock(how_many,product_name,rental_products)

        tax = sales_tax(how_many)

        print('$:',total(how_many,product_name,tax,rental_products))        
    
#if they choose the number 2 they get a side-by-side
#sbs stands for side-by-side

def rent_2():
    category = input('What would you like to rent:\n\tAtv\n\tSide-by-Side\n:')
    manufacturer = input('What manufacturer would you prefer?\n\tHonda\n\tYamaha')
    year = input('What year model do you want:\n\t2017\n\t2018')
    
if __name__ == '__main__':
    main()

