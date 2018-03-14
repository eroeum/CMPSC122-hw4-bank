from customer import Customer
import os

def exit():
    """
    Exits the program
    This is a "fake" function that only confirms exit
    Clears screen after exit
    """

    clear('Unix')

    return

def help(accountType, helpFunc = ''):
    """
    Help menu for giving users all commands with short description

    :type accountType: string
    :param accountType: Type of account

    :type helpFunc: string
    :param helpFunc: Option functional to get more info
    """

    if(helpFunc == ''):
        print('For more information on a specific command, ' + \
              'type "help" command-name')

        # Dictionary of functions available
        func = {}

        if(accountType in ['Customer', 'Bank Teller', \
                           'Assistant', 'Manager']):
            func['whoami'] = 'Display your ID'
            func['clear'] = 'Clears the screen'
        if(accountType in ['Customer']):
            func['balance'] = 'Displays balance in your account'
            func['deposit'] = 'Deposits money into to your account'
            func['withdrawal'] = 'Withdrawals money from your account'
        if(accountType in ['Bank Teller', 'Assistant', 'Manager']):
            func['make'] = 'Creates a new account'
            func['ls'] = 'Displays all muatable accounts'
            func['requests'] = 'Displays the requests of a customer'
            func['accept']  = 'Accepts a request of customer'



        # Sorts commands alphabetically
        cmds = sorted(func)

        # Prints help commands
        for cmd in cmds:
            print('{}: {}'.format(cmd,func[cmd]))

    # whoami help
    elif(helpFunc == 'whoami'):
        print('WHOAMI\n'+
              '\n' +
              'NAME\n' +
              '     whoami - print effective userid\n' +
              'SYNOPSIS\n' +
              '     whoami\n' +
              'DESCRIPTION\n' +
              '     Print the user name associated with the current' +
              ' effective user ID.')

    elif(helpFunc == 'clear'):
        print('CLEAR\n'+
              '\n' +
              'NAME\n' +
              '     clear - clears the terminal screen\n' +
              'SYNOPSIS\n' +
              '     clear [OPTION]\n' +
              'DESCRIPTION\n' +
              '     Clears the entire terminal screen by envoking the' +
              ' clear command.\n' +
              'OPTIONS\n' +
              '     -w: Clears screen if on a windows machine i.e.' +
              ' command prompt')

    elif(helpFunc == 'balance'):
        print('BALANCE\n'+
              '\n' +
              'NAME\n' +
              '     balance - print effective balance of user\n' +
              'SYNOPSIS\n' +
              '     balance\n' +
              'DESCRIPTION\n' +
              '     Print the effective balance associated with the' +
              ' current account.')

    elif(helpFunc == 'deposit'):
        print('DEPOSIT\n'+
              '\n' +
              'NAME\n' +
              '     deposit - submits a request to add value to' +
              ' your account\n'
              'SYNOPSIS\n' +
              '     balance [VALUE TO ADD]\n' +
              'DESCRIPTION\n' +
              '     Submits a request to add a value to your account\n' +
              '     The value entered after balance will be the\n' +
              ' desired amount\n' +
              'EXAMPLE\n' +
              '     deposit 100')

    elif(helpFunc == 'withdrawal'):
        print('WITHDRAWAL\n'+
              '\n' +
              'NAME\n' +
              '     withdrawal - submits a request to deduct value' +
              ' from your account\n'
              'SYNOPSIS\n' +
              '     withdrawal [VALUE TO DEDUCT]\n' +
              'DESCRIPTION\n' +
              '     Submits a request to deduc a value from' +
              ' your account\n' +
              '     The value entered after balance will be the\n' +
              ' desired amount\n' +
              'EXAMPLE\n' +
              '     withdrawal 100')

    elif(helpFunc == 'make'):
        print('MAKE\n'+
              '\n' +
              'NAME\n' +
              '     make - creates a bank teller or assistant' +
              ' account\n'
              'SYNOPSIS\n' +
              '     make [ACCOUNT TYPE] [USER ID] [PASSCODE]\n' +
              'DESCRIPTION\n' +
              '     Creates a bank teller or assistant to help\n' +
              '     The account type can either be "assistant" or' +
              ' "teller"\n' +
              '     The userid will be the user id before hashing' +
              'for the assistant/bankteller to log in with\n' +
              '     The passcode will be the password before hashing' +
              'for the assistant/bankteller to log in with\n' +
              'EXAMPLE\n' +
              '     make assistant assistant1 greatPassword\n' +
              '     make teller teller1 greatPassword')

    elif(helpFunc == 'ls'):
        print('LS\n'+
              '\n' +
              'NAME\n' +
              '     ls - print mutable customers, banktellers, and' +
              ' assistants\n' +
              'SYNOPSIS\n' +
              '     ls\n' +
              'DESCRIPTION\n' +
              '     Use ls to view all available customers, bank' +
              ' tellers, and assistants that can be accessed\n' +
              '     Prints all short userID (first 8 characters)')

    return

def balance(person):
    """
    Shows balance in the account
    """

    print('Account Balance: {}'.format(str(person.getValue())))
    return

def deposit(person, value_to_add):
    """
    Deposits value into the account

    :type value_to_add: float
    :param value_to_add: Value to be added in funds
    """

    person.requestDelta(value_to_add)
    return

def withdrawal(person, value_to_deduct):
    """
    Withdrawals value from the account

    :type value_to_deduct: float
    :param value_to_deduct: Value to be withdrawled in funds
    """

    person.requestDelta(-1 * value_to_deduct)
    return

def whoami(person):
    """
    Return the owner's ID

    """

    print(person.getOwner())
    return

def make(genesis, accountType, userID, users):
    """
    Create an account

    :type genesis: Customer
    :param genesis: Original account

    :type accountType: string
    :param accountType: type of account

    :type userID: string
    :param userID: user id of the account
    """

    if(accountType == 'assistant'):
        ret0 = genesis.createAssistant(userID, [], [])
    elif(accountType == 'teller'):
        ret0 = genesis.createBankTeller(userID, [])

    users[userID] = ret0
    return users

def ls(accountType, account, customers):
    """
    Lists all accounts accessible

    :type accountType: string
    :param accountType: type of account

    :type account: Customer
    :param account: The account that is being inspected
    """

    # View Customers
    if(accountType in ['Bank Teller', 'Assistant', 'Manager']):
        print('\nCustomers:')
        for customer in customers:
            if(not(customer is None)):
                print(customer[:8])

    # View Bank Tellers
    if(accountType in ['Assistant', 'Manager']):
        print('\nBank Tellers:')
        for bankteller in account.viewBankTellers():
            if(not(bankteller is None)):
                print(bankteller.getOwner()[:8])

    # View Assistants
    if(accountType in ['Manager']):
        print('\nAssistants:')
        for assistant in account.viewAssistants():
            if(not(assistant is None)):
                print(assistant.getOwner()[:8])

def clear(platf):
    if(platf == 'Windows'):
        os.system('cls')
    else:
        os.system('clear')

def requests(user, customer):
    """
    Lists all requests of the customer

    :type user: class
    :param user: The current user

    :type customer: customer
    :param customer: Customer that will be viewed
    """

    requests = user.viewRequests(customer)
    requestNum = 1
    for request in requests:
        print('#{}|{}'.format(requestNum,request))
        requestNum += 1

def acceptRequest(user, customer, reqNum):
    """
    Accepts a customer's request

    :type user: class
    :param user: The current user

    :type customer: customer
    :param customer: Customer that is being accepted

    :type reqNum: int
    :param reqNum: Request number correponding to the request
    """

    user.acceptRequest(customer, int(reqNum))
