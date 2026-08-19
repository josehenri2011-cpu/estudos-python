import produtos
import relatorios
import persistencia

cadastro_produtos=persistencia.carregar_json()




def menu(cadastro_produtos):
  
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
              produtos.cadastro(cadastro_produtos)
   
            elif opcao==2:
                produtos.consultar_produto(cadastro_produtos)
    
            elif opcao==3:
                produtos.Alteração_produto(cadastro_produtos)
    
            elif opcao==4:
                produtos.excluir_produto(cadastro_produtos)
    
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




menu(cadastro_produtos)