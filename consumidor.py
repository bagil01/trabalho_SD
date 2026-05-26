import socket
import time
import random


HOST = 'localhost'
PORT = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print("=" * 50)
print(" CONSUMIDOR CONECTADO ")
print("=" * 50)

""" while True:

   opcao = input("\nDigite ENTER para ler uma requisição ou 'sair': ")

    if opcao.lower() == "sair":
        break

    client.send("LER".encode())

    resposta = client.recv(1024).decode()


    if resposta == "FILA_VAZIA":

        print("\n[FILA] Nenhuma requisição disponível.")

    elif resposta == "ERRO AO CONECTAR NO SERVIDOR PRODUTOR":

        print("\n[ERRO] Falha ao conectar no servidor produtor.")

    else:

        print(f"\n[REQUISIÇÃO RECEBIDA] {resposta}")

"""
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