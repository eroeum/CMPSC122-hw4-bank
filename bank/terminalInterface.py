from customer import Customer
from manager import Manager
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
    bankTellers = {}
    assistants = {}
    managers = {}
    users = Password({})

    # Displays welcome message
    print("Welcome to banking inteface: v" + version)

    # Initiliaze genesis account
    print('To initialize the bank, a manager must be created.')
    print('Please choose a username and password:')
    username = input('Username: ')
    password = input('Password: ')
    while(username == 'new' or username == 'exit'):
        print('Error creating your account\n' + \
              'Please note that the username cannot be "new" or "exit"')
        username = input('Username: ')
        password = input('Password: ')
    users.addAutheticatedUser(username, password)
    userID = users.hashUsername(username)
    managers[userID] = Manager(userID, [], [], [])

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

                # Checks if user is a customer
                if(userID in customers):
                    user = customers[userID]
                    accountType = 'Customer'

                # Checks if user is a bankTeller
                elif(userID in bankTellers):
                    user = bankTellers[userID]
                    accountType = 'Bank Teller'

                # Checks if user is a assistant
                elif(userID in assistants):
                    user = assistants[userID]
                    accountType = 'Assistant'

                # Checks if user is a mangager
                elif(userID in managers):
                    user = managers[userID]
                    accountType = 'Manager'

                print('\nWelcome! for help please type "help"')

                # Runs until user logs out
                while(True):

                    # Asks user for input terminal style
                    func = input('{} ({})>>'.format(userID_8, \
                                                    accountType))

                    # Log-out function
                    if(func == 'exit'):
                        tf.exit()
                        break

                    # Help function
                    elif(func[:4] == 'help' or func[:4] == 'quit'):
                        tf.help()

                    elif(func[:6] == 'whoami'):
                        tf.whoami(user)

                    # Balance function
                    elif(func[:7] == 'balance'):
                        tf.balance(user)

                    # Deposit function
                    elif(func[:7] == 'deposit'):
                        valList = func.split()
                        if(len(valList) == 2):
                            try:
                                tf.deposit(user, float(valList[1]))
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
                                tf.withdrawal(user, \
                                              float(valList[1]))
                            except ValueError:
                                print('Invalid witdrawal amount')
                        else:
                            print('"withdrawal" requires 1 ' + \
                                  'argument:\n' + \
                                  'witdrawal' + \
                                  '[VALUE TO WITHDRAWAL]\n' + \
                                  'For help, type "help withdrawal"')

                    # Make function
                    elif(func[:4] == 'make'):
                        val = func.split()
                        if(len(val) == 4):

                            # Make assistant
                            if(val[1] == 'assistant' and \
                               accountType == 'Manager'):
                                accountID = users.hashUsername(val[2])
                                password = users.hashUsername(val[3])

                                if((users.addAutheticatedUser( \
                                       val[2], val[3])) and \
                                       not(accountID == 'new') and \
                                       not(accountID == 'exit')):
                                    assistants = tf.make(user, \
                                                         'assistant', \
                                                         accountID, \
                                                         assistants)
                                else:
                                    print('Error creating account')

                            # Make Bank Teller
                            elif(val[1] == 'teller' and \
                                 accountType in ['Manager',
                                                 'Assistant']):
                                accountID = users.hashUsername(val[2])
                                password = users.hashUsername(val[3])

                                if((users.addAutheticatedUser( \
                                       val[2], val[3])) and \
                                       not(accountID == 'new') and \
                                       not(accountID == 'exit')):
                                    bankTellers = tf.make(user, \
                                                          'teller', \
                                                          accountID, \
                                                          bankTellers)
                                else:
                                    print('Error creating account')

                            else:
                                print("Invalid Input")

                    # List function
                    elif(func[:2] == 'ls'):
                        tf.ls(accountType, user, customers)

                    # Clear screen
                    elif(func[:5] == 'clear'):
                        if(func[6:8] == '-w'):
                            tf.clear('Windows')
                        else:
                            tf.clear('Unix')

                    # View a customer's requests
                    elif(func[:8] == 'requests'):
                        val = func.split()
                        indv = val[1]
                        for customer in customers:
                            if(indv in customer[:8]):
                                indv = customers[customer]
                                tf.requests(user, indv)
                                break

                    # Acceps a customer's request
                    elif(func[:6] == 'accept'):
                        val = func.split()
                        indv = val[1]
                        reqNum = val[2]
                        for customer in customers:
                            if(indv in customer[:8]):
                                indv = customers[customer]
                                tf.acceptRequest(user, indv, reqNum)
                                break


                    # Unrecognized command
                    else:
                        print('Command unrecognized')
                        print('For help, please enter "help"')

if __name__ == '__main__':
    displayInterface()
