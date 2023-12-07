import json
from lesson_13.DataStorage import DataStorage


class DataStorageWrite(DataStorage):

    def connect(self):
        try:
            file = open(self.path, 'r+')
            self.status = "connected"
            self.content = json.load(file)
        except FileNotFoundError:
            super().connect()
            file = open(self.path, 'r+')
            self.status = "connected"
            self.content = json.load(file)

    def append(self, content):
        if self.status == "connected":
            self.content.append(content)
            with open(self.path, 'r+') as file:
                json.dump(self.content, file)
        else:
            print('Connect to the file first!')

    def disconnect(self):
        super().disconnect()
