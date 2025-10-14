from database import connection_db
from search_book import search_book
from borrow import borrow
from return_book import return_book
from rich.console import Console
from rich import print
console=Console()
class users():
    
    def __init__(self,user_id):
        console.print("WELCOME TO MARKAZI LIBRARY. ",style='bold magenta')
        choice='0'
        while choice!='5':
            console.print('1.Search Book',style='bold green')
            console.print('2.Borrow Book',style='bold blue1')
            console.print('3.Return book',style='bold yellow')
            console.print('4.Exit',style='bold red1')
            choice=console.input('[bold white]Enter your choice: ')
            
            match choice:
                case '1':
                    search_book()
                case '2':
                    borrow(user_id)
                    
                case '3':
                    return_book(user_id)
                case '4':
                    console.print("Exiting the system...",style='bold red1')
                    break
                