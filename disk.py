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