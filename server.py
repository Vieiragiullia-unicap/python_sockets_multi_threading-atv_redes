import socket
import threading

HEADER = 64
PORT = 5050
#  SERVER = "10.1.4.60"
# Another way to get the local IP address automatically
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
print(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# lista para armazenar os clientes conectados
connections = []

# Função para lidar com a conexão de um cliente
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connections.append(conn)
    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    print(f"[DISCONNECT] {addr} disconnected.")
                    if (threading.active_count() - 2) == 0: print(f"[ACTIVE CONNECTIONS] 0")
                    else: print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 2}")
                    connected = False
                else:
                    for connection in connections:
                        if connection != conn:
                            connection.send(msg.encode(FORMAT))
                    print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))
        except Exception as e:
            print(f"Erro ao processar mensagem de {addr}: {e}")
            connected = False

    conn.close()
    if conn in connections:
        connections.remove(conn)
    
# Função para iniciar o servidor
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        # Cria uma nova thread para lidar com a conexão do cliente
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

# Inicia o servidor
print("[STARTING] server is starting...")
start()
