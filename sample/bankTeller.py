class BankTeller(Customer):
    """
    Represents a user with mid-level priveledges
    Users having these priveledges are usually bank tellers
    """
    def __init__(self, userID, customers):
        """
        Creates the variables associated with this class

        :type userID: string
        :param userID: the owner of the account

        :type customers: list
        :param customers: all customers that can be accessed
        """

        Customer.__init__(0 , userID)
        self.__customers = customers
