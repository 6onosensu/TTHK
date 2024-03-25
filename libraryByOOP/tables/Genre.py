from DataManager import *

class Genre(DataManager):
    def __init__(self, db_path, id, name=None):
        super().__init__(db_path)
        self.id = id
        if not name:
            data = self.fetch_records("genres", ("id", id))[0]

        self.name = name or data.name

    def show_genres(self):
        self.show_all_records(self, "genres")

    def add_genre(self):
        fields = {
            'genre_name': self.name
        }
        self.add_record("genres", **fields)

    def update(self):
        updates = {
            'genre_name': self.name
        }
        self.update_record_by_id("genres", self.id, updates)