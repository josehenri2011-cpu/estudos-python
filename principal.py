

import persistencia
import relatorios
import validacoes
cadastro_produtos=persistencia.carregar_json()
encerrar=False


def cadastro(cadastro_produtos):
          while True:       
               produto=validacoes.ler_produto()  
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
          dados=validacoes.buscar_produto(produto)
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
         dados=validacoes.buscar_produto(produto)
         if dados:
            break
         else:
            print("produto nao encontrado, tente novamente")
    
    print("qual informaçao deseja alterar ? ")
    buscar=input()
    if buscar in  cadastro_produtos[produto]:
       print("digite o novo valor")
       novo_valor=float(input())
       cadastro_produtos[produto][buscar]=novo_valor
       persistencia.salvar_json(cadastro_produtos)
    else:
      print("valor nao localizado, tente novamente")


def excluir_produto():
    print("qual produto deseja excluir?")
    produto=input()
    dados=validacoes.buscar_produto(produto)
    if dados:
       print(dados)
       print("tem certeza que deseja excluir ?")
       resposta=input()
       if resposta== "sim":
          del cadastro_produtos[produto]
          print("produto excluido com sucesso")
          persistencia.salvar_json(cadastro_produtos)
       elif resposta== "nao":
           print("voltando ao menu")
           return
           
       
       else:
          print("resposta invalida")

    else:
       print("produto nao cadastrado")








          
                 
          
          


def menu():
  while True:
        print("1 - Cadastrar produto")
        print("2 - Consultar produto")
        print("3 - Alterar produto")
        print("4 - excluir produto")
        print("5 - Gerar relatorio")
        print("6 - Ler relatorio")
        print("7 - Salvar Json")
        print("8 - Encerrar")
        try:
           opcao=int(input())
           if opcao<9 and opcao>0:
              return opcao
             
           else:
               print("opcao inexistente")
        except ValueError:
             print("seu animal, digite UM NUMERO")
             continue

        
while True: 
     opcao=menu()       
    
     if opcao==1:
        cadastro(cadastro_produtos)
   
     elif opcao==2:
          consultar_produto(cadastro_produtos)
    
     elif opcao==3:
          Alteração_produto(cadastro_produtos)
    
     elif opcao==4:
          excluir_produto()
    
     elif opcao==5:
          relatorios.gerar_relatorio(cadastro_produtos)
          
     elif opcao==6:
          relatorios.ler_relatorio() 

     elif opcao==7:
          persistencia.salvar_json(cadastro_produtos)

     

     elif opcao==8:
          while True:
              print("Tem certeza que deseja finalizar ?") 
              resposta=input()
              if resposta =="sim":
                 encerrar=True
                 break
         
              elif resposta=="nao":
                   print("voltando ao menu")
                   break
                    
              else:
                 print("resposta invalida")
        
     if encerrar==True:
        print("programa finalizado")
        break