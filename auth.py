import json

def get_credentials():
    username = input('Enter your username: ')
    password = input(f'Enter your password {username}: ')

    return username, password

def write_passwdb(passwd):
    with open('passwd.json', 'w') as pwdb_file:
        json.dump(pwdb, pwdb_file)


if __name__ == '__main__':
    username, password = get_credentials()
    pwdb = {username: password}
    write_passwdb(pwdb)
