'''
banking app with a solid user interface
checking balances
transferring funds
depositing money
withdrawing money
checking account limits
pin confirmation prompt

'''
import random as rd

def check_bal():

    current_balance = rd.randint(100, 999999)
    return f'your current balance is Ksh{current_balance}'


print('welcome to safeBank Banking App!\n Please enter your details below : ')
while True:
    user_email = input('please enter your email address: ')
    #user_pin = input('please enter your pin: ')

    if '@' in user_email and '.' in user_email:
        print('Email exists')

    else:
        print('Invalid email, try again')
        continue
    user_pin = input('please enter your pin: ')

    if len(user_pin) == 4 and user_pin.isdigit:
        print('pin accepted')
        break

    else:
        print('invalid pin, try again!')

print('welcome!please make a selection below: ')

print('''
1. to check your current balance
2. to transfer funds
3. to deposit an amount of money
''')

choice = input('please make your selection from the above choices(enter a number) : ')

if choice == '1':

    confirm_pin = input('please enter your pin to confirm: ')

    if user_pin == confirm_pin:
        balance = check_bal()
        print(balance)
    else:
        print('incorrect pin')
