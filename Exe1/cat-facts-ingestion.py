import datetime as dt
import requests
import json
import csv
import os
import re


regs = 100

def requisicaoAPI():
    data_req = requests.get(f'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={regs}')
    data_json = data_req.json()
    return data_json

def gerarLandingJson(data_json,nfl:bool,hist:bool):
    if hist == True:
        if nfl == True:
            arquivo_json = f'Exe1/json-ingest/cat-facts-{re.sub(r'[-. :]', '',str(dt.datetime.today())[:19])}.json' # Importante: Interpretacao da datastamp: YYYY-MM-DD HH:MM:SS
        elif nfl == False:
            arquivo_json = f'Exe1/json-ingest/cat-facts.json'
        arquivo_json = os.path.abspath(arquivo_json)

        with open(arquivo_json, 'w', encoding='utf-8') as jf:
            json.dump(data_json, jf, indent=4)

def gerarCSV(data_json):
    arquivo_csv = 'Exe1/csv/cat-facts.csv'
    arquivo_csv = os.path.abspath(arquivo_csv)
    
    nome_campos = ["_id", "user", "text", "type", "deleted", "createdAt", "updatedAt", "__v", "status_verified", "status_sentCount"]

        
    with open(arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        
        writer.writerow(nome_campos)
        
        if regs > 1:
            for item in data_json:
                row = [
                    item.get("_id"),
                    item.get("user"),
                    item.get("text"),
                    item.get("type"),
                    item.get("deleted"),
                    item.get("createdAt"),
                    item.get("updatedAt"),
                    item.get("__v"),
                    item["status"].get("verified") if "status" in item else None,
                    item["status"].get("sentCount") if "status" in item else None,
                ]
                writer.writerow(row)
        else:
            row = [
                data_json.get("_id"),
                data_json.get("user"),
                data_json.get("text"),
                data_json.get("type"),
                data_json.get("deleted"),
                data_json.get("createdAt"),
                data_json.get("updatedAt"),
                data_json.get("__v"),
                data_json["status"].get("verified") if "status" in data_json else None,
                data_json["status"].get("sentCount") if "status" in data_json else None,
            ]
            writer.writerow(row)

try:
    dados_api = requisicaoAPI()
    gerarLandingJson(dados_api,True,True)
    gerarCSV(dados_api)
    print("Processo concluído.")
except Exception as e:
    print(f"Erro: {e}")