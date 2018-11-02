class Account:
    '''
    Class that generates new instances of account
    '''
    account_details = []

    def __init__(self,username,password):
                
        self.username = username
        self.password = password
    
    def save_account(self):
        '''
        saves account objects into the account_details
        '''
        Account.account_details.append(self)
