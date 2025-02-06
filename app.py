import os
import pandas as pd
import requests
from datetime import datetime

planilha_path = r"" #Aqui vc tem que colocar o caminho do excel 
pasta_destino = r"\TOMBAMENTOS" #Aqui vc tem que colocar o caminho da pasta no seu computadot

def extrair_id_do_link(url):
    if isinstance(url, str) and "drive.google.com" in url:
        if "id=" in url:
            return url.split("id=")[-1]
        elif "/d/" in url:
            return url.split("/d/")[1].split("/")[0]
    return None

def baixar_imagem(url, caminho_destino):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  
        
        with open(caminho_destino, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"\033[92mImagem salva em: {caminho_destino}\033[0m")
    except requests.exceptions.RequestException as e:
        print(f"\033[91mErro ao baixar a imagem: {e}\033[0m")

df = pd.read_excel(planilha_path, engine="openpyxl")
print(df.columns)

for index, row in df.iterrows():
    tombamento = str(row["TOMBAMENTO"]).zfill(6)  #TOMABAMENTO nome dado a minha primeira coluna (Resulmindo ele pega a coluna com nome e nisso esle se baseia em criar arquivos que estejam nessa coluna)
    pasta_tombamento = os.path.join(pasta_destino, tombamento)

    os.makedirs(pasta_tombamento, exist_ok=True)

    colunas_imagens = ["", "", "", "", "", ""] #Nome das colunas no arquivo do Excel, você coloca baseado no seu arquivo xlxs

    for coluna in colunas_imagens:
        link_drive = row[coluna]

        if pd.notna(link_drive):  
            file_id = extrair_id_do_link(str(link_drive))
            if file_id:
                nome_arquivo = f"{tombamento}.{coluna}.png" 
                caminho_destino = os.path.join(pasta_tombamento, nome_arquivo)

                url_download = f"https://drive.google.com{file_id}" #Aqui você coloca o link aonde as imgs do Google drive estão ospedadas
                baixar_imagem(url_download, caminho_destino)

print("Processo concluído!")
