# produtor.py

import socket

HOST = 'localhost'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print("=" * 50)
print(" PRODUTOR CONECTADO ")
print("=" * 50)

while True:

    mensagem = input("\nDigite a requisição (ou sair): ")

    if mensagem.lower() == "sair":
        break
    client.send(mensagem.encode())

    resposta = client.recv(1024).decode()

    print(f"[SERVIDOR] {resposta}")

client.close()

print("\nConexão encerrada.")