# Aprendendo manipulacoes de arquivos:
Esse projeto visa em aprender a manipular arquivos de diversos tipos e, tambem, saber relaciona-los.

## Virtual Environment in Python
First, we have to create a Python environment.

    https://fastapi.tiangolo.com/pt/virtual-environments/

If you prefer, with virtual environment, you can use uv to manage more easily versions os pythons that you want to use in a local directory

    https://docs.astral.sh/uv/

    https://github.com/astral-sh/uv

1. Checking python version:

        python --version or python3 --version

2. Checking if venv installed:

    Usually, Python 3.3 to above the venv comes together.

        python -m venv --help

3. Creating an virtual environment

    Choose the directory that you want to develop and digit the following command

        python -m venv environment_name

4. Activating the virtual environment:

    Window

        environment_name\Scripts\activate

    MacOs/Linux

        source environment_name/bin/activate

5. Now, you can install, using pip, fastapi package:

    Before to install packages

        python -m pip install --upgrade pip

    The installation forms below is to ensure that other packages is installed with fastapi, for example, uvicorn

        pip install "fastapi[standard]" or pip install "fastapi[all]"

    If you want to install fastapi in classic form, just runs

        pip install fastapi
    
    but is recommended to install also uvicorn in following

        pip install "uvicorn[standard]"

    and the same form to other packages.

    If you have a requirements.txt, just copy it inside of virtual environment directory and run following command

        pip install -r requirements.txt

6. Freeze packages versions on the requirements.txt file:

    After installed packages that you need to your project is a good practice to freeze its in a requirements.txt files.

    To do it, you have, in first, digit

        pip freeze

    After this you have to create a requirements file and to make Ctrl+C and Ctrl+V about this file. Or, more fast

        pip freeze > requirements.txt

Now, you have an isolated virtual environment to start to develop your first fast api.

Just see references that I used to study about.

- [References](#references)

Tip: If you want to get out of the virtual environment just type

    deactivate

## Bibliotecas Python

### Pandas
- Leitura de Excel: Utiliza pd.read_excel().

- Conversão para JSON: Utiliza DataFrame.to_json().

- Instalação: pip install pandas openpyxl (para suporte a arquivos .xlsx).

Exemplo:

    import pandas as pd

    # Ler arquivo Excel
    df = pd.read_excel('arquivo.xlsx')

    # Converter para JSON
    json_data = df.to_json(orient='records')

### OpenPyXL
- Leitura de Excel: Utiliza openpyxl.load_workbook().

- Conversão para JSON: Você precisará converter manualmente os dados lidos.

- Instalação: pip install openpyxl.

Exemplo:

    from openpyxl import load_workbook
    import json

    # Ler arquivo Excel
    wb = load_workbook('arquivo.xlsx')
    sheet = wb.active

    # Converter para JSON
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    json_data = json.dumps(data)

### XlsxWriter
- Leitura de Excel: Não suporta leitura, apenas escrita.

- Conversão para JSON: Você pode usar outra biblioteca para a conversão, como json.

- Instalação: pip install XlsxWriter.

### Excel to JSON Converter
- Leitura de Excel e Conversão para JSON: Específica para essa tarefa.

- Instalação: pip install excel2json.

Exemplo:

    from excel2json import excel2json

    # Converter Excel para JSON
    json_data = excel2json('arquivo.xlsx')

### Pyxlsb
- Leitura de arquivos Excel em formato binário (.xlsb).

- Conversão para JSON: Você precisará converter manualmente os dados lidos.

- Instalação: pip install pyxlsb.

Exemplo:

    from pyxlsb import open_workbook
    import json

    # Ler arquivo Excel .xlsb
    with open_workbook('arquivo.xlsb') as wb:
        with wb.get_sheet(1) as sheet:
            data = [row for row in sheet.rows()]
    json_data = json.dumps(data)

### json2xls
- Conversão de JSON para Excel: Específica para essa tarefa.

- Instalação: pip install json2xls.

Exemplo:

    from json2xls import json2xls

    # Converter JSON para Excel
    json_data = [{"nome": "Exemplo", "idade": 30}]
    xls = json2xls(json_data)
    with open('output.xlsx', 'wb') as f:
        f.write(xls)
