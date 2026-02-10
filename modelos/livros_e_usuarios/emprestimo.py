from datetime import date

class Emprestimo():
    def __init__(self, livro, usuario):
        self._livro = livro
        self._usuario = usuario
        self._data = date.today()

    def __str__(self):
        return f'{self._livro} | {self._usuario} | {self._data:%d/%m/%Y}'