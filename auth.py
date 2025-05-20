from database import connection_db
from admin import admin
from user import users
class auth():
    def __init__(self):
        choice ='0'
        while choice !='3':
            print('1.Sign up')
            print('2.Sign in')
            print('3.Exit')
            choice = input('please choose an option: ')
            if choice == '1':
                self.sign_up()
            elif choice == '2':
                self.sign_in()
            elif choice == '3':
                print("Exiting the system...")
                break
            else:
                print("Invalid choice, please try again.")
                
    def sign_up(self):
        cursor=connection_db()  
        print('please enter your information: ')
        username=self.isUsernameValid()
        password=self.pass_check()
        password_confirm=input('confirm your password: ')
        phone=self.isPhoneNumberTaken()
        if password==password_confirm:
            query = "INSERT INTO users (username, `password`, phone) VALUES (%s, %s, %s)" 
            cursor.execute(query, (username, password, phone))
            cursor.connection.commit()
            print('sign up successful')
    
    def sign_in(self):   
        cursor = connection_db()
        print("Enter your information: ")
        username=input('Enter your username: ') 
        password=input('Enter your password: ')
        query="select `admin`, id from users where username=%s and `password`=%s "
        cursor.execute(query , (username,password))
        user=cursor.fetchone()
        if user:
            print('Login seccsesfully. ')
            if user["admin"]==1:
                self=admin()
                
            else:
                users(user['id'])
            
    def pass_check(self):
        flag=False
        while flag!=True:
            password=input('enter your password: ')
            if len(password) < 8:
                print('password is too short')
                flag=False
            elif not any(char.isdigit() for char in password):
                print('password must contain at least one digit')
                flag=False
            elif not any(char.isupper() for char in password):
                print('password must contain at least one uppercase letter')
                flag=False
            else:
                print('password confirmed')
                flag=True
        return password
    
    def isUsernameTaken(self, username):
        cursor = connection_db()
        flag=False
        while flag!=True:
            username=username   
            query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(query, (username))
            result = cursor.fetchone()
            if result:
                print('username already taken')
                flag=False
                username = self.isUsernameValid()                
            else:
                return True
    
    def isUsernameValid(self):
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
                flag=self.isUsernameTaken(username)
                return username   
    def isPhoneNumberTaken(self):
        cursor = connection_db()
        flag=False
        phone=input("Enter your phone number: ")
        while flag !=True:
            query = 'select phone from users where phone=%s'
            cursor.execute(query , (phone))
            result=cursor.fetchone()
            if result:
                print('Number already used.')
                phone=input("Enter your phone number again: ")
                
            else:
                return phone