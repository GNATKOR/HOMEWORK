from lesson_14.handlers import JsonHandler, TxtHandler


class FileWorker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_type = self.__file_type_determining()

    def __file_type_determining(self):
        if self.file_path.endswith('.json'):
            return 'json'
        elif self.file_path.endswith('txt'):
            return 'txt'
        else:
            raise ValueError('Unsupported filetype!')

    def read(self):
        if self.file_type == 'json':
            result = JsonHandler(self.file_path).read()
            return result
        elif self.file_type == 'txt':
            result = TxtHandler(self.file_path).read()
            return result

    def close(self):
        if self.file_type == 'json':
            result = JsonHandler(self.file_path).close
            return result
        elif self.file_type == 'txt':
            result = TxtHandler(self.file_path).close
            return result

    def append(self, content):
        if self.file_type == 'json':
            JsonHandler(self.file_path).append(content)
            return 'Content added!'
        elif self.file_type == 'txt':
            TxtHandler(self.file_path).append(content)
