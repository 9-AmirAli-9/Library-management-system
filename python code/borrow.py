from database import connection_db
from search_book import search_book
from rich.prompt import Prompt,Confirm
from rich.console import Console
from rich import print
console=Console()
class borrow():

    def __init__(self,user_id):
        choice=0
        while choice!=3: 
            console.print('1.borrow book',style='bold white')
            console.print('2.search book',style='bold white')
            console.print('3.Exit',style='bold yellow')
            console.print('note:if you dont know book id please search the book',style='bold yellow1 underline')
            choice=console.input('[bold white]enter your choice:')
            match choice:
                case '1':
                    book_id=console.input('[bold white]enter book id: ')
                    self.borrow_book(book_id,user_id)
                case '2':
                    search_book(self)
                case '3':
                    break

    def borrow_book(self,book_id,user_id):
        cursor=connection_db()
        book_id=int(book_id)
        query=" select * from book where id = %s "
        cursor.execute(query,book_id)
        book=cursor.fetchone()
        # tableeeeeeeeee
        console.print(book)
        choice='0'
        choice=console.input("[bold white]DO YOU WANT THIS BOOK?[/bold white]")
        print(choice)
        if choice=='y' or choice=='yes': 
            if book['available']==1:
                query='insert into borrow (book_id,user_id) value (%s,%s)'
                cursor.execute(query,(book_id,user_id))
                cursor.connection.commit()
                console.print('BOOK BORROWED SUCCESSFULLY.',style='bold spring_green1')
                query='update book set available=0 where id=%s'
                cursor.execute(query,book_id)
                cursor.connection.commit()
            else:
                console.print('THIS BOOK IS NOT AVAILABLE.\nPLEASE SELECT ANOTHER BOOK.',style='bold red1')
        
        else:
            print('nashod')
            return  