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
