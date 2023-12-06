class Moving:
    def move(self):
        raise NotImplementedError(
            'Define move in %s.' % self.__class__.__name__
        )

