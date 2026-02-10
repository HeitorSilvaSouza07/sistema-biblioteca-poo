from modelos.biblioteca import Biblioteca
from modelos.livros_e_usuarios.livro import Livro
from modelos.livros_e_usuarios.user import User
from modelos.livros_e_usuarios.emprestimo import Emprestimo

def main():
    biblioteca = Biblioteca()
    usuario1 = User('Heitor')
    livro1 = Livro('It a coisa')
    livro2 = Livro('Entendendo algoritmos')
    livro3 = Livro('Her')
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)
    biblioteca.emprestar_livro_ao_usuario(usuario1, livro1)
    biblioteca.listar_emprestimos()
    biblioteca.listar_livros()

if __name__ == '__main__':
    main()