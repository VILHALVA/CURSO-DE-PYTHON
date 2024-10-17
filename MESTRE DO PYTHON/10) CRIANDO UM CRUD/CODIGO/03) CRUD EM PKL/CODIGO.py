import os
import pickle
from time import sleep

class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class GerenciadorUsuarios:
    def __init__(self):
        self.arquivo = os.path.join(os.path.dirname(__file__), 'usuarios.pkl')
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'wb'):
                pass  

    def adicionar_usuario(self, nome, idade):
        usuario = Usuario(nome, idade)
        with open(self.arquivo, 'ab') as f:
            pickle.dump(usuario, f)
        print("😎USUÁRIO ADICIONADO COM SUCESSO!")

    def listar_usuarios(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'rb') as f:
                print("=" *100)
                print("LISTA DE USUÁRIOS:")
                print("-" *100)
                try:
                    while True:
                        usuario = pickle.load(f)
                        print("*" *100)
                        print(f"NOME: {usuario.nome}, IDADE: {usuario.idade}")
                        print("*" *100)
                except EOFError:
                    pass
                print("=" *100)
        else:
            print("😒NENHUM USUÁRIO CADASTRADO.")

    def atualizar_usuario(self, nome_antigo, novo_nome, nova_idade):
        with open(self.arquivo, 'rb') as f:
            usuarios = []
            try:
                while True:
                    usuario = pickle.load(f)
                    if usuario.nome == nome_antigo:
                        usuario.nome = novo_nome
                        usuario.idade = nova_idade
                    usuarios.append(usuario)
            except EOFError:
                pass

        with open(self.arquivo, 'wb') as f:
            for usuario in usuarios:
                pickle.dump(usuario, f)
        print("😙USUÁRIO ATUALIZADO COM SUCESSO!")

    def excluir_usuario(self, nome):
        with open(self.arquivo, 'rb') as f:
            usuarios = []
            try:
                while True:
                    usuario = pickle.load(f)
                    if usuario.nome != nome:
                        usuarios.append(usuario)
            except EOFError:
                pass

        with open(self.arquivo, 'wb') as f:
            for usuario in usuarios:
                pickle.dump(usuario, f)
        print("🗑USUÁRIO EXCLUÍDO COM SUCESSO!")

def exibir_menu():
   print("\nMENU:")
   print("1. ADICIONAR USUÁRIO")
   print("2. LISTAR USUÁRIOS")
   print("3. ATUALIZAR USUÁRIO")
   print("4. EXCLUIR USUÁRIO")
   print("5. SAIR")

def main():
    gerenciador = GerenciadorUsuarios()

    while True:
        exibir_menu()
        opcao = input("😎ESCOLHA UMA OPÇÃO:\n>>>")

        if opcao == "1":
            nome = input("😎DIGITE O NOME:\n>>>")
            idade = input("😎DIGITE A IDADE:\n>>>")
            gerenciador.adicionar_usuario(nome, idade)
        elif opcao == "2":
            gerenciador.listar_usuarios()
        elif opcao == "3":
            nome_antigo = input("😎DIGITE O NOME A SER ATUALIZADO:\n>>>")
            novo_nome = input("😎DIGITE O NOVO NOME:\n>>>")
            nova_idade = input("😎DIGITE A NOVA IDADE:\n>>>")
            gerenciador.atualizar_usuario(nome_antigo, novo_nome, nova_idade)
        elif opcao == "4":
            nome = input("😎DIGITE O NOME DO USUÁRIO A SER EXCLUÍDO:\n>>>")
            gerenciador.excluir_usuario(nome)
        elif opcao == "5":
            print("🚀SAINDO...")
            sleep(3)
            break
        else:
            print("😡OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()
