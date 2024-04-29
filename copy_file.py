import os
import shutil
import datetime

# Função para verificar se um diretório existe e, se não, criá-lo
def criar_diretorio(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

# Diretório de origem e destino
diretorio_origem = "C:\\Pasta_de_Teste\\Origem"
diretorio_destino = "C:\\Pasta_de_Teste\\Destino"
diretorio_log = diretorio_destino  # O arquivo de log será salvo na pasta destino

# Verificar se o diretório de destino existe e, se não, criá-lo
criar_diretorio(diretorio_destino)

# Percorrer todos os arquivos no diretório de origem e subpastas
for pasta_atual, subpastas, arquivos in os.walk(diretorio_origem):
    for arquivo in arquivos:
        caminho_completo_origem = os.path.join(pasta_atual, arquivo)
        # Construir o caminho de destino preservando a estrutura de diretórios
        caminho_relativo = os.path.relpath(caminho_completo_origem, diretorio_origem)
        caminho_completo_destino = os.path.join(diretorio_destino, caminho_relativo)
        
        # Verificar se o arquivo já existe no destino
        if os.path.exists(caminho_completo_destino):
            print(f"O arquivo '{caminho_completo_destino}' já existe no destino.")
            with open(os.path.join(diretorio_log, "log_copia.txt"), "a") as log:
                log.write(f"{datetime.datetime.now()} - Arquivo '{caminho_completo_origem}' ja existe no destino '{caminho_completo_destino}'\n")
            continue

        # Criar as subpastas que não existem no destino
        diretorio_destino_pai = os.path.dirname(caminho_completo_destino)
        criar_diretorio(diretorio_destino_pai)

        # Copiar o arquivo para o destino
        try:
            shutil.copy2(caminho_completo_origem, caminho_completo_destino)
            print(f"Arquivo '{caminho_completo_origem}' copiado para '{caminho_completo_destino}'")
            with open(os.path.join(diretorio_log, "log_copia.txt"), "a") as log:
                log.write(f"{datetime.datetime.now()} - Arquivo '{caminho_completo_origem}' copiado para '{caminho_completo_destino}'\n")
        except Exception as e:
            print(f"Erro ao copiar o arquivo '{caminho_completo_origem}': {e}")
            with open(os.path.join(diretorio_log, "log_copia.txt"), "a") as log:
                log.write(f"{datetime.datetime.now()} - Erro ao copiar o arquivo '{caminho_completo_origem}': {e}\n")
