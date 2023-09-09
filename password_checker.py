import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching data from api: {res.status_code}')
    return res

def get_leaked_passwords(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def check_password_exist_api(password: str):
    #must use utf8
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    five_chars, tail = sha1password[:5], sha1password[5:]
    
    response = request_api_data(five_chars)
    return get_leaked_passwords(response, tail)


def check_passwords(passwords):
    for password in passwords:
        count = check_password_exist_api(password)
        if count:
            print(f'The password: {password} was found this many times {count}.  You should change your password.')
        else:
            print(f'The password: {password} was not found: {count} in database.')
    return 'done'