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

def help():
    """
    Help menu for giving users all commands with short descritpion
    """

    # Not Completed
    print('For more information on a specific command, ' + \
          'type "Help" command-name')

    # Dictionary of functions available
    func = {}
    func['balance'] = 'Displays balance in your account'
    func['deposit'] = 'Deposits money into to your account'
    func['withdrawal'] = 'Withdrawals money from your account'
    func['whoami'] = 'Display your ID'
    func['make'] = 'Creates a new account'
    func['clear'] = 'Clears the screen'
    func['ls'] = 'Displays all muatable accounts'

    # Sorts commands alphabetically
    cmds = sorted(func)

    # Prints help commands
    for cmd in cmds:
        print('{}: {}'.format(cmd,func[cmd]))
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

    person.requestDelta(-1 * deltaValue)
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
