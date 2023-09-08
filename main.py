#https://haveibeenpwned.com/

#hackers use dictionary attacks
import password_checker

password_checker.request_api_data('CD415')
password_checker.check_password_exist_api('password1234')