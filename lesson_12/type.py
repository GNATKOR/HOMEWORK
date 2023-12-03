from lesson_12.move import Moving


class Animal(Moving):
    def voice(self):
        raise NotImplementedError(
            'Define voice in %s.' % self.__class__.__name__
        )


class Transport(Moving):
    def launch(self):
        raise NotImplementedError(
            'Define launch in %s.' % self.__class__.__name__
        )

