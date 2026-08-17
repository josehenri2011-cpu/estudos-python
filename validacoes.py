import principal

def ler_produto():
    while True:
            print("informe o produto")
            produto=input()
            if produto not in principal.cadastro_produtos:
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


def buscar_produto(produto):
    if produto in principal.cadastro_produtos:
       return principal.cadastro_produtos[produto]
    else:
        return False
