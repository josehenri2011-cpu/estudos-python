import persistencia
import validacoes


movimentacoes = [
    {"produto": "Arroz", "tipo": "entrada", "quantidade": 30},
    {"produto": "Feijao", "tipo": "entrada", "quantidade": 20},
    {"produto": "Cafe", "tipo": "entrada", "quantidade": 15},
    {"produto": "Arroz", "tipo": "saida", "quantidade": 12},
    {"produto": "Feijao", "tipo": "saida", "quantidade": 7},
    {"produto": "Cafe", "tipo": "saida", "quantidade": 10},
    {"produto": "Arroz", "tipo": "entrada", "quantidade": 5},
    {"produto": "Feijao", "tipo": "saida", "quantidade": 8},
]

def relatorio_Produto_Movimentação_Estoque(historico):
    dados=analise_Produto_Movimentação_Estoque(historico)
    for chave, valor in dados.items():
        print(chave,":")
        for produto, informacoes in valor.items():
            print(produto,informacoes)


def analise_Produto_Movimentação_Estoque(historico):
    acumulador=0
    produto_campeao=0
    analise={}
    relatorio={}
    total={
        "total_geral":0,
    }
    dic_temp={                           
                "produto_maior_participação":0,
                "percentual":0
                }
              
    for dicionario in historico:
        produto_atual=dicionario["produto"]
        if produto_atual not in analise:
            analise[produto_atual]={
                "total_entradas":0,
                "total_saidas":0,
                "total_produto":0,
                "percentual_produto":0,
                } 
        if dicionario["tipo da movimentação"]=="entrada":
            analise[produto_atual]["total_entradas"]+=dicionario["quantidade movimentada"]
    
        if dicionario["tipo da movimentação"]=="saida":
            analise[produto_atual]["total_saidas"]+=dicionario["quantidade movimentada"]
        
        analise[produto_atual]["total_produto"]=analise[produto_atual]["total_entradas"]+analise[produto_atual]["total_saidas"]
       
        
        
        
    for chave,dados in analise.items():
         if "total_produto" in dados:
             acumulador+=dados["total_produto"]
             
    total["total_geral"]=acumulador  
    
    
    
    
    for chave, valor in analise.items():
        if "total_produto" in valor:
          analise[chave]["percentual_produto"]=valor["total_produto"]/total["total_geral"]*100
        
        if analise[chave]["percentual_produto"]>produto_campeao: 
           produto_campeao=analise[chave]["percentual_produto"]
           dic_temp["produto_maior_participação"]=chave
    
    dic_temp["percentual"]=produto_campeao
    relatorio["dados_produtos"]=analise
    relatorio["total_movimentado"]=total
    relatorio["produto_campeao"]=dic_temp
    return relatorio
        
    
    
    
        



def relatorio_media_produtos(historico):
    relatorio=Produtos_abaixo_saldo_médio(historico)
    for chave, valor in relatorio.items():
        print(chave,valor)
def Produtos_abaixo_saldo_médio(historico):
    analise={}
    teste={
        "total":0,
        "quantidade_produtos":0,     
    }
    
    relatorio={
        "saldo_medio":0,
        
    }        
    
    
    for dicionario in historico:
        produto_atual=dicionario["produto"]
        if produto_atual not in analise:
            analise[produto_atual]={
              "total_entradas":0,
              "total_saidas":0,
              "saldo_final":0,
               }
            teste["quantidade_produtos"]+=1
        
        
        if dicionario["tipo da movimentação"]=="entrada":
            analise[produto_atual]["total_entradas"]+=dicionario["quantidade movimentada"]
        
        if dicionario["tipo da movimentação"]=="saida":
            analise[produto_atual]["total_saidas"]+=dicionario["quantidade movimentada"]
        analise[produto_atual]["saldo_final"]=analise[produto_atual]["total_entradas"]-analise[produto_atual]["total_saidas"]
    for chave,dados in analise.items():
        teste["total"]+=dados["saldo_final"]
        relatorio["saldo_medio"]=teste["total"]/teste["quantidade_produtos"]
        
    
    for chave,dados in analise.items():
        produto_reprovado=chave
        if dados["saldo_final"]<relatorio["saldo_medio"]:  
           relatorio[produto_reprovado]={
               "saldo_produto_abaixo_media":0,
               }
           relatorio[produto_reprovado]["saldo_produto_abaixo_media"]=dados["saldo_final"]
    return relatorio
    
    print(analise)
    print(teste)
    print(relatorio)



def leitor_dinamico():
    numero_critico=analista()
    movimentaçoes=Consolidar_estoque()
    
    if movimentaçoes=={}:
            numero_critico=analista()
            print("vazio")
            return
    else:
        print(movimentaçoes)

    if numero_critico=={}:
        print("vazio")
        return
    else:
       print(numero_critico)
           

