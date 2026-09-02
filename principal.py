import produtos
import relatorios
import persistencia

cadastro_produtos=persistencia.carregar_json()
historico=persistencia.carregar_historico()
encerrar=False

def menu():
  
  while True:
        print("1 - Cadastrar produto")
        print("2 - Consultar produto")
        print("3 - Alterar produto")
        print("4 - excluir produto")
        print("5 - Gerar relatorio")
        print("6 - Ler relatorio")
        print("7 - Salvar Json")
        print("8 - relatorio detalhado")
        print("9 - Movimentação Estoque")
        print("10 - Consultar Historico")
        print("11 - Consultar movimentaçoes produto")
        print("12 - Historico completo")
        print("13 - Ranking de atividade do estoque")
        print("14 - Relatório de saldo líquido por produto")
        print("15 - Auditor de inconsistências do histórico")
        print("16 - encerrar")
        
        try:
           opcao=int(input())
           if opcao<17 and opcao>0:
              return opcao
             
           else:
               print("opcao inexistente")
        except ValueError:
             print("seu animal, digite UM NUMERO")
             continue    
    


while True:      
     
            opcao=menu()       
    
            if opcao==1:
              produtos.cadastro(cadastro_produtos,historico)
   
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
                persistencia.salvar_json(cadastro_produtos,historico)

            elif opcao==8:
                relatorios.relatorio_estoque(cadastro_produtos)

            elif opcao==9:
                produtos.movimentação(cadastro_produtos,historico)                

            elif opcao==10:
                relatorios.movimentacao_histórico(historico)

            elif opcao==11:
                relatorios.consulta_movimentaçoes(historico)

            elif opcao==12:
                relatorios.historico_completo(historico)

            elif opcao==13:
                 relatorios.rankin_atividade(historico)
            
            elif opcao==14:
                relatorios.Relatório_saldo_líquido(historico)
            
            
            elif opcao==15:
                historico_teste =[    
                    {
                    "produto": "pedra",
                    "tipo da movimentação": "entrada",
                    "quantidade movimentada": 5,
                    "estoque antes": 5,
                    "estoque depois": 5
                    },
                    
                    {
                    "produto": "pedra",
                    "tipo da movimentação": "pele",
                    "quantidade movimentada": 0,
                    "estoque antes": 5,
                    "estoque depois": 5
                    },
                    {
                    "produto": "marros",
                    "tipo da movimentação": "feijao",
                    "quantidade movimentada": 0,
                    "estoque antes": 5,
                    "estoque depois": 5
                    },
                    {
                    "produto": "pedra",
                    "tipo da movimentação": "entrada",
                    "quantidade movimentada": 0,
                    "estoque antes": 5,
                    "estoque depois": 5
                    }
                ]

                relatorios.relatorio_inconsistências(historico_teste)     
         
            
            elif opcao==16:
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