import shutil
import os

def copiar_arquivos(origem, destino):
    try:
        # Verifica se o diretório de destino existe ou cria um novo
        if not os.path.exists(destino):
            os.makedirs(destino)

        # Lista todos os arquivos na pasta de origem
        arquivos = os.listdir(origem)

        # Copia cada arquivo para a pasta de destino
        for arquivo in arquivos:
            caminho_origem = os.path.join(origem, arquivo)
            caminho_destino = os.path.join(destino, arquivo)
            shutil.copy2(caminho_origem, caminho_destino) # shutil.copy2 - Preserva os metadata
            print(f"Arquivo {arquivo} copiado com sucesso!")

            # Grava um log
            with open("log.txt", "a") as log:
                log.write(f"Cópia do arquivo {arquivo} realizada {origem} para {destino}.\n")

        # Grava um log
       # with open("log.txt", "a") as log:
        #    log.write(f"Cópia de arquivos de {origem} para {destino} realizada.\n")

    except Exception as e:
        print(f"Erro ao copiar arquivos: {e}")

# Exemplo de uso
# pasta_origem = "caminho/para/sua/pasta/origem"
# pasta_destino = "caminho/para/sua/pasta/destino"

pasta_origem = "C://Pasta_de_Teste//Origem"
pasta_destino = "C://Pasta_de_Teste//Destino"
copiar_arquivos(pasta_origem, pasta_destino)
