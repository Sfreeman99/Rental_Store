def read_inventory():
    with open('inventory.txt','r') as inventory:
        inventory.readline()
        inventory = inventory.readlines()
    
    rental_products = {}
    for item in inventory:
        sublist = item.split('||')
        rental_products[sublist[5].strip()] = {'Year': int(sublist[0].strip()),'Manufacturer': sublist[1].strip(), 'Model Name': sublist[2].strip(), 'Original Price': float(sublist[3].strip()), 'stock': int(sublist[4].strip()), 'rental price': float(sublist[6].strip())}
    return rental_products

