from auth import auth
from rich import print
from rich.console import Console
from rich.prompt import Prompt,Confirm
from rich.console import Console
console=Console()
class main():
    def __init__(self):
        console.print("Welcome to the markazi library",style='bold magenta')
        auth()      

main=main()