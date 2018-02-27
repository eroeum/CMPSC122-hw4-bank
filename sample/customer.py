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
