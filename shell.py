rental_products = {'Atv':{'price': 30, 'stock': 1}, 'Side-by-Side':{'price': 100, 'stock': 1}}

print('Welcome to Shedlia\'s Atv and Side-By-Side Rental Agency')
# give the user choices through numbers So it can be easier to choose what you want
decision = input(''' What would you like:
\t1. Atvs
\t2. Side-by-Sides\n:''')

if decision == '1':
    print('Atv')
    rental_products['Atv']['stock'] -= 1
elif decision == '2':
    print('Side-by-Side')
    rental_products['Side-by-Side']['stock'] -= 1

print(rental_products)



