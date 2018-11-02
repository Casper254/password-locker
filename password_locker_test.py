import unittest
from password_locker import Account

class TestAccount(unittest.TestCase):
    '''
    Test the Account class behaviors.
    '''
    def setUp(self):
        '''
        Set up method runs before each test case.
        '''
        self.new_account = Account('Wema','lock')

    def test_init(self):
        '''
        tests if the object is initialized properly
        '''

        self.assertEqual(self.new_account.username,'Wema')
        self.assertEqual(self.new_account.password,'lock')

    def test_save_account(self):
        '''
        tests if the account object is saved into the account_details
        '''
        self.new_account.save_account()
        self.assertEqual(len(Account.account_details),1)

if __name__ == '__main__':
    unittest.main()