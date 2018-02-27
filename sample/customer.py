class Customer:
    """
    Represents a user with low-level priveledges
    Users only having these priveledges are usually customers
    """
    def __init__(self, value, userID_owner, userID_users = []):
        """
        Creates the variables assosciated with this class

        :type value: float
        :param value: monetary value within this bank (not subAccounts)

        :type userID_owner: string
        :param userID_owner: the owner of the account

        :type userID_user: string
        :param userID_user: priveledged users

        :type subAccounts: dict
        :param subAccounts: Accounts that can be accessed with this node

        :type requests: list
        :param requests: list of requested transactions

        :type hist: list
        :param hist: list of previous transactions
        """

        self.__value = value
        self.__owner = userID_owner
        self.__users = userID_users + [userID_owner]
        self.__subAccounts = {}
        self.__requests = []
        self.__hist = []

    def getValue(self):
        """
        Retrieves value held within bank
        """

        return self.__value

    def getOwner(self):
        """
        Retrieves owner of the bank
        """

        return self.__owner

    def getUsers(self):
        """
        Retrieves priveledged users of the bank
        """

        return self.__users

    def getSubaccounts(self):
        """
        Retrives accounts owned by this account
        """

        return self.__subAccounts

    def getHistory(self):
        """
        Retrieves history of this account
        """

        return self.__hist
