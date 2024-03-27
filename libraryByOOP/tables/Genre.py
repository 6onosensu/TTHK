from DataManager import *

class Genre(DataManager):
    def __init__(self, db_path, id, name=None):
        super().__init__(db_path)
        self.table_name = "genres"
        self.record_id = "genre_id"
        self.id = id
        if not name:
            data = self.fetch_by_id(id)

        self.name = name or data[1]

    def create(self):
        fields = {
            'genre_name': self.name
        }
        self.add_record(**fields)

    def update(self):
        updates = {
            'genre_name': self.name
        }
        self.update_record_by_id(self.id, updates)

    def delete(self):
        self.delete_record_by_id(self.id)