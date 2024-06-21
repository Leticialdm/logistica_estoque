from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
from colorama import Fore, Style

class Produtos_Excedidos:
    @staticmethod
    def relatar_estoque_excedido():
        client = MongoClient('mongodb://localhost:27017/')
        db = client['Logistica_de_Estoque']
        produtos_colecao = db['produtos']

        query = {
            "$expr": { "$gt": ["$estoque_atual", "$quantidade_estoque_maximo"] }
        }

        produtos_encontrados = produtos_colecao.find(query)
        
        produtos_excesso_estoque = []

        for produto in produtos_encontrados:
            excesso_estoque = produto['estoque_atual'] - produto['quantidade_estoque_maximo']
            produto['excesso_estoque'] = excesso_estoque
            produtos_excesso_estoque.append(produto)

        produtos_ordenados = sorted(produtos_excesso_estoque, key=lambda x: x['excesso_estoque'], reverse=True)

        print(Fore.GREEN + "\nEstes são os produtos com estoque excedido:" + Style.RESET_ALL)
        for produto in produtos_ordenados:
            valor_estoque_excesso = produto['excesso_estoque'] * produto['preco_medio_custo']

            print(f"{Fore.MAGENTA}-_id:{Style.RESET_ALL} {produto['_id']}, {Fore.MAGENTA}Nome:{Style.RESET_ALL} {produto['nome']}, {Fore.MAGENTA}Quantidade em estoque:{Style.RESET_ALL} {produto['estoque_atual']}, {Fore.MAGENTA}Quantidade de estoque máximo:{Style.RESET_ALL} {produto['quantidade_estoque_maximo']}, {Fore.MAGENTA}Preço médio de custo:{Style.RESET_ALL} R${produto['preco_medio_custo']:.2f}, {Fore.MAGENTA}Excesso de estoque:{Style.RESET_ALL} {produto['excesso_estoque']}, {Fore.MAGENTA}Valor do estoque em excesso:{Style.RESET_ALL} R$ {valor_estoque_excesso:.2f}")
            print('__________________________________________________________________________________')

        print(Fore.BLUE + "\nVoltando ao menu Relatório de produtos com estoque excedido..." + Style.RESET_ALL)

        client.close()
    
    def adicionar_produto():
        client = MongoClient('mongodb://localhost:27017/')
        db = client['Logistica_de_Estoque']
        produtos_colecao = db['produtos']

        print('__________________________________________________________________________________')        
        print(Style.BRIGHT + Fore.GREEN + "\nAdicionando um novo produto nas condições de:" + Style.RESET_ALL)
        print("-Estoque atual excedendo o estoque máximo")

        nome = input("\n-Digite o nome do produto: ")
        data_fabricacao = input("-Digite a data de fabricação (YYYY-MM-DD): ")
        data_validade = input("-Digite a data de validade (YYYY-MM-DD): ")
        lote = input("-Digite o lote do produto: ")
        escaninho_id = input("-Digite o ID do escaninho: ")
        preco_medio_custo = float(input("-Digite o preço médio de custo: "))
        data_ultima_compra = input("-Digite a data da última compra (YYYY-MM-DD): ")
        quantidade_estoque_minimo = int(input("-Digite a quantidade mínima de estoque: "))
        quantidade_estoque_maximo = int(input("-Digite a quantidade máxima de estoque: "))
        data_ultima_movimentacao = input("-Digite a data da última movimentação (YYYY-MM-DD): ")
        estoque_atual = int(input("-Digite a quantidade atual em estoque: "))
        preco_unitario = float(input("-Digite o preço unitário: "))

        novo_produto = {
            "nome": nome,
            "data_fabricacao": datetime.strptime(data_fabricacao, "%Y-%m-%d"),
            "data_validade": datetime.strptime(data_validade, "%Y-%m-%d"),
            "lote": lote,
            "escaninho_id": escaninho_id,
            "preco_medio_custo": preco_medio_custo,
            "data_ultima_compra": datetime.strptime(data_ultima_compra, "%Y-%m-%d"),
            "quantidade_estoque_minimo": quantidade_estoque_minimo,
            "quantidade_estoque_maximo": quantidade_estoque_maximo,
            "data_ultima_movimentacao": datetime.strptime(data_ultima_movimentacao, "%Y-%m-%d"),
            "estoque_atual": estoque_atual,
            "preco_unitario": preco_unitario
        }
        produtos_colecao.insert_one(novo_produto)
        resultado = produtos_colecao.insert_one(novo_produto)

        print("__________________________________________________________________________________")
        print(Fore.GREEN +f"\nProduto adicionado com sucesso! ID do produto: {resultado.inserted_id}" + Style.RESET_ALL)
        print("__________________________________________________________________________________")
        print(Fore.BLUE + "\nVoltando ao menu Relatório de produtos...\n" + Style.RESET_ALL)

        client.close()

    from pymongo import MongoClient

    def adicionar_produto():
        client = MongoClient('mongodb://localhost:27017/')
        db = client['Logistica_de_Estoque']
        produtos_colecao = db['produtos']

        print('__________________________________________________________________________________')        
        print(Style.BRIGHT + Fore.GREEN + "\nAdicionando um novo produto nas condições de:" + Style.RESET_ALL)
        print("-Estoque atual excedendo o estoque máximo")

        nome = input("\n-Digite o nome do produto: ")
        data_fabricacao = input("-Digite a data de fabricação (YYYY-MM-DD): ")
        data_validade = input("-Digite a data de validade (YYYY-MM-DD): ")
        lote = input("-Digite o lote do produto: ")
        escaninho_id = input("-Digite o ID do escaninho: ")
        preco_medio_custo = float(input("-Digite o preço médio de custo: "))
        data_ultima_compra = input("-Digite a data da última compra (YYYY-MM-DD): ")
        quantidade_estoque_minimo = int(input("-Digite a quantidade mínima de estoque: "))
        quantidade_estoque_maximo = int(input("-Digite a quantidade máxima de estoque: "))
        data_ultima_movimentacao = input("-Digite a data da última movimentação (YYYY-MM-DD): ")
        estoque_atual = int(input("-Digite a quantidade atual em estoque: "))
        preco_unitario = float(input("-Digite o preço unitário: "))

        novo_produto = {
            "\n-nome": nome,
            "-data_fabricacao": datetime.strptime(data_fabricacao, "%Y-%m-%d"),
            "-data_validade": datetime.strptime(data_validade, "%Y-%m-%d"),
            "-lote": lote,
            "-escaninho_id": escaninho_id,
            "-preco_medio_custo": preco_medio_custo,
            "-data_ultima_compra": datetime.strptime(data_ultima_compra, "%Y-%m-%d"),
            "-quantidade_estoque_minimo": quantidade_estoque_minimo,
            "-quantidade_estoque_maximo": quantidade_estoque_maximo,
            "-data_ultima_movimentacao": datetime.strptime(data_ultima_movimentacao, "%Y-%m-%d"),
            "-estoque_atual": estoque_atual,
            "-preco_unitario": preco_unitario
        }

        resultado = produtos_colecao.insert_one(novo_produto)

        print("__________________________________________________________________________________")
        print(Fore.GREEN + f"Produto adicionado com sucesso! ID do produto: {resultado.inserted_id}" + Style.RESET_ALL)
        print("__________________________________________________________________________________")
        print(Fore.BLUE + "\nVoltando ao menu Relatório de produtos...\n" + Style.RESET_ALL)

        client.close()

    def excluir_produto():
        client = MongoClient('mongodb://localhost:27017/')
        db = client['Logistica_de_Estoque']
        produtos_colecao = db['produtos']

        print("__________________________________________________________________________________")
        print(Style.BRIGHT + Fore.RED + "\nExcluir produto nas condições de:" + Style.RESET_ALL)
        print("-Estoque atual excedendo o estoque máximo")
        produto_id = input(Fore.MAGENTA + "\n- Digite o ID do produto a ser excluído: " + Style.RESET_ALL)

        try:
            object_id = ObjectId(produto_id)
            resultado = produtos_colecao.delete_one({"_id": object_id})

            if resultado.deleted_count > 0:
                print("__________________________________________________________________________________")
                print(Fore.GREEN + f"\nProduto com ID {produto_id} excluído com sucesso!" + Style.RESET_ALL)
                print("__________________________________________________________________________________")
            else:
                print("__________________________________________________________________________________")
                print(Fore.RED + f"\nProduto com ID {produto_id} não encontrado." + Style.RESET_ALL)
                print("__________________________________________________________________________________")

        except Exception as e:
            print("__________________________________________________________________________________")
            print(Fore.RED + f"\nErro ao excluir o produto: {e}" + Style.RESET_ALL)
            print("__________________________________________________________________________________")

        print(Fore.BLUE + "\nVoltando ao menu Relatório de produtos..." + Style.RESET_ALL)

        client.close()

    def editar_produto():
        client = MongoClient('mongodb://localhost:27017/')
        db = client['Logistica_de_Estoque']
        produtos_colecao = db['produtos']

        print("__________________________________________________________________________________")
        print(Style.BRIGHT + Fore.GREEN + "\nEditando um novo produto nas condições de:" + Style.RESET_ALL)
        print("-Estoque atual excedendo o estoque máximo")
        
        produto_id = input("\n- Digite o ID do produto a ser editado: ")

        try:
            object_id = ObjectId(produto_id)
            produto = produtos_colecao.find_one({"_id": object_id})
            if produto:
                print("\nAgora digite os novos valores para o produto (pressione Enter para manter o valor atual):")

                nome = input(f"\n- Nome ({produto['nome']}): ") or produto['nome']
                data_fabricacao = input(f"- Data de fabricação ({produto['data_fabricacao'].strftime('%Y-%m-%d')}): ") or produto['data_fabricacao']
                data_validade = input(f"- Data de validade ({produto['data_validade'].strftime('%Y-%m-%d')}): ") or produto['data_validade']
                lote = input(f"- Lote ({produto['lote']}): ") or produto['lote']
                escaninho_id = input(f"- ID do escaninho ({produto['escaninho_id']}): ") or produto['escaninho_id']
                preco_medio_custo = input(f"- Preço médio de custo ({produto['preco_medio_custo']}): ") or produto['preco_medio_custo']
                data_ultima_compra = input(f"- Data da última compra ({produto['data_ultima_compra'].strftime('%Y-%m-%d')}): ") or produto['data_ultima_compra']
                quantidade_estoque_minimo = input(f"- Quantidade mínima de estoque ({produto['quantidade_estoque_minimo']}): ") or produto['quantidade_estoque_minimo']
                quantidade_estoque_maximo = input(f"- Quantidade máxima de estoque ({produto['quantidade_estoque_maximo']}): ") or produto['quantidade_estoque_maximo']
                data_ultima_movimentacao = input(f"- Data da última movimentação ({produto['data_ultima_movimentacao'].strftime('%Y-%m-%d')}): ") or produto['data_ultima_movimentacao']
                estoque_atual = input(f"- Quantidade atual em estoque ({produto['estoque_atual']}): ") or produto['estoque_atual']
                preco_unitario = input(f"- Preço unitário ({produto['preco_unitario']}): ") or produto['preco_unitario']

                produto_atualizado = {
                    "\n-nome": nome,
                    "-data_fabricacao": datetime.strptime(data_fabricacao, "%Y-%m-%d") if isinstance(data_fabricacao, str) else data_fabricacao,
                    "-data_validade": datetime.strptime(data_validade, "%Y-%m-%d") if isinstance(data_validade, str) else data_validade,
                    "-lote": lote,
                    "-escaninho_id": escaninho_id,
                    "-preco_medio_custo": float(preco_medio_custo),
                    "-data_ultima_compra": datetime.strptime(data_ultima_compra, "%Y-%m-%d") if isinstance(data_ultima_compra, str) else data_ultima_compra,
                    "-quantidade_estoque_minimo": int(quantidade_estoque_minimo),
                    "-quantidade_estoque_maximo": int(quantidade_estoque_maximo),
                    "-data_ultima_movimentacao": datetime.strptime(data_ultima_movimentacao, "%Y-%m-%d") if isinstance(data_ultima_movimentacao, str) else data_ultima_movimentacao,
                    "-estoque_atual": int(estoque_atual),
                    "-preco_unitario": float(preco_unitario)
                }

                produtos_colecao.update_one({"_id": object_id}, {"$set": produto_atualizado})
                print("__________________________________________________________________________________")
                print(Fore.GREEN + f"\nProduto com ID {produto_id} atualizado com sucesso!" + Style.RESET_ALL)
                print("__________________________________________________________________________________")
            else:
                print("__________________________________________________________________________________")
                print(Fore.RED + f"\nProduto com ID {produto_id} não encontrado." + Style.RESET_ALL)
                print("__________________________________________________________________________________")
        except Exception as e:
            print("__________________________________________________________________________________")
            print(Fore.RED + f"\nErro ao editar o produto: {e}" + Style.RESET_ALL)
            print("__________________________________________________________________________________")

        client.close()
