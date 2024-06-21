from faltoso import Produtos_Faltosos
from colorama import Fore, Style

def relatorio_faltoso():
    opção = ''
    while opção != '2':
        print("\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~")
        print("\nO Menu de " + Fore.BLUE + "Relatório de produtos com estoque faltoso" + Style.RESET_ALL + " foi selecionado com sucesso!")
        print("\nEstas são as opções disponíveis para essa função:")
        print("1. Gerar relatórios")
        print("2. Adicionar novo produto")
        print("3. Excluir um produto")
        print("4. Editar um produto")
        print("5. Voltar")
        
        opção = input("\nPor favor, escolha uma das opções (1, 2, 3, 4 ou 5): ")

        if opção == '1':
            Produtos_Faltosos.relatar_estoque_faltoso()
        elif opção == '2':
            Produtos_Faltosos.adicionar_produto()
        elif opção == '3':
            Produtos_Faltosos.excluir_produto()
        elif opção == '4':
            Produtos_Faltosos.editar_produto()
        elif opção == '5':
            print(Fore.BLUE + "\nVoltando ao menu principal...\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Opção inválida. Tente novamente." + Style.RESET_ALL)