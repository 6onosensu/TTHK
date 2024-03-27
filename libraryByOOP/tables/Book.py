from DataManager import DataManager

class Book(DataManager):
    def __init__(self, db_path, id, name=None, num_of_pages=None, author_id=None, genre_id=None):
        super().__init__(db_path)
        self.table_name = "books"
        self.record_id = "book_id"
        self.id = id
        if not name:
            data = self.fetch_by_id(id)
        
        self.name = name or data[1]
        
        self.num_of_pages = num_of_pages or data[2]
        self.author_id = author_id or data[3]
        self.genre_id = genre_id or data[5]

    def create(self):
        fields = {
            'title': self.name, 
            'num_of_pages': self.num_of_pages, 
            'author_id': self.author_id, 
            'genre_id': self.genre_id
        }
        self.add_record(**fields)
    
    def update(self):
        updates = {
            'title': self.name,
            'num_of_pages': self.num_of_pages,
            'author_id': self.author_id,
            'genre_id': self.genre_id
        }
        self.update_record_by_id(self.id, updates)
    
    def delete(self):
        self.delete_record_by_id(self.id)