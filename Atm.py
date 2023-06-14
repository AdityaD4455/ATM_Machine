print('Welcome to ATM')
restart = ('Y')
chances = 3
balance = 1000

while chances >= 0:
    pin = int(input("Please enter your 4 digit pin : "))
    if pin == (1234):
        print('You entered your pin correctly \n')
        while restart not in ('n','NO','no','N'):
            print('Please press 1 for your Balance \n')
            print('Please press 2 for your withdrawl \n')
            print('Please press 3 for your Pay \n')
            print('Please press 4 for your Return card \n')
            option = int(input('What would you like to choose?'))
            if option==1:
                print('Your balance is :- ', balance,'\n')
                restart = input('would you like to go back?')
                if restart in ('n','NO',',no','N'):
                    print('Thanks you for useing ATM')
                    break
            elif option == 2:
                option2 =('y')
                withdrawl = float(input('How much would you like to withdrawl ? \n $100/$200/$500/$2000 for other enter 1' ))
                if withdrawl in [100,200,500,2000]:
                    balance = balance - withdrawl
                    print('\n your balnce is now :-', balance)
                    restart = input('what would you like to do?')
                    if restart in ('n','NO',',no','N'):
                        print('Thanks you for useing ATM')
                        break
                elif withdrawl != [100,200,500,2000]:
                    print('Invaild amount, please retry \n')
                    restart=('y')
            elif withdrawl==1:
                withdrawl=float(input('Please enter the desired amount:'))
            elif option == 3:
                pay_in = float (input('How much would you like to pay'))
                balance = balance + pay_in
                print('\n Your balance is now $', balance)
                restart = input('Would you like to go back?')
                if restart in ('n','NO',',no','N'):
                    print('Thanks you for useing ATM')
                    break
            elif option==4:
                print('Print wait while you card is returned...\n')
                print('Thanks you for using our ATM')
                break
            else:
                print('please enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect password')
        chances = chances-1
        if chances == 0:
            print('\n No more tries, contact in bank')
            break1111