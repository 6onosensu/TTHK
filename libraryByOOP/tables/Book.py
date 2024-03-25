from DataManager import DataManager

class Book(DataManager):
    def __init__(self, db_path, id, name=None, num_of_pages=None, author_id=None, genre_id=None):
        super().__init__(db_path)
        self.id = id
        if not name:
            data = self.fetch_records("books", ("id", id))[0]

        self.name = name or data.name
        self.num_of_pages = num_of_pages or data.num_of_pages
        self.author_id = author_id or data.author_id
        self.genre_id = genre_id or data.genre_id
    
    def show_books(self):
        self.show_all_records(self, "books")

    def add_book(self):
        fields = {
            'title': self.name, 
            'num_of_pages': self.num_of_pages, 
            'author_id': self.author_id, 
            'genre_id': self.genre_id
        }
        self.add_record("books", **fields)
    
    def update(self):
        updates = {
            'title': self.name,
            'num_of_pages': self.num_of_pages,
            'author_id': self.author_id,
            'genre_id': self.genre_id
        }
        self.update_record_by_id("books", self.id, updates)
