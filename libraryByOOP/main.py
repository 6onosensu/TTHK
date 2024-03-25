from LibraryApp import LibraryApp
from os import path

filename = path.abspath(__file__)
db_directory = filename.rstrip('main.py') 
db_path = path.join(db_directory, 'library.db')
app = LibraryApp(db_path)
app.run()