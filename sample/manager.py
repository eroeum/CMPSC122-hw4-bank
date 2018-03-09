class Manager(Assistant):
    """
    Represents a user with high-level priveledges
    Users having these priveledges are usually managers
    """
    def __init__(self, userID, customers, bankTellers, assistants):
        """
        Creates the variables associated with this class

        :type userID: string
        :param userID: the owner of the account

        :type customers: list
        :param customers: all customers that can be accessed

        :type bankTellers: list
        :param bankTellers: all bank tellers that can be accessed

        :type assistants: list
        :param assistants: all assistants that can be accessed
        """

        Assistant.__init__(self, userID, customers, bankTellers)
        self.__assistants = assistants

    def viewAssistants(self):
        """
        Returns the assistants under this class
        """

        return self.__assistants
