from .models import User
        
def isUsernameValid(username):
    flag=False
    while flag!=True:
        username = input('enter your username: ')
        if len(username) < 5:
            print('username is too short')
            flag=False
        elif not username.isalnum():
            print('username must contain only letters and numbers')
            flag=False
        else:
            flag=isUsernameTaken(username)
    return username

def isUsernameTaken(username):        
    user = User.objects.filter(username=username).first()
    if user:
        print('username already taken')
        return False
    return True

def pass_check(self):
    flag=False
    while flag!=True:
        password=input('enter your password: ')
        if len(password) < 8:
            print('password is too short.')
            flag=False
        elif not any(char.isdigit() for char in password):
            print('password must contain at least one digit.')
            flag=False
        elif not any(char.isupper() for char in password):
            print('password must contain at least one uppercase letter.')
            flag=False
        else:
            print('password confirmed.')
            flag=True
    return password
    
def isPhoneNumberTaken(self):
    
    flag=False
    phone=input("Enter your phone number: ")
    while flag !=True:
        result=User.objects.filter(phone=phone).first()
        if result:
            print('Number already used.')
            phone=input("Enter your phone number again: ")

        else:
            return phone