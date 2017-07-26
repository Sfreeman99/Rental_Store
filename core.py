rental_products = {'Atv':{'price': 30, 'stock': 1}, 'Side-by-Side':{'price': 100, 'stock': 1}}


def remove_stock(how_many,product_name, rental_products):
    ''' (int, dict of dict) -> 

    takes in how many of the products the customer wants
    and takes it away from stock

    >>> (remove_stock(3,'Atv',{'Atv':{'price': 30, 'stock': 5}}) ==
    ... {'Atv':{'price': 30, 'stock': 2}})
    True
    >>> (remove_stock(5,'Atv',{'Atv':{'price': 30, 'stock': 5}}) ==
    ... {'Atv':{'price': 30, 'stock': 0}})
    True  
    >>> (remove_stock(1,'Atv',{'Atv':{'price': 30, 'stock': 5}}) ==
    ... {'Atv':{'price': 30, 'stock': 4}})
    True
    '''

    if product_name == 'Atv':
        rental_products[product_name]['stock'] -= how_many
    if product_name == 'Side-by-Side':
        rental_products[product_name]['stock'] -= how_many
    return rental_products
        
    