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
