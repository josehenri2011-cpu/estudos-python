
def ler_produto(cadastro_produtos):
    while True:
            print("informe o produto")
            produto=input()
            if produto not in cadastro_produtos:
               return produto
            else:
                print(f"{produto} já esta cadastrado")


def ler_quantidade():
      while True:
              try:
                 print("coloque a quantidade")
                 quantidade=int(input())
                 if quantidade>=0:
                    return quantidade
                                   
                 else:
                     print("A quantidade deve ser um numero inteiro e positivo")
              except ValueError:
                    print("A quantidade deve conter um valor inteiro, sua anta")
    
def ler_preço():
    while True:   
          try:
              print("informe o preço")
              preço=float(input())
              
              if preço>0:
                 return preço
                                
               
              else:
                  print("o valor do preço deve ser maior que zero")
                  continue
               
          except ValueError:
                 print("o preço deve conter um valor numerico, sua anta")


def buscar_produto(produto,cadastro_produtos):
    if produto in cadastro_produtos:
       return cadastro_produtos[produto]
    else:
        return False
