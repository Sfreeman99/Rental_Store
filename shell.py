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
    name = input('What is your first and last name?\n:').title()
    category = input('What do you want to rent:\n\t1. Atv\n\t2. Side-by-Side\n\t3. Scooter\n\t4. Bike\n:')
    rental_products = read_inventory()
    if category in rental_products:
        
        how_many_hours = int(input('how many hours would you like?\n:'.format(category)))

        current_deposit = deposit(category,rental_products)
    
        new_inventory = remove_stock(category,rental_products)

        write_inventory(new_inventory)

        total_amount = total(how_many_hours, category, rental_products)

        print('Your deposit would be $:',round(current_deposit, 2), sep = '')
    
        print('Your total will be $:',total_amount, sep = '')

        print('With tax added that would be $:', round(sales_tax(total_amount), 3), sep = '')

        decision = 'renting'

        tax = sales_tax(total_amount)

        history(name, category, decision, tax)

def return_item():
    rental_products = read_inventory()
    name = input('What is your name?').title()
    category = input('What do you want to rent:\n\t1. Atv\n\t2. Side-by-Side\n\t3. Scooter\n\t4. Bike\n:')
    item = input('What do you want to return:\n\t1. Atv\n\t2. Side-by-Side\n\t3. Scooter\n\t4. Bike\n:')
    add_stock(product_name, rental_products)
    current_deposit = deposit(category,rental_products)
    print('Here is your deposit of', current_deposit,'back.\n\tHave A Nice Day !!!')
    


        

#if they choose the number 2 they get a side-by-side
#sbs stands for side-by-side
    
if __name__ == '__main__':
    main()

