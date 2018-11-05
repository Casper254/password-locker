class Account:
    '''
    Class that generates new instances of account
    '''
    account_list = []

#this function puts the info in variables
    def __init__(self,username,password, email):
                
        self.username = username
        self.password = password
        self.email = email
    
#This function saves the account information
    def save_account(self):
        '''
        saves account objects into the account_details
        '''
        Account.account_list.append(self)

    def delete_account(self):
        '''
        this method deletes a saved account from the account list
        '''
        Account.account_list.remove(self)

    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args: 
            email address: email address to search for
        Returns:
            password that matches the email address.
        '''

        for address in cls.account_list:
            if address.email == email:
                return address
    
    @classmethod
    def account_exist(cls, email):
        '''
        method that checks if an account exists from the contact list.
        '''
        for  account in cls.account_list:
            if account.email == email:
                return True

        return False

    @classmethod
    def display_account(cls):
        '''
        method that returns the contact list
        '''
        return cls.account_list
