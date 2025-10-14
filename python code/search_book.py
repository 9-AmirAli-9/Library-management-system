from database import connection_db

class search_book():
    def __init__(self):
        choice='0'
        while choice!='5':
            print("1.Search by title: ")
            print("2.Search by author: ")
            print("3.Search by genre: ")
            print("4.Search by published date: ")
            print("5.exit")
            choice=input('Enter your choice: ')

            match choice:
                case '1':
                    self.search_title()
                case '2':
                    self.search_author()
                    
                case '3':
                    self.search_genre()
                    
                case '4':
                    self.search_published_date()

                case '5':
                    print("Exiting the system...")
                    break

    def search_title(self):
        cursor=connection_db()
        book_title=input("enter your book title: ")
        query = "select * from book where  title like %s "
        book_title = '%' + book_title + '%'
        cursor.execute(query,book_title)
        book=cursor.fetchall()
        for book in book:
            print(book)
        cursor.close()
    
    def search_author(self):
        cursor=connection_db()
        book_author=input("enter your book author: ")
        query = "select * from book where  author like %s "
        book_author = '%' + book_author + '%'
        cursor.execute(query,book_author)
        book=cursor.fetchall()
        for book in book:
            print(book)
        cursor.close()
    
    def search_genre(self):
        cursor=connection_db()
        book_genre=input("enter your book genre: ")
        query = "select * from book where  genre like %s "
        book_genre = '%' + book_genre + '%'
        cursor.execute(query,book_genre)
        book=cursor.fetchall()
        for book in book:
            print(book)
        cursor.close()
    
    def search_published_date(self):
        cursor=connection_db()
        book_published_date=input("enter your book published_date: ")
        query = "select * from book where  published_date like %s "
        book_published_date = '%' + book_published_date + '%'
        cursor.execute(query,book_published_date)
        book=cursor.fetchall()
        for book in book:
            print(book)
        cursor.close()