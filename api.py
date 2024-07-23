from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/cpf/<cpf>', methods=['GET'])
def get_cpf_info(cpf):
    headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://si-pni.saude.gov.br/',
        'sec-ch-ua-mobile': '?0',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiI5ODc3NjIyMzI3MiIsIm9yaWdlbSI6IlNDUEEiLCJpc3MiOiJzYXVkZS5nb3YuYnIiLCJub21lIjoiRUxMRU4gR09Ow4dBTFZFUyBERSBTT1VTQSIsImF1dGhvcml0aWVzIjpbIlJPTEVfU0ktUE5JX09FU0MiLCJST0xFX1NDUEFTSVNURU1BX0dFUyIsIlJPTEVfU0ktUE5JIiwiUk9MRV9TQ1BBX0dFUyIsIlJPTEVfU0NQQV9VU1IiLCJST0xFX1NDUEFTSVNURU1BIiwiUk9MRV9TSS1QTklfR0VTQSIsIlJPTEVfU0NQQSJdLCJjbGllbnRfaWQiOiJTSS1QTkkiLCJzY29wZSI6WyJDTlNESUdJVEFMIiwiR09WQlIiLCJTQ1BBIl0sImNuZXMiOiJudWxsIiwib3JnYW5pemF0aW9uIjoiREFUQVNVUyIsImNwZiI6Ijk4Nzc2MjIzMjcyIiwiZXhwIjoxNzIxNzU0NDAxLCJqdGkiOiI2YjhlNmJhMi04ZTBmLTQ4MzAtOGRiZS1lMzk2Y2MwN2JiNzAiLCJrZXkiOiIyNjE3OTQiLCJlbWFpbCI6ImVsbGVuZC1zb3VzYUBob3RtYWlsLmNvbSJ9.gL-Jqtfi0J9JuIs1g_a3oQYcuowIBoqqjyUV1OtdmUE',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(f'https://servicos-cloud.saude.gov.br/pni-bff/v1/cidadao/cpf/{cpf}', headers=headers)
    data = response.json()

    if 'records' in data and len(data['records']) > 0:
        record = data['records'][0]
        formatted_data = {
            "status": 200,
            "dados": {
                "cpf": record.get("cpf", ""),
                "nome": record.get("nome", ""),
                "data_nascimento": record.get("dataNascimento", ""),
                "sexo": record.get("sexo", ""),
                "obito": record.get("obito", False),
                "endereco": {
                    "logradouro": record['endereco'].get("logradouro", ""),
                    "numero": record['endereco'].get("numero", ""),
                    "bairro": record['endereco'].get("bairro", ""),
                    "cep": record['endereco'].get("cep", ""),
                    "municipio": record['endereco'].get("municipio", ""),
                    "sigla_uf": record['endereco'].get("siglaUf", ""),
                },
                "telefone": {
                    "ddi": record['telefone'][0].get("ddi", "") if record.get("telefone") else "",
                    "ddd": record['telefone'][0].get("ddd", "") if record.get("telefone") else "",
                    "numero": record['telefone'][0].get("numero", "") if record.get("telefone") else "",
                },
                "nome_mae": record.get("nomeMae", ""),
                "nome_pai": record.get("nomePai", "")
            },
           
        }
    else:
        formatted_data = {
            "status": 404,
            "error": "No records found"
        }

    return jsonify(formatted_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

