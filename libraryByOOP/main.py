from LibraryApp import LibraryApp
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_directory, 'library.db')
app = LibraryApp(db_path)
app.run()

"""
filename = path.abspath(__file__)
db_directory = filename.rstrip('main.py') 
db_path = path.join(db_directory, 'library.db')
app = LibraryApp(db_path)
app.run()
"""
