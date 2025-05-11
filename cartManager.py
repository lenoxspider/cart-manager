print('Fruit Basket Manager')
basket = ['apple', 'banana', 'orange']

def show():
    for item in basket:
        print('{}' .format(item))
    else:
        print('Your basket is empty.')

def confirm(name):
    if name in basket:
        print('{} is in your basket' .format(name))
    else:
        print('{} is not found in your basket' .format(name))

def increase(name):
    basket.append(name)
    print(f'{name} added successfully')

def decrease(name):
    if name in basket:
        basket.remove(name)
        print(f'{name} removed successfully')
    else:
        print('{} is not found' .format(name))

while True:
    user_input = input('# : ').strip()
    usin_small = user_input.lower()
    if usin_small == 'exit':
        break
    elif usin_small == 'view':
        show()
    elif usin_small.startswith('add '):
        item = user_input[4:].strip().lower()
        increase(item)
    elif usin_small.startswith('remove '):
        item = user_input[7:].strip()
        decrease(item)
    elif usin_small.startswith('check '):
        item = user_input[6:].strip()
        confirm(item)
