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

        Customer.__init__(self, 0 , userID)
        self.__customers = customers

    def viewRequests(self, customer):
        """
        Retrieves the requests held within the customer

        :type customer: Customer
        :param customer: Customer with requests
        """

        return customer.getRequests()
