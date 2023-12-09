import json


class BaseHandler:
    def read(self):
        ...

    def append(self, content):
        ...

    def close(self):
        ...


class JsonHandler(BaseHandler):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def read(self):
        self.file = open(self.file_path, 'r')
        return self.file.read()

    def append(self, content):
        with open(self.file_path, 'r') as file:
            file_content = json.load(file)
        if not isinstance(file_content, list):
            raise TypeError('Fix your JSON file. It must contains only list!')
        else:
            file = open(self.file_path, 'w')
            file_content.append(content)
            json.dump(file_content, file)

    def close(self):
        self.file.close()


class TxtHandler(BaseHandler):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def read(self):
        self.file = open(self.file_path, 'r')
        return self.file.read()

    def append(self, content):
        file = open(self.file_path, 'a')
        file.write(content)

    def close(self):
        self.file.close()
