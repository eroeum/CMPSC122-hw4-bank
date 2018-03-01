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

    def authenticate_password(self,userid,password):
        """
        Autheticates Passwords using UUID and SHA512 password hashing

        :type userid: string
        :param userid: User ID that user has chosen

        :type password: string
        :param password: Password to attempt to authenticate userid
        """

        # Encodes userid and password into utf-8 format to be hashed
        encodedUserID = (userid + self.__salt).encode('utf-8')
        encodedPassword = (password + self.__salt).encode('utf-8')

        # Hash (1-way) userid using SHA512
        hashed_userid = hasher.sha512(encodedUserID).hexdigest()

        # Detects if userid is regestered
        if(hashed_userid not in self.__approvedUsers):
            return 0

        # Hash (1-way) password using SHA512
        hashed_password = hasher.sha512(encodedPassword).hexdigest()

        # Determines if the password matches the userid
        if(self.__approvedUsers[hashed_userid] == hashed_password):
            # Returns 1 if the password has been authenticated
            return 1
        else:
            # Returns 0 if the password has not been authenticated
            return 0

    def addAutheticatedUser(self,userid,password):
        """
        Adds autheticated user using UUID and SHA512 password hashing

        :type userid: string
        :param userid: User ID that user has chosen

        :type password: string
        :param password: Password to attempt to authenticate userid
        """

        # Encodes userid and password into utf-8 format to be hashed
        encodedUserID = (userid + self.__salt).encode('utf-8')
        encodedPassword = (password + self.__salt).encode('utf-8')

        # Hash (1-way) userid using SHA512
        hashed_userid = hasher.sha512(encodedUserID).hexdigest()

        # Detects if userid is already regestered
        if(hashed_userid in self.__approvedUsers):
            return 0

        # Hash (1-way) password using SHA512
        hashed_password = hasher.sha512(encodedPassword).hexdigest()
        self.__approvedUsers[hashed_userid] = hashed_password
        return 1

    def writeEncrypted(self, filename, dest='./'):
        """
        Writes all usernames and passwords to a txt file

        :type filename: string
        :param filename: filename of txt file

        :type dest: string
        :param dest: location to write txt file
        """

        # Writes file with salt
        passFile = open(filename,'w')
        passFile.write("{}\n".format(self.__salt))

        # Writes file of encrypted data in format: <userid>:<password>
        for user in self.__approvedUsers:
            passFile.write("{}:{}\n".\
                           format(user, self.__approvedUsers[user]))
