from database import connection_db
from rich import print
from rich.prompt import Prompt
from rich.console import Console
console=Console()
class admin():      

    def __init__(self):
        console.print("Welcome to the Library Management System",style="bold magneta")
        choice ='0'
        while choice !='4':
            console.print('1.Add book',style="bold green")
            console.print('2.Remove book',style="bold red1")
            console.print('3.Update book',style="bold blue1")
            console.print('4.Exit',style="bold yellow")
            choice = console.input('[bold white]please choose an option: ')
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.update_book()
            elif choice == '4':
                console.print("Exiting the system...",style="bold red1")
                break
            else:
                console.print("Invalid choice, please try again.",style="bold red1")
                
    def add_book(self):
        cursor = connection_db()
        console.print("Adding a new book...",style="bold yellow1")
        title = console.input("[bold white]Enter book title: ")
        genre = console.input("[bold white]Enter book genre: ")
        author = console.input("[bold white]Enter book author: ")        
        query = "INSERT INTO book (title, genre, author) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, genre, author))
        cursor.connection.commit()
        console.print("Book added successfully!",style="bold spring_green1")
        cursor.close()
        
    def delete_book(self):
        cursor = connection_db()
        console.print("Deleting a book...",style="bold yellow1")
        book_id=console.input("[bold white]Enter the book id: ")
        query= "delete from books where id = %s"
        cursor.execute(query,book_id)
        cursor.connection.commit()
        console.print("Book deleted successfully!",style="bold spring_green1")
        cursor.close()
        
    def update_book(self):
        cursor= connection_db()
        console.print("Updating the book...",style="bold yellow1")
        choice='0'
        choice=console.input('[bold white]Enter your choice: ')
        while choice!='5':
            match choice:
                case '1':#title
                    book_id=console.input('[bold white]Enter the book id: ')
                    title=console.input('[bold white]Enter new title: ')
                    query= "update books set title = %s where `id` = %s"
                    cursor.execute(query,(title , book_id))
                    cursor.connection.commit()
                    console.print('Book updated seccessfully',style="bold spring_green1")
                    
                case '2':#authur
                    book_id=console.input('[bold white]Enter the book id: ')
                    authur=console.input('[bold white]Enter the new authur: ')
                    query = "update books set authur =%s where `id`=%s"
                    cursor.execute(query,(authur,book_id))
                    cursor.connection.commit()
                    console.print('Book updated seccessfully',style="bold spring_green1")
                    
                case '3':#published date
                    book_id=console.input('[bold white]Enter the book id: ')
                    published=console.input('[bold white]Enter new published date: ')                    
                    query= "update books set published_date=date where `id`=%s"
                    cursor.execute(query,(book_id))
                    cursor.connection.commit()
                    console.print('Book updated seccessfully',style="bold spring_green1")
                    
                case '4':#genre
                    book_id=console.input('[bold white]Enter the book id: ')
                    genre=console.input('[bold white]Enter new genre: ')
                    query= "update books set genre=%s where `id`=%s"
                    cursor.execute(query,(genre,book_id))
                    cursor.connection.commit()
                    console.print('Book updated seccessfully',style="bold spring_green1")
                    
                case '5':#exit
                    console.print('EXIT...',style="bold red1")
                    
                case _:
                    console.print('your choice is not valid',style="bold red1")
                    
        
