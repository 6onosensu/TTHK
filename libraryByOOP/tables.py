import DatabaseAccess

class Book(DatabaseAccess):
    
    def __init__(self, id, title, publication_date, author, genre):
        self.id = id
        self.title = title
        self.publication_date = publication_date
        self.author = author
        self.genre = genre
    
    def __str__(self):
        return f"Title: {self.title}, Publication date: {self.publication_date},
        Author: {self.author.name}, Genre: {self.genre.genre}"
    
    def __del__(self):
        return "The book was deleted!"
    
    def add_book(self, title, publication_date, author, genre):
        query = "INSERT INTO authors(title, publication_date, author, genre) VALUES(?, ?, ?, ?)"
        self.execute_query(query, (title, publication_date, author, genre))

class Author(DatabaseAccess):
    def __init__(self, db_path):
        super().__init__(db_path)

    def add_to(self, name, date_of_birth):
        query = "INSERT INTO authors(name, date_of_birth) VALUES(?, ?)"
        self.execute_query(query, (name, date_of_birth))
        print("Author added to the database.")

class Genre(DatabaseAccess):

    def __init__(self, id, genre):
        self.id = id
        self.genre = genre