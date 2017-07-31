
def remove_stock(how_many,product_name, rental_products):
    ''' (int,str, dict of dict) -> 

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
    elif product_name == 'Side-by-Side':
        rental_products[product_name]['stock'] -= how_many
    elif product_name == 'Scooter':
        rental_products[product_name]['stock'] -= how_many
    elif product_name == 'Bike':
        rental_products[product_name]['stock'] -= how_many
    return rental_products
        

def total(how_many,product_name,rental_products):
    ''' int,str, dict of dict -> total

    returns the total transaction of what you rented

    >>> total(1, 'Atv', {'Atv':{'rental price': 30, 'stock': 3}})
    30
    >>> total(2, 'Atv', {'Atv':{'rental price': 30, 'stock': 3}})
    60
    >>> total(0, 'Atv', {'Atv':{'rental price': 30, 'stock': 3}})
    0
    >>> total(1, 'Atv', {'Atv':{'rental price': 30, 'stock': 3}})
    30
    '''
    total = rental_products[product_name]['rental price'] * how_many
    return round(total, 2)
    
def sales_tax(total):
    ''' float -> float
    
    takes in an int and gives out a float
    that would be the tax
    
    >>> sales_tax(3)
    3.21
    >>> sales_tax(2)
    2.14
    >>> sales_tax(1)
    1.07
    >>> sales_tax(0)
    0.0
    '''
    
    return ((float(total) * .07) + float(total))