import requests
import json

# Envio de Webhook
# url = 'https://webhook.site/0a1839e8-2e31-431d-a20d-bc794cbe5d8e'
url = 'http://127.0.0.1:5000/webhook/pagamentos-novos'
dic = {
    "nome": "Mi",
    "email": "mi@email.com.br",
    "status": "reembolsado",
    "valor": 870.50,
    "forma_pagamento": "paypal",
    "parcelas": 4
}

r = requests.post(url=url, data=json.dumps(dic, indent=4), headers={'Content-Type': 'application/json'})
print(r)

