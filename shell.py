from core import *
from disk import *
def customer_main():
    print('Welcome Customer')
    decision = ''
    while decision != 'Rent' or 'Return':
        decision = input(''' What would you like to do today?:
        ** You have to type out the name not the number **
        \t1. Rent
        \t2. Return
        :''').title().strip()
        if decision == 'Rent':
            rent()
            break
        elif decision == 'Return':
            return_item()
            break
        else:
            print('Invalid Choice... Please type Rent or Return\n')

def rent():
    #the variable 'how many' is used to see how many of the products the customer wants
    rental_products = read_inventory()
    name = input('What is your first and last name?\n:').title()
    category = category_decision()
    # while category != 'Atv' or 'Side-by-Side' or 'Scooter' or 'Bike':
    #     category = input('What do you want to rent:\n\t**Spell Exactly how it is shown**\n\t1. Atv\n\t2. Side-by-Side\n\t3. Scooter\n\t4. Bike\n:')
    #     if category in rental_products:
        
    # how_many_hours = int(input('how many hours would you like?\n:'.format(category)))

    how_many_hours = how_many_hours_decision(category, name)

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

def how_many_hours_decision(category, name):
    how_long = ''
    while True:
        how_long = int(input('How long would you like to rent the {} {}\n1hr\n2hrs\n3hrs\n4hrs?'.format(category, name)))
        if (how_long == 1) or (how_long == 2) or (how_long == 3) or (how_long == 4):
            return how_long
            break
        else:
            print('Invalid Choice... Please choose 1, 2, 3, or 4')
def category_decision():
    rental_products = read_inventory()
    category = ''
    while True:
        category = input('What do you want to rent:\n\t**Spell Exactly how it is shown**\n\t1. Atv\n\t2. Side-by-Side\n\t3. Scooter\n\t4. Bike\n:')
        if category in rental_products:
            return category
            break
        else:
            print('Invalid Choice.... Please Try Again\n')

def return_item():
    rental_products = read_inventory()
    name = input('What is your name?\n:').title()
    category = input('What do you want to return:\n\t1. Atv\n\t2. Side-by-Side\n\t3. Scooter\n\t4. Bike\n:')
    new_inventory = add_stock(category, rental_products)
    write_inventory(new_inventory)
    current_deposit = deposit(category,rental_products)
    print('Here is your deposit of ${:.2f} back {}.\n\tHave A Nice Day !!!'.format(current_deposit, name))
  
def main():
    print('Welcome to Shedlia\'s Wheels 4 You')
    answer = ''
    while answer != 'customer' or 'employee':
        answer = input('Are you a customer or employee\n:').lower().strip()
        if answer == 'customer':
            customer_main()
            break
        elif answer == 'employee':
            employee_main()
            break
        else:
            print('please choose one or the other and spell it correctly...')

def employee_main():
    print('Welcome employee of Shedlia\'s Rental Store')
    decision = ''
    while decision != '1' or '2' or '3':
        decision = input('What do you want to do today?\n\t1. Add product to stock\n\t2. Check total revenue\n\t3.See transaction History\n\t**Pick numbers Only**\n:')
        if decision == '1':
            category = input('What is the name of the item you want to rent?\n**How you type it is how it will show in the inventory**\n:')
            original_price = float(input('what is the price you payed for one of that particular item?\n:'))
            stock = int(input('How many of them do you have currently?\n:'))
            rental_price = float(input('What do you want the rental price to be?\n:'))
            add_new_product(category,original_price,stock,rental_price)
            print('The item {} with the rental price of ${:.2f} has been added to the inventory'.format(category, rental_price))
            break
        elif decision == '2':
            total = total_revenue_reader()
            revenue = total_revenue(total)
            print('Your total revenue would be:\n${:.2f}'.format(revenue))
            break
        elif decision == '3':
            print('These are all your transactions:\n\n',history_reader(), sep = '')
            break

        else:
            print('Not Valid Input... Please Try Again!!!')
            




if __name__ == '__main__':
    main()

