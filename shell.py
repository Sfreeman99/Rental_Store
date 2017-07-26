from core import rental_products

def main():
    print('Welcome to Shedlia\'s Atv and Side-By-Side Rental Agency')
    # give the user choices through numbers So it can be easier to choose what you want
    decision = input(''' What would you like:
    \t1. Atvs
    \t2. Side-by-Sides
    \t3. Both
    :''').strip()
    #user chooses through numbers what they want
    #if they choose the number 1 they get an atv in stock
    if decision == '1':
        rent_atv()
    elif decision == '2':
        rent_sbs()
    elif decision == '3':
        rent_both()

def rent_atv():
    #the variable 'how many' is used to see how many of the products the customer wants
    how_many = int(input('how many Atv\'s would you like?'))
    rental_products['Atv']['stock'] -= how_many
    print(rental_products)
    
#if they choose the number 2 they get a side-by-side
#sbs stands for side-by-side
def rent_sbs():
    how_many = int(input('how many Side-by-Side\'s would you like?'))
    rental_products['Side-by-Side']['stock'] -= how_many
    print(rental_products)
    
#if they choose the number 3 they get both an atv and side-by-side
def rent_both():
    print('Both')
    how_many_atv = int(input('how many Atv\'s would you like?'))
    how_many_sbs = int(input('how many Side-by-Side\'s would you like?'))    
    rental_products['Atv']['stock'] -= how_many_atv
    rental_products['Side-by-Side']['stock'] -= how_many_sbs
    print(rental_products)

if __name__ == '__main__':
    main()

