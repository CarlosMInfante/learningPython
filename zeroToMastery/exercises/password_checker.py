#  Get the user to input their username and password. Create an output that converts the password into *'s
#  and show the total count of characters in the password
username = input('Please enter your username ')
password = input('Please enter your password ')
password_length = len(password)
hidden_password = password_length * '*'

print(f'{username}, your password {hidden_password} is {password_length} letters long.')
