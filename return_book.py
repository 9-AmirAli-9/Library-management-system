from database import connection_db
from rich.console import Console
from rich import print
from search_book import search_book
console=Console()
class return_book():
    def __init__(self,user_id):
        choice=0
        while choice!=4:
            console.print('1.Return book',style="bold white")
            console.print('2.Search book',style="bold white")
            console.print('3.EXIT.',style="bold yellow")
            console.print('If you dont know the book id please search.',style='bold yellow1 underline')
            choice=console.input('[bold white]enter your choice: ')
            match choice:
                case '1':
                    self.returned_book(user_id)
                case '2':
                    self.borrow_list(user_id)
                case '3':
                    break

    def borrow_list(self,user_id):
        cursor=connection_db()
        query="""select book.id,book.title,book.genre ,book.author from book
                 inner join borrow on borrow.book_id=book.id
                 where borrow.user_id = %s """
        cursor.execute(query,user_id)
        book_list=cursor.fetchall()
        console.print(book_list)

    def returned_book(self,user_id):
        cursor=connection_db()
        book_id=console.input('ENTER THE BOOK ID: ')
        console.print(book_id,style="")
        console.print(user_id,style="")
        query='insert into returned (book_id,user_id) value (%s,%s)'
        cursor.execute(query,(book_id,user_id))
        cursor.connection.commit()
        console.print('BOOK RETURNED SECCESSFULLY',style="")
        query='update book set available=1 where id=%s'
        cursor.execute(query,book_id)
        cursor.connection.commit()

