def read_inventory():
    with open('inventory.txt','r') as inventory:
        inventory.readline()
        inventory = inventory.readlines()
    
    rental_products = {}
    for item in inventory:
        sublist = item.split('||')
        rental_products[sublist[5].strip()] = {'Year': sublist[0].strip(),'Manufactioner': sublist[1].strip(), 'Model Name': sublist[2].strip(), 'Original Price': sublist[3].strip(), 'stock': sublist[4].strip()}
    print(rental_products)

