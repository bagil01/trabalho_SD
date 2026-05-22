import socket
import time
import random

mensagens = [

    "Pedido de pagamento",
    "Atualizacao de estoque",
    "Novo usuario cadastrado",
    "Compra realizada",
    "Solicitacao de relatorio",
    "Requisicao de login",
    "Atualizacao de perfil",
    "Pedido de suporte",
    "Processamento de compra",
    "Verificacao de dados"

]

HOST = 'localhost'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print("=" * 50)
print(" PRODUTOR CONECTADO ")
print("=" * 50)

"""while True:

    mensagem = input("\nDigite a requisição (ou sair): ")

    if mensagem.lower() == "sair":
        break
    client.send(mensagem.encode())

    resposta = client.recv(1024).decode()

    print(f"[SERVIDOR] {resposta}")

client.close()

print("\nConexão encerrada.")
"""
try:

    while True:

        mensagem = random.choice(mensagens)

        print(f"\n[ENVIANDO] {mensagem}")

        client.send(mensagem.encode())

        resposta = client.recv(1024).decode()

        print(f"[SERVIDOR] {resposta}")

        tempo = random.randint(5, 7)

        time.sleep(tempo)

except KeyboardInterrupt:

    print("\nEncerrando produtor...")
