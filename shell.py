from core import remove_stock, total
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
    decision = input('What do you want to rent:\n\t1. Atv\n\t2. Side-by-Side\n:')
    rental_products = read_inventory()
    if decision == '1':
        product_name = 'Atv'.strip()
        
        how_many = int(input('how many Atv\'s would you like?\n:'))
    
        print(remove_stock(how_many,product_name,rental_products))
    
        print('$:',total(how_many,product_name,rental_products))
    
    if decision == '2':
        product_name = 'Side-by-Side'.strip()
    
        how_many = int(input('how many Atv\'s would you like?\n:'))
    
        remove_stock(how_many,product_name,rental_products)

        print('$:',total(how_many,product_name,rental_products))        
    
#if they choose the number 2 they get a side-by-side
#sbs stands for side-by-side

    
if __name__ == '__main__':
    main()

