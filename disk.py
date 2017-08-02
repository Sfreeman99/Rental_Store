def read_inventory():
    with open('inventory.txt','r') as inventory:
        inventory.readline()
        inventory = inventory.readlines()
    
    rental_products = {}
    for item in inventory:
        sublist = item.strip().split('||')
        rental_products[sublist[0].strip()] = {
            'Original Price': float(sublist[1].strip()),
            'stock': int(sublist[2].strip()),
            'rental price': float(sublist[3].strip())
        }

    return rental_products
    
def write_inventory(new_inventory):
    message = 'Category || Original Price || In Stock || Price to Rent ||\n'
    for key, value in new_inventory.items():
        message += '{} || {} || {} || {}\n'.format(key, value['Original Price'],value['stock'], value['rental price'])
    with open('inventory.txt','w') as new_file:
        new_file.write(message)

def history(name, category, decision, tax):
    message = '\n{}, {}, {}, {}'.format(name , category, decision, tax)
    with open('history.txt', 'a') as history:
        history.write(message)

def add_new_product(category,original_price,stock,rental_price):
    message = '\n{} || {} || {} || {}'.format(category, original_price, stock, rental_price)
    with open('inventory.txt','a') as new_product:
        new_product.write(message)

def total_revenue_reader():
    with open('history.txt','r') as money:
        money.readline()
        money_counter = money.readlines()
    revenue = []
    for item in money_counter:
        sublist = item.split(', ')
        revenue.append(float(sublist[3]))

    return revenue

def history_reader():
    with open('history.txt','r') as history:
        history.readline()
        history = history.readlines()
    message = 'First Name and Last Name, Item Rented, Returning/Renting, Money earned\n'
    for item in history:
        sublist = item.split(', ')
        message += '''
                    ----------------------------------------
                        {}, {}, {}, {}
                    ----------------------------------------\n'''.format(sublist[0],sublist[1],sublist[2],float(sublist[3]))
    return message  

