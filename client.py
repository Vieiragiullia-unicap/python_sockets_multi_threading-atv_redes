import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# Whatever IP address you found from running ipconfig in terminal.
SERVER = "10.30.7.48"
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
# Cria um objeto de soquete do cliente para comunicação TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Officially connecting to the server.
client.connect(ADDR)

# Função para enviar mensagens ao servidor
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
# funcão para receber mensagens do servidor
def receive():
    while True:
        try:
            mensage = client.recv(HEADER).decode(FORMAT)
            if mensage:
                print(f"[SERVER] {mensage}")
        except OSError:
            print("Scoket error occurred.")
            break
            
# Inicia a thread para receber mensagens
receive_thread = threading.Thread(target=receive)
receive_thread.start()

while True:
    msg = input()
    send(msg)
    if msg == DISCONNECT_MESSAGE:
        break

receive_thread.join()
client.close()

