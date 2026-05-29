import socket
import threading
from queue import Queue

HOST = 'localhost'
PORT = 5000

fila = Queue()


MAX_PRODUTORES = 3
produtores_conectados = 0

def atender_cliente(conn, addr):

    global produtores_conectados

    print(f"\n[+] Cliente conectado: {addr}")

    while True:

        try:

            mensagem = conn.recv(1024).decode()

            if not mensagem:
                break

            if mensagem == "GET":

                if not fila.empty():

                    item = fila.get()

                    print(f"[SERVIDOR CONSUMIDOR] Removeu da fila: {item}")

                    conn.send(item.encode())

                else:

                    conn.send("FILA_VAZIA".encode())

            else:

                print(f"[PRODUTOR] Mensagem recebida: {mensagem}")

                fila.put(mensagem)

                print(f"[FILA] Total de itens: {fila.qsize()}")

                conn.send("Mensagem adicionada na fila".encode())

        except:

            print(f"[-] Cliente desconectado: {addr}")

            break


    produtores_conectados -= 1

    print(f"[INFO] Produtores conectados: {produtores_conectados}")

    conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("=" * 50)
print(" SERVIDOR PRODUTOR INICIADO ")
print(f" HOST: {HOST}")
print(f" PORTA: {PORT}")
print("=" * 50)


while True:

    conn, addr = server.accept()


    if produtores_conectados >= MAX_PRODUTORES:

        print(f"[LIMITE] Conexão recusada: {addr}")

        conn.send("LIMITE_ATINGIDO".encode())

        conn.close()

        continue

    produtores_conectados += 1

    print(f"[INFO] Produtores conectados: {produtores_conectados}")

    conn.send("CONECTADO".encode())

    thread = threading.Thread(
        target=atender_cliente,
        args=(conn, addr)
    )

    thread.start()