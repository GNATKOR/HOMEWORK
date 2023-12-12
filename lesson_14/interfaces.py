from lesson_14.handlers import JsonHandler, TxtHandler


class FileWorker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.handler = self.__file_type_determining()

    def __file_type_determining(self):
        types = {'json': JsonHandler, 'txt': TxtHandler}
        file_type = self.file_path.split('.')[-1]
        if file_type in types:
            return types[file_type](self.file_path)
        else:
            raise ValueError('Unsupported filetype!')

    def read(self):
        return self.handler.read()

    def close(self):
        return self.handler.close()

    def append(self, content):
        return self.handler.append(content)
