#https://haveibeenpwned.com/
import sys
#hackers use dictionary attacks
import password_checker
import pathlib

filepath = pathlib.Path(__file__).parent / 'passwords.txt'


passwords = []
try:
    with open(filepath, 'r') as my_password_file:
        if(filepath.stat().st_size == 0):
            print('No passwords found')
        else:
            for password in my_password_file.readlines():
                passwords.append(password.strip())
except:
    print('No passwords found')


print(password_checker.check_passwords(passwords))

