from bankTeller import BankTeller

class Assistant(BankTeller):
    """
    Represents a user with mid-level priveledges
    Users having these priveledges are usually bank tellers
    """
    def __init__(self, userID, customers, bankTellers):
        """
        Creates the variables associated with this class

        :type userID: string
        :param userID: the owner of the account

        :type customers: list
        :param customers: all customers that can be accessed

        :type bankTellers: list
        :param bankTellers: all bank tellers that can be accessed
        """

        BankTeller.__init__(self, userID, customers)
        self.__bankTellers = bankTellers

    def viewBankTellers(self):
        """
        Returns the bank tellers under this account
        """

        return self.__bankTellers

    def createBankTeller(self, userID, customers):
        """
        Creates a Bank Teller under this account

        :type userID: string
        :param userID: the userID of the assistant

        :type customers: list
        :param customers: all customers that assitant can access

        :type bankTellers: list
        :param bankTellers: all bank tellers that assistant can access
        """

        bankTeller = BankTeller(userID, customers)
        self.__bankTellers.append(bankTeller)

        return bankTeller
