class User():
    def __init__(self, nome):
        self._nome = nome

    def __str__(self):
        return self._nome