from produtos import Produtos
from colorama import Fore, Style

def menu_produtos():
    opção = ''
    while opção != '5':
        print("\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~")
        print("\nO Menu de " + Fore.BLUE + "Relatório de produtos" + Style.RESET_ALL + " foi selecionado com sucesso!")
        print("\nEstas são as opções disponíveis para essa função:")
        print("1. Gerar relatório de produtos")
        print("2. Adicionar novo produto")
        print("3. Excluir um produto")
        print("4. Editar um produto")
        print("5. Voltar")

        opção = input("\nPor favor, escolha uma opção (1, 2, 3, 4 ou 5): ")

        if opção == '1':
            Produtos.relatar_produtos()
        elif opção == '2':
            Produtos.adicionar_produto()
        elif opção == '3':
            Produtos.excluir_produto()
        elif opção == '4':
            Produtos.editar_produto()
        elif opção == '5':
            print(Fore.BLUE + "\nVoltando ao menu principal...\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + "\nOpção inválida. Tente novamente.\n" + Style.RESET_ALL)

if __name__ == "__main__":
    menu_produtos()

