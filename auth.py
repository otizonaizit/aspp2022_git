def get_credentials():
    username = input('Enter your username: ')
    password = input(f'Enter your password {username}: ')

    return username, password

if __name__ == '__main__':
    get_credentials()
