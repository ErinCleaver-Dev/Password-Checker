import requests
import hashlib



def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    print(res)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching data from api: {res.status_code}')
    return res

def get_leaked_passwords(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text)
    print(hashes)
    for hash, count in hashes:
        print(hash, count)
    pass

def check_password_exist_api(password: str):
    #must use utf8
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    five_chars, tail = sha1password[:5], sha1password[5:]
    
    response = request_api_data(five_chars)
    return get_leaked_passwords(response, tail)

