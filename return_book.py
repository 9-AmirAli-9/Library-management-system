from database import connection_db

class return_book():
    def __init__(self,user_id):
        choice=0
        while choice!=4:
            print('1.ENTER BOOK ID TO RETURN. ')
            print('2.I DONT KNOW THE NUMBER. ')
            print('3.EXIT.')
            choice=input('enter your choice: ')
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
        print(book_list)

    def returned_book(self,user_id):
        cursor=connection_db()
        book_id=input('ENTER THE BOOK ID: ')
        print(book_id)
        print(user_id)
        query='insert into returned (book_id,user_id) value (%s,%s)'
        cursor.execute(query,(book_id,user_id))
        cursor.connection.commit()
        print('BOOK RETURNED SECCESSFULLY')
        query='update book set available=1 where id=%s'
        cursor.execute(query,book_id)
        cursor.connection.commit()

