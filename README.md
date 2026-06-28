# 🛒 API de Vendas — FastAPI

API REST de vendas construída do zero com FastAPI, desenvolvida para fins de estudo.

## 🚀 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- Python 3.11+

## 📦 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/vendas` | Lista todas as vendas |
| GET | `/vendas/{id}` | Retorna uma venda pelo ID |
| POST | `/vendas` | Cria uma nova venda |
| PUT | `/vendas/{id}` | Atualiza uma venda existente |
| DELETE | `/vendas/{id}` | Remove uma venda |
| GET | `/relatorio` | Retorna faturamento total, item mais caro e item mais vendido |

## ▶️ Como rodar

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Acesse a documentação automática em: http://127.0.0.1:8000/docs

## ⚠️ Observação

Os dados são armazenados em memória — ao reiniciar o servidor, as alterações são perdidas.

## 🔜 Próximos passos

- [ ] Integração com banco de dados
- [ ] Validações com `@field_validator` do Pydantic
- [ ] Autenticação com JWT
- [ ] Testes automatizados com pytest
