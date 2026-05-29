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


resposta_inicial = client.recv(1024).decode()


if resposta_inicial == "LIMITE_ATINGIDO":

    print("\n[ERRO] Limite máximo de produtores atingido.")

    client.close()

    exit()

elif resposta_inicial == "CONECTADO":

    print("=" * 50)
    print(" PRODUTOR CONECTADO ")
    print("=" * 50)

try:

    while True:

        mensagem = random.choice(mensagens)

        print(f"\n[ENVIANDO] {mensagem}")

        client.send(mensagem.encode())

        resposta = client.recv(1024).decode()

        print(f"[SERVIDOR] {resposta}")

        tempo = 5

        print(f"[AGUARDANDO {tempo}s]")

        time.sleep(tempo)

except KeyboardInterrupt:

    print("\nEncerrando produtor...")


client.close()