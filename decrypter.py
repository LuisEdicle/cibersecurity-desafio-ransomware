import os
import pyaes

# Função para descriptografar o arquivo
def decrypt_file(file_name, key):
    try:
        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Inicializar o objeto AES para descriptografar
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Gerar o nome do novo arquivo descriptografado
        new_file_name = file_name.rsplit(".", 1)[0]

        # Escrever o arquivo descriptografado
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        # Remover o arquivo criptografado original
        os.remove(file_name)

        print(f"Arquivo '{file_name}' descriptografado com sucesso!")
        print(f"Arquivo descriptografado gerado: {new_file_name}")

    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")


# Nome do arquivo criptografado e chave para descriptografia
file_name = "teste.txt.ransomwaretroll"
key = b"testeransomwares"

# Chamar a função para descriptografar
decrypt_file(file_name, key)
