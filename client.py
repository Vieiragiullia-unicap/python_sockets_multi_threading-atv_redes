import socket

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# Whatever IP address you found from running ifconfig in terminal.
# SERVER = ""
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
    print(client.recv(2048).decode(FORMAT))

send("Hello World")
input()
send("Hello Matt")
input()
send("Hello Everyone")
input()
send(DISCONNECT_MESSAGE)
