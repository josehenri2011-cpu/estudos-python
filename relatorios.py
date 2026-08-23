

def ler_relatorio():
   try:
      with open("produtos.txt", "r") as arquivo:
            fichas=arquivo.read()
            print(fichas)
   except FileNotFoundError:
          print("Arquivo nao encontrado")
def gerar_relatorio(cadastro_produtos):
    with open("produtos.txt", "w") as arquivo:
        for produto, informaçoes in cadastro_produtos.items():
            arquivo.write(f"{produto}\n")
            for chave, valor in informaçoes.items():
                arquivo.write(f" {chave}, {valor}\n")

def relatorio_estoque(cadastro_produtos):
    maior=0
    primeira_quantidade=True
    for produto, informacoes in cadastro_produtos.items():
        print(produto)
        quantidade=cadastro_produtos[produto]["quantidade"]
        preço=cadastro_produtos[produto]["preço"]
        

        for chave, valor in informacoes. items():
            print(chave, valor)
            
            if chave=="quantidade":
                print(f"Valor total do estoque:{preço * quantidade}")

                if valor>maior:
                   maior=valor
                if primeira_quantidade:
                   menor=valor 
                   primeira_quantidade=False
                if valor<menor:
                   menor=valor
                   


    print("MISSAO")
    print("Maior quantidade:", maior)
    print("Menor quantidade:", menor)
    