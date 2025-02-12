import json

def ler_json(nome_arquivo):
    """Lê um arquivo JSON e exibe os dados formatados."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)  # Converte JSON para um dicionário ou lista
            print(type(dados))
            print(json.dumps(dados, indent=4, ensure_ascii=False))  # Exibe formatado
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{nome_arquivo}' não contém um JSON válido.")

# Nome do arquivo JSON a ser lido
arquivo_json = "dados.json"
ler_json(arquivo_json)
