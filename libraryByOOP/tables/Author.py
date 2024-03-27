from DataManager import DataManager

class Author(DataManager):
    name = ""
    def __init__(self, db_path, id=None, name=None):
        super().__init__(db_path)
        self.table_name = "authors"
        self.record_id = "author_id"
        self.id = id
        if not name:
            data = self.fetch_by_id(id)

        self.name = name or data[1]

    def create(self):
        if self.name:
            fields = {'author_name': self.name}
            self.add_record(**fields)
        else:
            print("Author name is required to add an author.")

    def update(self):
        updates = {'author_name': self.name}
        self.update_record_by_id(self.id, updates)

    def delete(self):
        self.delete_record_by_id(self.id)