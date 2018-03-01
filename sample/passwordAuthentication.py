import hashlib as hasher
import uuid

class Password:
    def __init__(self,approvedUsers):
        """
        :type approvedUsers: dict
        :param approvedUsers: List of corresponding userid, passwords
        """

        self.__salt = uuid.uuid4().hex
        self.__approvedUsers = approvedUsers
