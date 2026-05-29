import socket
import time

HOST = 'localhost'
PORT = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

resposta_inicial = client.recv(1024).decode()

if resposta_inicial == "LIMITE_ATINGIDO":

    print("\n[ERRO] Limite máximo de consumidores atingido.")

    client.close()

    exit()

elif resposta_inicial == "CONECTADO":

    print("=" * 50)
    print(" CONSUMIDOR CONECTADO ")
    print("=" * 50)

try:

    while True:

        print("\n[SOLICITANDO REQUISIÇÃO...]")

        client.send("LER".encode())

        resposta = client.recv(1024).decode()

        if resposta == "FILA_VAZIA":

            print("[FILA] Nenhuma requisição disponível.")

        elif resposta == "ERRO AO CONECTAR NO SERVIDOR PRODUTOR":

            print("[ERRO] Falha ao conectar no servidor produtor.")

        else:

            print(f"[REQUISIÇÃO RECEBIDA] {resposta}")

        tempo = 7

        print(f"[AGUARDANDO {tempo}s PARA NOVA LEITURA]")

        time.sleep(tempo)

except KeyboardInterrupt:

    print("\nEncerrando consumidor...")

client.close()