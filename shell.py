from core import rental_products
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
    how_many = int(input('how many Atv\'s would you like?'))
    rental_products['Atv']['stock'] -= how_many
#if they choose the number 2 they get a side-by-side
elif decision == '2':
    how_many = int(input('how many Side-by-Side\'s would you like?'))
    rental_products['Side-by-Side']['stock'] -= how_many
#if they choose the number 3 they get both an atv and side-by-side
elif decision == '3':
    print('Both')
    rental_products['Atv']['stock'] -= 1
    rental_products['Side-by-Side']['stock'] -= 1

print(rental_products)



