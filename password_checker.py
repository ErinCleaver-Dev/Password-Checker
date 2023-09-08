import requests
import hashlib



def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    print(res)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching data from api: {res.status_code}')
    return res


def check_password_exist_api(password):
    print(password.encode('utf-8'))
    #sha1password = hashlib.sha1(password.encode('utf-8'))