def analista():
    dicionario=Consolidar_estoque()          
    
    
    
    identificador={       
        "produto_menor_saldo":0,
        "numero_critico":0,    
    }
    flag=True
    for chave, dados in dicionario.items():           
       if flag: 
          identificador["produto_menor_saldo"]=chave
          identificador["numero_critico"]=dados["saldo_final"]
          flag=False
       if identificador["numero_critico"]>dados["saldo_final"]:
           identificador["produto_menor_saldo"]=chave
           identificador["numero_critico"]=dados["saldo_final"]
    
    
    return identificador       

    

def Consolidar_estoque():
    
    analise={}
    
    for dicionario in movimentacoes:
        produto_atual=dicionario["produto"]
        if produto_atual not in analise:
           analise[produto_atual]={
                "total_unidades_entrada":0,
                "total_unidades_saida":0,
                "saldo_final":0
                }
        if dicionario["tipo"]=="entrada":
           analise[produto_atual]["total_unidades_entrada"]+=dicionario["quantidade"]
        if dicionario["tipo"]=="saida":
           analise[produto_atual]["total_unidades_saida"]+=dicionario["quantidade"]
        analise[produto_atual]["saldo_final"]=analise[produto_atual]["total_unidades_entrada"]-analise[produto_atual]["total_unidades_saida"]
    return analise
  



def Extrato_Produto(historico,produto):
    dic_analise=Analise_Produto(historico,produto)
    print(dic_analise["entrada"]["produto"])
    print(f"total entrada:{dic_analise['entrada']['operaçoes_entrada']}")
    print(f"total unidades entrada: {dic_analise['entrada']['total_unidades_entrada']}")
    print(f"total saida: {dic_analise['entrada']['operaçoes_saida']}")
    print(f"saldo_movimentado: {dic_analise['entrada']['saldo_movimentado']}")


def Analise_Produto(historico,produto):
    dic_analise={
        "entrada":{
                             "produto":None,
                              "operaçoes_entrada":0,
                              "total_unidades_entrada":0,
                              "operaçoes_saida":0,                  
                               "total_unidades_saida":0,                         
                                "saldo_movimentado":0                        },
    
        
    }
        
    for dicionario in historico:
        if dicionario["produto"]==produto:
           if dicionario["tipo da movimentação"]=="entrada":
              dic_analise["entrada"]["produto"]=dicionario["produto"]
              dic_analise["entrada"]["operaçoes_entrada"]+=1
              dic_analise["entrada"]["total_unidades_entrada"]+=dicionario["quantidade movimentada"]
           elif dicionario["tipo da movimentação"]=="saida":
               dic_analise["entrada"]["operaçoes_saida"]+=1
               dic_analise["entrada"]["total_unidades_saida"]+=dicionario["quantidade movimentada"]
           dic_analise["entrada"]["saldo_movimentado"]=dic_analise["entrada"]["total_unidades_entrada"]-dic_analise["entrada"]["total_unidades_saida"]
    return dic_analise

def relatorio_maior_movimentação(historico):
    maior_movimentação=Maior_movimentação_tipo(historico)
    print(maior_movimentação["entrada"]["produto"])
    print(maior_movimentação["entrada"]["maior_entrada"])           
    print(f"quantidade de movimentações:{maior_movimentação['entrada']['operaçoes_entrada']}")           
    print(f"total movimentado:{maior_movimentação['entrada']['total_movimentado_entrada']}")           
        
    print(maior_movimentação["saida"]["produto"])
    print(maior_movimentação["saida"]["maior_saida"])           
    print(f"quantidade de movimentações:{maior_movimentação['saida']['operaçoes_saida']}")           
    print(f"total movimentado:{maior_movimentação['saida']['total_movimentado_saida']}")           


def Maior_movimentação_tipo(historico):
    movimentacao={
        "entrada":{
             "produto":None,
             "maior_entrada":0,
              "operaçoes_entrada":0,
              "total_movimentado_entrada":0   
                 
                           },
        "saida":{
            "produto":None,
            "maior_saida":0,
            "operaçoes_saida":0,
            "total_movimentado_saida":0
            
            },
    }
    
    for dicionario in historico:
        if dicionario["tipo da movimentação"]=="entrada":
           movimentacao["entrada"]["operaçoes_entrada"]+=1
           movimentacao["entrada"]["total_movimentado_entrada"]+=dicionario["quantidade movimentada"] 
           if dicionario["quantidade movimentada"]>movimentacao["entrada"]["maior_entrada"]:
               movimentacao["entrada"]["produto"]=dicionario["produto"]
               movimentacao["entrada"]["maior_entrada"]=dicionario["quantidade movimentada"]
    
        elif dicionario["tipo da movimentação"]=="saida":
             movimentacao["saida"]["operaçoes_saida"]+=1
             movimentacao["saida"]["total_movimentado_saida"]+=dicionario["quantidade movimentada"]
             if dicionario["quantidade movimentada"]>movimentacao["saida"]["maior_saida"]:
                movimentacao["saida"]["produto"]=dicionario["produto"]
                movimentacao["saida"]["maior_saida"]=dicionario["quantidade movimentada"]
    return movimentacao        
               
               
            
    

