from fastapi import FastAPI
import pandas as pd
import json

app = FastAPI()

@app.get("/")
async def read_excel_file():
    # Ler arquivo Excel
    df = pd.read_excel('arquivo.xlsx')

    # Converter para JSON
    json_data = df.to_json(orient='records')

    return json_data

@app.get("/xlsxtojson")
async def excel_to_json():
    # Ler o arquivo Excel
    df = pd.read_excel('arquivo.xlsx')

    # Converter para JSON
    json_data = df.to_json(orient='records')

    # Salvar o JSON em um arquivo
    with open('arquivo.json', 'w') as json_file:
        json_file.write(json_data)

    print("Conversão de Excel para JSON concluída!")
    return json_data

@app.get("/jsontoxlsx")
async def json_to_excel():
    # Ler o arquivo JSON
    with open('arquivo.json', 'r') as json_file:
        json_data = json.load(json_file)

    # Converter para DataFrame
    df = pd.DataFrame(json_data)

    # Salvar como arquivo Excel
    df.to_excel('arquivo_convertido.xlsx', index=False)

    print("Conversão de JSON para Excel concluída!")
    return df
