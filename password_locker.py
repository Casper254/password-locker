class Account:
    '''
    Class that generates new instances of account
    '''
    account_details = []

#this function puts the info in variables
    def __init__(self,username,password):
                
        self.username = username
        self.password = password
    
#This function saves the account information
    def save_account(self):
        '''
        saves account objects into the account_details
        '''
        Account.account_details.append(self)
    
#
