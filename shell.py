import core
import disk


def main():
    print('Welcome to Shedlia\'s Wheels 4 U'.center(100))
    answer = ''
    while True:
        answer = input('Are you a customer or employee\n:').lower().strip()
        if answer == 'customer':
            customer_main()
            exit()
        elif answer == 'employee':
            employee_main()
            exit()
        else:
            print('please choose one or the other and spell it correctly...')


def employee_main():
    name = input('What is your name?\n\t:').title().strip()
    print('Welcome {}!!!'.format(name))
    decision = ''
    while decision != 'q':
        decision = input(
            'What do you want to do today?\n\t1. Add product to stock\n\t2. Check total revenue\n\t3.See transaction History\n\t**Pick numbers Only**\n**Choose '
            'q'
            ' to quit at any time**\n:')
        if decision == '1':
            category = category_name()
            original_price = price()
            stock = stock_quantity()
            rental_price = rental_value()
            disk.add_new_product(category, original_price, stock, rental_price)
            print(
                'The item {} with the rental price of ${:.2f} has been added to the inventory'.
                format(category, rental_price))
        elif decision == '2':
            total = disk.total_revenue_reader()
            revenue = core.total_revenue(total)
            print('Your total revenue would be:\n${:.2f}\n'.format(revenue))

        elif decision == 'q':
            print('Have a nice day {}!!!'.format(name))
        elif decision == '3':
            print('These are all your transactions:\n\n{}'.format(
                disk.history_reader()))

        else:
            print('Not Valid Input... Please Try Again!!!\n')


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
    decision = 'rent'
    rental_products = disk.read_inventory()
    current_menu = disk.menu(rental_products)
    name = input('What is your first and last name?\n:').title()
    category = category_decision(decision, current_menu)

    current_deposit = core.deposit(category, rental_products)

    print('Your deposit would be $:{:.2f}'.format(current_deposit))

    how_many_hours = how_many_hours_decision(category, name)

    new_inventory = core.remove_stock(category, rental_products)

    disk.write_inventory(new_inventory)

    total_amount = core.total(how_many_hours, category,
                              rental_products) + current_deposit

    print('Your total will be $: {:.2f}'.format(total_amount))

    print('With tax added that would be $: {:.2f}'.format(
        core.sales_tax(total_amount)))

    tax = core.sales_tax(total_amount)

    disk.history(name, category, decision, tax)


def return_item():
    decision = 'return'
    rental_products = disk.read_inventory()
    current_menu = disk.menu(rental_products)
    name = input('What is your name?\n:').title().strip()
    category = category_decision(decision, current_menu)
    new_inventory = core.add_stock(category, rental_products)
    disk.write_inventory(new_inventory)
    current_deposit = core.deposit(category, rental_products)
    print('Here is your deposit of ${:.2f} back {}.\n\tHave A Nice Day !!!'.
          format(current_deposit, name))
    disk.return_history(name, category, decision, current_deposit)


def how_many_hours_decision(category, name):
    how_long = ''
    while how_long != '1' or '2' or '3' or '4':
        how_long = input(
            'How long would you like to rent the {} {}\n\t1. 1hr\n\t2. 2hrs\n\t3. 3hrs\n\t4. 4hrs?\n:'.
            format(category, name))
        if (how_long == '1') or (how_long == '2') or (how_long == '3') or (
                how_long == '4'):
            return int(how_long)
            break
        else:
            print('Invalid Choice... Please choose 1, 2, 3, or 4\n')


def category_decision(decision, current_menu):
    rental_products = disk.read_inventory()
    category = ''
    while True:
        # category = input('What do you want to {}:\n\t**Spell Exactly how it is shown**\n\t1. Atv\n\t2. Side-by-Side\n\t3. Scooter\n\t4. Bike\n:'.format(decision)).strip()
        category = input(
            'What do you want to {}:\n\t**Spell Exactly how it is shown**\n{}\n:'.
            format(decision, current_menu)).strip()

        if category in rental_products:
            return category
            break
        else:
            print('Invalid Choice.... Please Try Again\n')


def category_name():
    category = input(
        'What is the name of the item you want to rent out?\n**How you type it is how it will show in the inventory**\n:'
    )
    return category


def price():
    decision = float(
        input(
            'what is the price you payed for one of that particular item?\n:'))
    return decision


def stock_quantity():
    decision = int(input('How many of them do you have currently?\n:'))
    return decision


def rental_value():
    decision = float(input('What do you want the rental price to be?\n:'))
    return decision


if __name__ == '__main__':
    main()
