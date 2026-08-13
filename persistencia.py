import json     

def salvar_json(cadastro_produtos):
   with open("produtos.json", "w") as arquivo:
        json.dump(cadastro_produtos, arquivo, ensure_ascii=False, indent=4)

def carregar_json():
    try:
        with open("produtos.json", "r") as arquivo:
             dados=json.load(arquivo)
             return dados
             
             
    except FileNotFoundError:
             
             return {}
    except json.JSONDecodeError:
           print("Arquivo corrompido")
           return {}