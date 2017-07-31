
def remove_stock(product_name, rental_products):
    ''' (int,str, dict of dict) -> 

    takes in how many of the products the customer wants
    and takes it away from stock

    >>> (remove_stock('Atv',{'Atv':{'price': 30, 'stock': 5}}) ==
    ... {'Atv':{'price': 30, 'stock': 4}})
    True
    >>> (remove_stock('Atv',{'Atv':{'price': 30, 'stock': 5}}) ==
    ... {'Atv':{'price': 30, 'stock': 4}})
    True  
    >>> (remove_stock('Atv',{'Atv':{'price': 30, 'stock': 5}}) ==
    ... {'Atv':{'price': 30, 'stock': 4}})
    True
    '''
    if product_name == 'Atv':
        rental_products[product_name]['stock'] -= 1
    elif product_name == 'Side-by-Side':
        rental_products[product_name]['stock'] -= 1
    elif product_name == 'Scooter':
        rental_products[product_name]['stock'] -= 1
    elif product_name == 'Bike':
        rental_products[product_name]['stock'] -= 1
    return rental_products
        

def total(how_many_hours,product_name,rental_products):
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
    total = rental_products[product_name]['rental price'] * how_many_hours
    return round(total, 2)
    
def sales_tax(total_amount):
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
    
    sale = ((float(total_amount) * .07) + float(total_amount))
    return sale


def deposit(category,rental_products):
    ''' str, dict of str,float,int,float -> deposit

    takes in the category and looks at the original price
    in rental products and takes %10 of it for the deposit

    >>> deposit('Water', {'Water':{'Original Price': 10}})
    1.0
    >>> deposit('Water', {'Water':{'Original Price': 20}})
    2.0
    

    '''
    return (rental_products[category]['Original Price'] * .1)