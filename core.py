
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
    if product_name == 'Side-by-Side':
        rental_products[product_name]['stock'] -= how_many
    return rental_products
        

def total(how_many,product_name,sales_tax, rental_products):
    ''' int,str, dict of dict -> total

    returns the total transaction of what you rented

    >>> total(1, 'Atv',.07, {'Atv':{'rental price': 30, 'stock': 3}})
    30.07
    >>> total(2, 'Atv',.14, {'Atv':{'rental price': 30, 'stock': 3}})
    60.14
    >>> total(0, 'Atv',.00, {'Atv':{'rental price': 30, 'stock': 3}})
    0.0
    >>> total(1, 'Atv',.07, {'Atv':{'rental price': 30, 'stock': 3}})
    30.07
    '''
    price = rental_products[product_name]['rental price'] * how_many
    total = price + sales_tax
    return total
    
def sales_tax(how_many):
    ''' int -> float
    
    takes in an int and gives out a float
    that would be the tax
    
    >>> sales_tax(3)
    0.21
    >>> sales_tax(2)
    0.14
    >>> sales_tax(1)
    0.07
    >>> sales_tax(0)
    0.0
    '''
    tax = round(how_many * .07, 2)
    return tax