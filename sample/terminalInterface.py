from customer import Customer
from passwordAuthentication import Password
import terminalFunctions as tf

version = '0.1'

def displayInterface():
    """
    Terminal-Based banking application

    :type customers: dict
    :param customers: dictionary of all created customers

    :type users: Password
    :params users: Class with all developed user-password authentication
    """

    customers = {}
    users = Password({})

    # Displays welcome message
    print("Welcome to banking inteface: v" + version)

    # Performs until user exits
    while(True):

        # Asks for login information
        print('\nPlease enter your login information ' + \
              'or enter "new" for the username and password' + \
              'to create a new account' + \
              'or enter "exit" for the username and password to leave')
        username = input('Username: ')
        password = input('Password: ')

        # User creates new account
        if(username == 'new'  and password == 'new'):
            print('\nAccount Creation:\n' + \
                  'Please select a username and password')
            username = input('Username: ')
            password = input('Password: ')

            # If the user inputs an incorrect value
            while(username == 'new' or \
                  username == 'exit' or \
                  not(users.addAutheticatedUser(username, password))):
                print('Error creating your account\n' + \
                      'Please note that the username' + \
                      ' cannot be "new" or "exit"')
                username = input('Username: ')
                password = input('Password: ')

            # Setups user account
            userID = users.hashUsername(username)
            customers[userID] = Customer(0,userID)

            print('Account Created!')

        # User exits the program
        elif(username == 'exit' and password == 'exit'):
            break

        # User logs in to system
        else:
            # If the user enters an incorrect combination
            if(not(users.authenticate_password(username, password))):
                print("Invalid combination. Please try again.")

            else:
                # Gets userID info
                userID = users.hashUsername(username)
                userID_8 = userID[:8]
                customer = customers[userID]
                print('\nWelcome! for help please type "help"')

                # Runs until user logs out
                while(True):

                    # Asks user for input terminal style
                    func = input('{} >>'.format(userID_8))

                    # Log-out function
                    if(func == 'exit'):
                        tf.exit()
                        break

                    # Help function
                    elif(func[:4] == 'help' or func[:4] == 'quit'):
                        tf.help()

                    elif(func[:6] == 'whoami'):
                        tf.whoami(customer)

                    # Balance function
                    elif(func[:7] == 'balance'):
                        tf.balance(customer)

                    # Deposit function
                    elif(func[:7] == 'deposit'):
                        valList = func.split()
                        if(len(valList) == 2):
                            try:
                                tf.deposit(customer, float(valList[1]))
                            except ValueError:
                                print('Invalid Deposit amount')
                        else:
                            print('"deposit" requires 1 argument:\n' + \
                                  'deposit [VALUE TO DEPOSIT]\n' + \
                                  'For help, type "help deposit"')

                    # Withdrawal function
                    elif(func[:10] == 'withdrawal'):
                        valList= func.split()
                        if(len(valList) == 2):
                            try:
                                tf.withdrawal(customer, \
                                              float(valList[1]))
                            except ValueError:
                                print('Invalid witdrawal amount')
                        else:
                            print('"withdrawal" requires 1 ' + \
                                  'argument:\n' + \
                                  'witdrawal' + \
                                  '[VALUE TO WITHDRAWAL]\n' + \
                                  'For help, type "help withdrawal"')

                    # Unrecognized command
                    else:
                        print('Command unrecognized')
                        print('For help, please enter "help"')



if __name__ == '__main__':
    displayInterface()
