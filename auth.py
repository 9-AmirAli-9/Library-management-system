from database import connection_db
from admin import admin
from user import users
from rich import print
from rich.prompt import Prompt
from rich.console import Console
console=Console()
class auth():
    def __init__(self):
        choice ='0'
        while choice !='3':
            console.print('1.Sign up',style="bold medium_spring_green")
            console.print('2.Sign in',style="bold bright_blue")
            console.print('3.Exit',style="bold yellow")
            choice = console.input('[bold white]Please choose an option: ')
            if choice == '1':
                self.sign_up()
            elif choice == '2':
                self.sign_in()
            elif choice == '3':
                console.print("Exiting the system...",style="bold red1")
                break
            else:
                console.print("Invalid choice, please try again.",style="bold red1")
                
    def sign_up(self):
        cursor=connection_db()  
        console.print('please enter your information: ',style="bold yellow1")
        username=self.isUsernameValid()
        password=self.pass_check()
        password_confirm=console.input('[bold white]confirm your password: ')
        phone=self.isPhoneNumberTaken()
        if password==password_confirm:
            query = "INSERT INTO users (username, `password`, phone) VALUES (%s, %s, %s)" 
            cursor.execute(query, (username, password, phone))
            cursor.connection.commit()
            console.print('sign up successful',style="bold spring_green1")
    
    def sign_in(self):   
        cursor = connection_db()
        console.print("Enter your information: ",style="bold yellow1")
        username=console.input('[bold white]Enter your username: ') 
        password=console.input('[bold white]Enter your password: ')
        query="select `admin`, id from users where username=%s and `password`=%s "
        cursor.execute(query , (username,password))
        user=cursor.fetchone()
        if user:
            console.print('Login seccsesfully. ',style="bold spring_green1")
            if user["admin"]==1:
                self=admin()
                
            else:
                users(user['id'])
        else:
            console.print('This username not found.',style="bold red1")
            
    def pass_check(self):
        flag=False
        while flag!=True:
            password=console.input('[bold white]enter your password: ')
            if len(password) < 8:
                console.print('password is too short.',style="bold red1")
                flag=False
            elif not any(char.isdigit() for char in password):
                console.print('password must contain at least one digit.',style="bold red1")
                flag=False
            elif not any(char.isupper() for char in password):
                console.print('password must contain at least one uppercase letter.',style="bold red1")
                flag=False
            else:
                console.print('password confirmed.',style="bold spring_green1")
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
                console.print('username already taken',style="bold red1")
                return False              
            else:
                return True
            
    
    def isUsernameValid(self):
        flag=False
        while flag!=True:
            username = console.input('[bold white]enter your username: ')
            if len(username) < 5:
                console.print('username is too short',style="bold red1")
                flag=False
            elif not username.isalnum():
                console.print('username must contain only letters and numbers',style="bold red1")
                flag=False
            else:
                flag=self.isUsernameTaken(username)
        return username   
    def isPhoneNumberTaken(self):
        cursor = connection_db()
        flag=False
        phone=console.input("[bold white]Enter your phone number: ")
        while flag !=True:
            query = 'select phone from users where phone=%s'
            cursor.execute(query , (phone))
            result=cursor.fetchone()
            if result:
                console.print('Number already used.',style="bold red1")
                phone=console.input("[bold white]Enter your phone number again: ")
                
            else:
                return phone