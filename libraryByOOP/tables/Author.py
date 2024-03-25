from DataManager import DataManager

class Author(DataManager):
    def __init__(self, db_path, id, name=None):
        super().__init__(db_path)
        self.id = id
        if not name:
            data = self.fetch_records("authors", ("id", id))[0]

        self.name = name or data.name

    def show_authors(self):
        self.show_all_records(self, "authors")

    def add_author(self):
        fields = {
            'author_name': self.name
        }
        self.add_record("authors", **fields)

    def update(self):
        updates = {
            'author_name': self.name
        }
        self.update_record_by_id("authors", self.id, updates)