def relatorio_inconsistências(historico):  
    list_auditor=Auditor_inconsistências(historico)
    
    for dados_auditor in list_auditor:
        relatorio_geral=dados_auditor["resumo"]
        if relatorio_geral["total analisado"]==0:
            print("historico esta vazio")
            return
        print("Relatorio Geral:")
        print(f"total analisado:{relatorio_geral['total analisado']}")
        print(f"válidas:{relatorio_geral['válidas']}")
        print(f"inválidas:{relatorio_geral['inválidas']}")
        print(f"percentual validas: {relatorio_geral['percentual validas']}%")
        print(f"percentual invalidas: {relatorio_geral['percentual invalidas']}%")
            
        
        for ocorrencia in dados_auditor["ocorrencias"]:    
            print("--------------------------")
            print(ocorrencia["Produto:"])
            if ocorrencia["categoria"] != "":
               print(ocorrencia["categoria"])
            
            if ocorrencia["Quantidade"] != "":
               print(ocorrencia["Quantidade"])
            
            
             
    

def Auditor_inconsistências(historico):
    
    movimentaçoes_analisadas = 0
    Movimentaçoes_validas = 0
    Movimentaçoes_invalidas = 0

    lista_auditor = []

    dic_auditor = {
    "resumo": {},
    "ocorrencias": []
}
   

    for dicionario in historico:
        problemas={}
        produto_atual = dicionario["produto"]

        movimentaçoes_analisadas += 1

        flag = False
        categoria = False
        quantidade = False

        if dicionario["produto"] == "":
            flag = True
        if dicionario["tipo da movimentação"] == "entrada":
            pass

        elif dicionario["tipo da movimentação"] == "saida":
            pass

        else:
            flag = True
            categoria = True

        if dicionario["quantidade movimentada"] <= 0:
            flag = True
            quantidade = True

        if flag==True:
            Movimentaçoes_invalidas += 1
            

            if dicionario["produto"] == "":
                
                problemas["Produto:"]="Problema: Nenhum produto encontrado"
                
            else:
               problemas["Produto:"]=produto_atual
    

            if categoria:
               problemas["categoria"]="Problema: movimentação invalida"
            else:
                problemas["categoria"] = ""
            

            if quantidade:

                problemas["Quantidade"]="Problema: quantidade inválida"
            else:
                problemas["Quantidade"] = ""
            
            dic_auditor["ocorrencias"].append(problemas)
                

        else:
            Movimentaçoes_validas += 1

    dic_auditor["resumo"]["total analisado"] = movimentaçoes_analisadas
    dic_auditor["resumo"]["válidas"] = Movimentaçoes_validas
    dic_auditor["resumo"]["inválidas"] = Movimentaçoes_invalidas
    if dic_auditor["resumo"]["total analisado"]>0:
        dic_auditor["resumo"]["percentual validas"] =(Movimentaçoes_validas / movimentaçoes_analisadas) * 100
        dic_auditor["resumo"]["percentual invalidas"] =(Movimentaçoes_invalidas / movimentaçoes_analisadas) * 100
    elif dic_auditor["resumo"]["total analisado"]==0:
         dic_auditor["resumo"]["percentual validas"] =0
         dic_auditor["resumo"]["percentual invalidas"] =0
    lista_auditor.append(dic_auditor)
    

   

    
    return lista_auditor
    
def Relatório_saldo_líquido(historico):
    if historico==[]:
       print("vazio")
       return
    
    dic_temp={}
    for dicionario in historico:
        
        produto_atual=(dicionario["produto"])
        
        if produto_atual not in  dic_temp:
           dic_temp[produto_atual]={
                        "total_entradas:":0,
                        "total_saidas:":0,
                        "saldo líquido:":0, 
                        "situação:":None,  
                    
                    }
        
        if dicionario["tipo da movimentação"]=="entrada":
           dic_temp[produto_atual]["total_entradas:"]+=dicionario["quantidade movimentada"]
        
        elif dicionario["tipo da movimentação"]=="saida":
             dic_temp[produto_atual]["total_saidas:"]+=dicionario["quantidade movimentada"]
        
        dic_temp[produto_atual]["saldo líquido:"]=dic_temp[produto_atual]["total_entradas:"]-dic_temp[produto_atual]["total_saidas:"]
        
        if dic_temp[produto_atual]["total_entradas:"]>dic_temp[produto_atual]["total_saidas:"]:
           dic_temp[produto_atual]["situação:"]="positivo"
        
        elif dic_temp[produto_atual]["saldo líquido:"]==0:
             dic_temp[produto_atual]["situação:"]="zerado"
        
        else:
            dic_temp[produto_atual]["situação:"]="negativo"
    
    for chave, dic in dic_temp.items():
        print("Produto:", chave)
        print("Total Entradas:", dic["total_entradas:"])
        print("Total Saidas:", dic["total_saidas:"])
        print("Saldo líquido:", dic["saldo líquido:"])
        print("Situação",dic["situação:"])
            



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
            
                     "Produto maior:":None, 
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