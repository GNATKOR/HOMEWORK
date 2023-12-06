import json


class DataStorage:
    @property
    def path(self):
        return self.__path

    def __init__(self):
        path = '/Users/korshun/PY94/HOMEWORK/lesson_13/DataBase.json'
        self.__path = path
        self.status = "disconnected"
        self.content = None

    def _create_storage(self):
        with open(self.__path, 'w') as file:
            json.dump([], file)
            return file

    def connect(self):
        try:
            file = open(self.__path, 'r')
            self.status = "connected"
            self.content = json.load(file)
        except FileNotFoundError:
            self._create_storage()
            file = open(self.__path, 'r')
            self.status = "connected"
            self.content = json.load(file)

    def disconnect(self):
        file = open(self.__path, 'r')
        file.close()
        self.status = "disconnected"
        print('File closed.')
