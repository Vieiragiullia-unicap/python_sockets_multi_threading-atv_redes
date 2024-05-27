import socket
import threading

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

# funcão para receber mensagens do servidor
def receive(msg):
    while True:
        msg_lengh = client.recv(HEADER).decode(FORMAT)
        if msg_lengh:
            msg_lengh = int(msg_lengh)
            msg = client.recv(msg_lengh).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                print(msg)
            
            except: print(Exception)
            client.close()
            break
            
# Função para enviar mensagens ao servidor
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

# Inicia a thread para receber mensagens
receive_thread = threading.Thread(target=receive)
receive_thread.start()

client.close()
send("Hello World")
input()
#send("Hello Matt")
#input()
#send("Hello Everyone")
#input()
#send(DISCONNECT_MESSAGE)
