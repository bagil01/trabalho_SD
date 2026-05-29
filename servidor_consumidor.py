import socket
import threading

HOST = 'localhost'
PORT = 6000


HOST_PRODUTOR = 'localhost'
PORT_PRODUTOR = 5000


MAX_CONSUMIDORES = 3
consumidores_conectados = 0


def buscar_requisicao():

    try:

        cliente_produtor = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        cliente_produtor.connect(
            (HOST_PRODUTOR, PORT_PRODUTOR)
        )

        cliente_produtor.send("GET".encode())

        resposta = cliente_produtor.recv(1024).decode()

        cliente_produtor.close()

        return resposta

    except:

        return "ERRO AO CONECTAR NO SERVIDOR PRODUTOR"

def atender_consumidor(conn, addr):

    global consumidores_conectados

    print(f"\n[+] Consumidor conectado: {addr}")

    while True:

        try:

            mensagem = conn.recv(1024).decode()

            if not mensagem:
                break

            print(f"[CONSUMIDOR] Solicitação recebida: {mensagem}")

            resposta = buscar_requisicao()

            print(f"[SERVIDOR PRODUTOR] Resposta: {resposta}")

            conn.send(resposta.encode())

        except:

            print(f"[-] Consumidor desconectado: {addr}")

            break


    consumidores_conectados -= 1

    print(f"[INFO] Consumidores conectados: {consumidores_conectados}")

    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("=" * 50)
print(" SERVIDOR CONSUMIDOR INICIADO ")
print(f" HOST: {HOST}")
print(f" PORTA: {PORT}")
print("=" * 50)


while True:

    conn, addr = server.accept()

    if consumidores_conectados >= MAX_CONSUMIDORES:

        print(f"[LIMITE] Conexão recusada: {addr}")

        conn.send("LIMITE_ATINGIDO".encode())

        conn.close()

        continue

    consumidores_conectados += 1

    print(f"[INFO] Consumidores conectados: {consumidores_conectados}")

    conn.send("CONECTADO".encode())


    thread = threading.Thread(
        target=atender_consumidor,
        args=(conn, addr)
    )

    thread.start()