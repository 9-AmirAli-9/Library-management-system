from database import connection_db
from search_book import search_book
from borrow import borrow
from return_book import return_book
class users():
    
    def __init__(self,user_id):
        print("WELCOME TO MARKAZI LIBRARY. ")
        choice='0'
        while choice!='5':
            print('1.Search Book')
            print('2.Borrow Book')
            print('3.Return book')
            print('4.Exit')
            choice=input('Enter your choice: ')
            
            match choice:
                case '1':
                    search_book()
                case '2':
                    borrow(user_id)
                    
                case '3':
                    return_book(user_id)
                case '4':
                    print("Exiting the system...")
                    break
                