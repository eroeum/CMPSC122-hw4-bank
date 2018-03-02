from customer import Customer

def exit():
    """
    Exits the program
    This is a "fake" function that only confirms exit
    """

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
