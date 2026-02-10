from modelos.livros_e_usuarios.livro import Livro
from modelos.livros_e_usuarios.user import User
from modelos.livros_e_usuarios.emprestimo import Emprestimo

class Biblioteca():
    def __init__(self):
        self._usuarios = []
        self._livros = []
        self._emprestimos = []

    def adicionar_user(self, nome):
        usuario = User(nome)
        self._usuarios.append(usuario)
    
    def adicionar_livro(self, nome):
        livro = Livro(nome)
        self._livros.append(livro)

    def listar_livros(self):
        print('Lista de livros: \n')
        for livros in self._livros:
            print(f'{livros._nome} | {livros._disponivel}')

    def listar_emprestimos(self):
        print('Lista de empretimos: \n')
        for emprestimo in self._emprestimos:
            print(emprestimo)
    
    def emprestar_livro_ao_usuario(self, usuario, livro):

        if livro._disponivel:
            emprestimo = Emprestimo( livro, usuario)
            livro._disponivel = not livro._disponivel
            self._emprestimos.append(emprestimo)
            print('Emprestimo concluido\n')

        else:
            print('Emprestimo negado')

    