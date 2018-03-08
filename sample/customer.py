from datetime import datetime

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

    def getRequests(self):
        """
        Retrieves request of account
        """

        return self.__requests

    def _deltaValue(self, delta):
        """
        Adds or removes funds from this bank

        :type delta: float
        :param delta: Amount to add to funds
        """

        self.__value += delta
        return 1

    def requestDelta(self, delta):
        """
        Rquests the withdrawl or deposit into customer's account

        :type delta: float
        :param delta: Amount to request funds
        """

        self.__requests.append('{}~{}:Add Val:{}'.format(
                               datetime.now().replace(microsecond = 0),
                               self.__owner,
                               str(delta)))
        return 1

    def removeRequest(self, reqNum):
        """
        Removes request from request list

        :type reqNum: int
        :param reqNum: Index of request
        """

        self.__requests.pop(reqNum)
        return 1


    def addHistory(self, event):
        """
        Adds an event to the history

        :type event: string
        :param event: Event that has take place (only accepted requests)
        """

        self.__hist.append(event)
        return 1
