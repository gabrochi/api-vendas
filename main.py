from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco": 4, "quantidade": 3},
    2: {"item": "garrafa", "preco": 10, "quantidade": 1},
    3: {"item": "computador", "preco": 103, "quantidade": 1},
    4: {"item": "chocolate", "preco": 2, "quantidade": 12},
}

class Venda(BaseModel):
    item: str
    preco: float
    quantidade: int

#EXIBIR TODAS AS VENDAS
@app.get("/vendas")
def exibir_vendas():
    return vendas

#EXIBIR VENDA {ID_VENDA}
@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda not in vendas:
        raise HTTPException(status_code=404, detail= "id not found")
    return vendas[id_venda]

#CRIAR VENDAS
@app.post("/vendas")
def criar_venda(venda: Venda):
    novo_id = max(vendas.keys()) + 1
    vendas[novo_id] = venda.model_dump()
    return {"id": novo_id, "venda": vendas[novo_id]}

#ATUALIZAR VENDAS
@app.put("/vendas/{id_venda}")
def atualizar_venda(id_venda: int, venda: Venda):
    if id_venda not in vendas:
        raise HTTPException(status_code=404, detail="item not found")
    vendas[id_venda] = venda.model_dump()  
    return {"id": id_venda, "venda": vendas[id_venda]}

#DELETAR VENDAS
@app.delete("/vendas/{id_venda}")
def remover_id(id_venda: int):
    if id_venda not in vendas:
        raise HTTPException(status_code=404, detail="id not found")
    dados = vendas[id_venda]
    vendas.pop(id_venda)
    return {"id removido": id_venda, "dados removidos": dados}

@app.get("/relatorio")
def exibir_relatorio():

    quantidades = []
    total = []
    maior_item = 0 
    maior_qtd_item = 0
    
    for venda in vendas.values():
        quantidades.append(venda["quantidade"]) #adiciona em quantidades os valores de venda["quantidade"]
        total.append(venda["preco"] * venda["quantidade"])  #adiciona em quantidades os valores de venda["preco"] * venda["quantidade"] 

        if venda["preco"] > maior_item: #verifica o maior preco dos pedidos e retorna o item e o preco
            maior_item = {"item": venda["item"], "preco": venda["preco"]}
            
        if venda["quantidade"] > maior_qtd_item: #verifica a maior quantidade dos itens dos pedidos e retorna o item e a quantidade
            maior_qtd_item = {"item": venda["item"], "quantidade": venda["quantidade"]}
    

    somatorio = sum(total) #somando...
    resultado = sum(quantidades)  
    
    return {"soma da quantidade de produtos": resultado,
            "soma dos valores X quantidade": somatorio,
            "o item de maior preco eh": maior_item,
            "o item de maior quantidade eh": maior_qtd_item
            }

