from DataManager import *

class Genre(DataManager):
    def __init__(self, db_path, id, name=None):
        super().__init__(db_path)
        self.table_name = "genres"
        self.id = id
        if not name:
            data = self.fetch_records(("id", id))[0]

        self.name = name or data.name

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