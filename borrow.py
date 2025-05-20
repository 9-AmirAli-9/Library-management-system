from database import connection_db
from search_book import search_book
class borrow():

    def __init__(self,user_id):
        choice=0
        while choice!=3: 
            print('1.enter book id for borrow')
            print('2.if you dont know book id please search the book')
            print('Exit')
            choice=input('enter your choice:')
            match choice:
                case '1':
                    book_id=input('enter book id: ')
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
        print(book)
        choice=0
        choice=input('YOU WANT THIS BOOK:\n1.YES\n2.NO')
        if choice=='1': 
            if book['available']==1:
                query='insert into borrow (book_id,user_id) value (%s,%s)'
                cursor.execute(query,(book_id,user_id))
                cursor.connection.commit()
                print('BOOK BORROWED SUCCESSFULLY.')
                query='update book set available=0 where id=%s'
                cursor.execute(query,book_id)
                cursor.connection.commit()
            else:
                print('THIS BOOK IS NOT AVAILABLE.\nPLEASE SELECT ANOTHER BOOK.')
        else:
            return