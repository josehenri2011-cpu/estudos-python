

import persistencia
import validacoes

encerrar=False


def cadastro(cadastro_produtos):
          while True:       
               produto=validacoes.ler_produto(cadastro_produtos)  
               preço=validacoes.ler_preço()
               quantidade=validacoes.ler_quantidade()
          
               dados={
                      "preço":preço,
                      "quantidade": quantidade}
               
         
               
               cadastro_produtos[produto]=dados

               persistencia.salvar_json(cadastro_produtos)
               while True:
                    print("deseja continuar ? sim/nao")
                    continuar=input()
                    if continuar=="nao":
                       sair=True
                       break
                    elif continuar=="sim":
                        sair=False 
                        break                
             
                    else:
                      print("opçao invalida!")  
    
          

               if sair==True:
                  return

def consultar_produto(cadastro_produtos):
    buscar= True
    while buscar:
          print(" nome do produto")
          produto=input()
          dados=validacoes.buscar_produto(produto,cadastro_produtos)
          if dados==False:
             print("produto nao registrado")
             
          else:   
             print(f"produto {produto}:")
             print(dados)
             
          
          print("deseja buscar outro produto ?")
          resposta=input()
          if resposta=="sim":
             buscar=True
          elif resposta=="nao":
             print("voltando ao menu")
             buscar= False
          
          else:
            print("resposta inválida")
          
         
    

 #MENU 


def Alteração_produto(cadastro_produtos):
    while True:
         print("qual produto vc deseja alterar ? ")
         produto=input()
         dados=validacoes.buscar_produto(produto,cadastro_produtos)
         if dados:
            break
         else:
            print("produto nao encontrado, tente novamente")
    
    print("qual informaçao deseja alterar ? ")
    buscar=input()
    if buscar in  cadastro_produtos[produto]:
       if buscar=="preço":
          novo_valor=validacoes.ler_preço()
          cadastro_produtos[produto][buscar]=novo_valor
       elif buscar=="quantidade":
          novo_valor=validacoes.ler_quantidade()
          cadastro_produtos[produto][buscar]=novo_valor
       persistencia.salvar_json(cadastro_produtos)
 

    else:
      print("valor nao localizado, tente novamente")


def excluir_produto(cadastro_produtos):
    while True:
       flag= False
       print("qual produto deseja excluir?")
       produto=input()
       dados=validacoes.buscar_produto(produto,cadastro_produtos)
       if dados:
            print(dados)
            while True:    
                 print("tem certeza que deseja excluir ?")
                 resposta=input()
                 if resposta== "sim":
                    del cadastro_produtos[produto]
                    print("produto excluido com sucesso")
                    persistencia.salvar_json(cadastro_produtos)
                    flag=True
                    break
                 elif resposta== "nao":
                     print("voltando ao menu")
                     flag=True
                     break                 
                 else:
                   print("resposta invalida")

       else:
         print("produto nao encontrado")
   
           

       if flag:
           return       

def movimentação(cadastro_produtos,historico):
    
    valor=0
    print("Qual Produto?")
    produto=input()
    if produto in cadastro_produtos:
       dados=validacoes.buscar_produto(produto,cadastro_produtos)
       print(dados)
       
       estoque=cadastro_produtos[produto]["quantidade"]
       print(estoque)
       dict_estoque={
               "produto":produto,
                }
       historico.append(dict_estoque)

    else:
        print("produto nao encontrado")
        return
    while True:
         print("selecione entrada ou saida")
         opcao=input()
         if opcao== "entrada":
            valor=validacoes.ler_quantidade()
            total=valor+estoque
            print(f"Estoque atual: {estoque}")
            print(f"entrada solicitada:{valor}"  )
            print(f"Estoque Final: {total}")
            cadastro_produtos[produto]["quantidade"]=total
            print(cadastro_produtos[produto]["quantidade"])
            dict_estoque["tipo da movimentação"]= "entrada"
            dict_estoque["quantidade movimentada"]= valor
            dict_estoque["estoque antes"]= estoque
            dict_estoque["estoque depois"]= total

            persistencia.salvar_json(cadastro_produtos)
            break
         
         elif opcao=="saida":
              valor=validacoes.ler_quantidade()
              total=estoque-valor
              dict_estoque["tipo da movimentação"]= "saida"

              if total>=0:
                 print(f"Estoque atual: {estoque}")
                 print(f"Saida solicitada:{valor}"  )
                 print(f"Estoque Final: {total}")
                 cadastro_produtos[produto]["quantidade"]=total
                 print(cadastro_produtos[produto]["quantidade"])
                 dict_estoque["quantidade movimentada"]= valor
                 dict_estoque["estoque antes"]= estoque
                 dict_estoque["estoque depois"]= total
                 persistencia.salvar_json(cadastro_produtos)
                 break
              else:
                  print("o estoque nao pode ser negativo")

         else:
             print("opçao invalida") 


                      
          
                