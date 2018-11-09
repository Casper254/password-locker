from password_locker import Account

def main():
    print('What would you like to do?')

    while True:
        print('Use these short codes : ca - create a new account, da - delete account, fa - recover password')

        short_code = input().lower()

        if short_code == 'ca':
            print('New Account')
            print('-'*10)

            print('New username....')
            username = input()

            print('Enter password')
            password = input()

            print('Enter email address')
            email = input()

            save_account(create_account(username,password,email))
            print('\n')
            print(f'New account {username} ')
            
            print ('\n')

        elif short_code == 'da':
            
            if display_account():
                print('Heres a list of all your Accounts')
                print('\n')

                for Account in display_account(): 
                    print(f'{Account.username}....{Account.email}')
                    print('\n')

            else:
                print('\n')
                print('Your account list is empty')
        
        elif short_code == 'fa':
            print('Enter your email address')
            search_email = input()

            if check_existing_account(search_email):
                search_account = find_account(search_email)
                print(f'Password....{search_account.password}')

            else:
                print('This account does not exist')

        elif short_code == 'ex':
            print('Signing out.....')
            break
        else:
            print('What was that? Please use the short codes')

def create_account(username, password, email):
    '''
    function that creats a new account
    '''
    new_account = Account(username, password, email)
    return new_account

def save_account(Account):
    '''
    function to save account
    '''
    Account.save_account()

def del_account(Account):
    '''
    Function to delete an account
    '''
    Account.delete_account()

def find_account(email):
    '''
    Function that finds an account by email and returns the account info
    '''
    return Account.find_by_email(email)

if __name__ == '__main__':
    main()
