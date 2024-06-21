from colorama import init, Fore, Style
from submenu1 import menu_produtos
from submenu2 import relatorio_excedidos
from submenu3 import relatorio_faltoso

init()

def menu_principal():
    opção = ''
    while opção != '4':
        print("\n=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~ MENU ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=")
        print("\n" + Style.BRIGHT + Fore.BLUE + "Atenção! Estas são as opções de funcionalidade deste programa:" + Style.RESET_ALL)
        print("1. Relatório de produtos")
        print("2. Relatório de produtos com estoque excedido")
        print("3. Relatório de produtos com estoque faltoso")
        print("4. Sair")

        opção = input("\nPor favor, escolha uma opção (1, 2, 3 ou 4): ")

        if opção == '1':
            menu_produtos()
        elif opção == '2':
            relatorio_excedidos()
        elif opção == '3':
            relatorio_faltoso()
        elif opção == '4':
            print(Fore.BLUE +"\nSAINDO DO PROGRAMA... Obrigada(o) e volte sempre!"+ Style.RESET_ALL)
        else:
            print(Fore.RED + "\nOpção inválida. Tente novamente." + Style.RESET_ALL)

if __name__ == "__main__":
    menu_principal()
