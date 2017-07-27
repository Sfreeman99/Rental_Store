def read_inventory():
    with open('inventory.txt','r') as inventory:
        inventory.readline()
        inventory = inventory.readlines()
    
    rental_products = {}
    for item in inventory:
        sublist = item.split('||')
        rental_products[sublist[0].strip()] = {'Year': int(sublist[1].strip()),'Manufacturer': sublist[2].strip(), 'Original Price': float(sublist[3].strip()), 'stock': int(sublist[4].strip()), 'rental price': float(sublist[5].strip())}
    return rental_products

def write_inventory(new_inventory):
    message = 'Year || Manufacturer || Mode Name || Original Price || In Stock || Category || Price to Rent ||\n'
    for key,value in new_inventory:
        message += '{} || {} || {} || {} || {} || {} || {} ||'.format(value['Year'], value['Manufacturer'], value['Model Name'], value['Original Price'],value['stock'], value['rental price'],key)
    with open('inventory.txt','w') as new_file:
        new_file.write(message)