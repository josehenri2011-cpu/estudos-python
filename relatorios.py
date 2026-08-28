import persistencia
import validacoes


def rankin_atividade(historico):
   if historico==[]:
     print("nenhum produto cadastrado")
     return
    
   resumo_temp={}
   for dicionario in historico:
        produto_atual=(dicionario["produto"])
        if produto_atual not in resumo_temp:  
            resumo_temp[produto_atual]={
                "produto":produto_atual,
                "total":0,
                "Quantidade de movimentações":0,
                
                
            }
        resumo_temp[produto_atual]["total"]+=dicionario["quantidade movimentada"]
        resumo_temp[produto_atual]["Quantidade de movimentações"]+=1

   campeao={         
            
                     "Produto maior":None, 
                     "volume total movimentado":0,
                                      
          
                 }
         
   for chave,volume in resumo_temp.items():
       if volume["total"]>campeao["volume total movimentado"]:
          campeao["volume total movimentado"]=volume["total"]
          campeao["Produto maior"]=chave
       
   
   
   for produto, dados in resumo_temp.items():
       print("produto:", produto)
       print("total de unidades movimentadas:", dados["total"])
       print("Quantidade de movimentações", dados["Quantidade de movimentações"])
   
   for chave, valor in campeao.items():
       print(chave, valor)


def historico_completo(historico):

    resumo = {}

    for dicionario in historico:

        produto_atual = dicionario["produto"]

        if produto_atual not in resumo:
            resumo[produto_atual] = {
                "total entradas": 0,
                "total saidas": 0,
                "total movimentacoes": 0
            }

        if dicionario["tipo da movimentação"] == "entrada":
            resumo[produto_atual]["total entradas"] += dicionario["quantidade movimentada"]

        elif dicionario["tipo da movimentação"] == "saida":
            resumo[produto_atual]["total saidas"] += dicionario["quantidade movimentada"]

        resumo[produto_atual]["total movimentacoes"] += 1

    for produto, dados in resumo.items():
        print("Produto:", produto)
        print("Total entradas:", dados["total entradas"])
        print("Total saidas:", dados["total saidas"])
        print("Total movimentações:", dados["total movimentacoes"])

def consulta_movimentaçoes(historico):
    if historico==[]:
       print("nenhum historico encontrado")
       return


    print("infome o produto")
    produto=input()
    total_entradas=0
    total_saidas=0
    total_movimentaçoes=0
    flag=False

    for dicionario in historico:           
        for chave, valor in dicionario.items():
            if chave=="produto":
                if produto==valor:
                   flag=True
                   for chave, valor in dicionario.items():
                       print(chave,valor)
                       if valor=="entrada":
                          movimentaçoes = dicionario["quantidade movimentada"]
                          total_movimentaçoes=total_movimentaçoes+1
                          total_entradas=total_entradas+movimentaçoes
                          
                          
                       elif valor=="saida":
                          movimentaçoes = dicionario["quantidade movimentada"]
                          total_movimentaçoes=total_movimentaçoes+1
                          total_saidas=total_saidas+movimentaçoes
                
    if flag==False:
       print("nenhum historico encontrado")
       return 
    print("total entradas:",total_entradas)
    print("total saidas:",total_saidas)
    print("total_movimentaçoes:",total_movimentaçoes)

def movimentacao_histórico(historico):
    
    if historico==[]:
       print("Não existe nenhum historico recente")
       return

    for diciociario in historico:
        for chave, valor in diciociario.items():
            print(f"{chave}:{valor}")                

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
    if cadastro_produtos == {}:
       print("nenhum registro esta cadastrado")
       return
    maior=0
    primeira_quantidade=True
    total=0
    for produto, informacoes in cadastro_produtos.items():
        print(produto)
        quantidade=cadastro_produtos[produto]["quantidade"]
        preço=cadastro_produtos[produto]["preço"]
        soma=preço * quantidade
        total=total+soma
        for chave, valor in informacoes. items():
            print(chave, valor)
            
            if chave=="quantidade":
                print(f"Valorem estoque:{soma}")

                if valor>maior:
                   maior=valor
                   nome_maior=produto

                if primeira_quantidade:
                   menor=valor 
                   nome_menor=produto
                   primeira_quantidade=False

                if valor<menor:
                   menor=valor
                   nome_menor=produto


    print("MISSAO")
    print(f"Maior quantidade:{nome_maior}={maior}")
    print(f"Menor quantidade: {nome_menor}={menor}")
    print(f"Valor total de todo estoque: {total}")