import json     

def salvar_json(cadastro_produtos,historico):
    with open("produtos.json", "w") as arquivo:
        json.dump(cadastro_produtos, arquivo, ensure_ascii=False, indent=4)
    with open("Historico_movimentaçoes.json", "w") as arquivo:
           json.dump(historico, arquivo, ensure_ascii=False, indent=4)
   
def carregar_json():
    try:
        with open("produtos.json", "r") as arquivo:
             dados=json.load(arquivo)
             return dados
        with open("Historico_movimentaçoes.json", "r") as arquivo:
                     dados=json.load(arquivo)
                     return dados            
    except FileNotFoundError:
             
             return {}
    except json.JSONDecodeError:
           print("Arquivo corrompido")
           return {}

def carregar_historico():
      try:
          with open("Historico_movimentaçoes.json", "r") as arquivo:
                       historico=json.load(arquivo)
                       return historico            
      except FileNotFoundError:
    
               return []
      except json.JSONDecodeError:
             print("Arquivo corrompido")
             return []
    