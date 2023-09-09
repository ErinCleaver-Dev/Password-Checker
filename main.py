#https://haveibeenpwned.com/
import sys
#hackers use dictionary attacks
import password_checker

print(password_checker.check_passwords(sys.argv[1:]))

