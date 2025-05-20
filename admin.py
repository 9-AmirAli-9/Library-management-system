from database import connection_db

class admin():      

    def __init__(self):
        print("Welcome to the Library Management System")
        choice ='0'
        while choice !='4':
            print('1.Add book')
            print('2.Remove book')
            print('3.Update book')
            print('4.Exit')
            choice = input('please choose an option: ')
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.update_book()
            elif choice == '4':
                print("Exiting the system...")
                break
            else:
                print("Invalid choice, please try again.")
                
    def add_book(self):
        cursor = connection_db()
        print("Adding a new book...")
        title = input("Enter book title: ")
        genre = input("Enter book genre: ")
        author = input("Enter book author: ")        
        query = "INSERT INTO book (title, genre, author) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, genre, author))
        cursor.connection.commit()
        print("Book added successfully!")
        cursor.close()
        
    def delete_book(self):
        cursor = connection_db()
        print("Deleting a book...")
        book_id=input("Enter the book id: ")
        query= "delete from books where id = %s"
        cursor.execute(query,book_id)
        cursor.connection.commit()
        print("Book deleted successfully!")
        cursor.close()
        
    def update_book(self):
        cursor= connection_db()
        print("Updating the book...")
        choice='0'
        choice=input('Enter your choice: ')
        while choice!='5':
            match choice:
                case '1':#title
                    book_id=input('Enter the book id: ')
                    title=input('Enter new title: ')
                    query= "update books set title = %s where `id` = %s"
                    cursor.execute(query,(title , book_id))
                    cursor.connection.commit()
                    print('Book updated seccessfully')
                    
                case '2':#authur
                    book_id=input('Enter the book id: ')
                    authur=input('Enter the new authur: ')
                    query = "update books set authur =%s where `id`=%s"
                    cursor.execute(query,(authur,book_id))
                    cursor.connection.commit()
                    print('Book updated seccessfully')
                    
                case '3':#published date
                    book_id=input('Enter the book id: ')
                    published=input('Enter new published date: ')                    
                    query= "update books set published_date=date where `id`=%s"
                    cursor.execute(query,(book_id))
                    cursor.connection.commit()
                    print('Book updated seccessfully')
                    
                case '4':#genre
                    book_id=input('Enter the book id: ')
                    genre=input('Enter new genre: ')
                    query= "update books set genre=%s where `id`=%s"
                    cursor.execute(query,(genre,book_id))
                    cursor.connection.commit()
                    print('Book updated seccessfully')
                    
                case '5':#exit
                    print('EXIT...')
                    
                case _:
                    print('your choice is not valid')
                    
        
