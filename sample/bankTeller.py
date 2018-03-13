from customer import Customer
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

    def viewCustomers(self):
        """
        Returns the customers under this account
        """

        return self.__customers

    def viewRequests(self, customer):
        """
        Retrieves the requests held within the customer

        :type customer: Customer
        :param customer: Customer with requests
        """

        return customer.getRequests()

    def acceptRequest(self, customer, reqNum):
        """
        Accepts a request for a customer

        :type customer: Customer
        :param customer: Customer with the request

        :type reqNum: int
        :param reqNum: Request number that wishes to be resolved
        """

        # All requests of customer
        requests = BankTeller.viewRequests(self, customer)

        # Checks if the reqNum exists
        if(reqNum < len(requests) and int(reqNum) == reqNum):

            # Add/Remove value to balnace
            if(requests[reqNum][149:156] == 'Add Val'):
                customer._deltaValue(float(requests[reqNum][157:]))
                customer.addHistory(requests[reqNum])
                customer.removeRequest(reqNum)

            return 1
        else:
            return 0
