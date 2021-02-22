# 8 characters long
# contain any sort of letters, numbers and $%#@
import re


pattern = re.compile(r"(^[A-Za-z\d@$%#@]{8,}$)")

password = []

def validator_function():
    string = input('Enter a password. It can contain letters, numbers and/or $ % # @ and must be more then 8 characters long: ')
    validation = pattern.search(string)
    if validation == None:
        print('-> Please use letters, numbers or $ % # @ and it has to be more then 8 characters long!')
        validator_function()
    else:
        password.append(string)


validator_function()
print(f'This is your password: {password}')


