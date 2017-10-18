import socket
 
StartUp=True
TCP_IP = '0.0.0.0'
TCP_PORT = 62
BUFFER_SIZE = 1024

 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while StartUp:
    data=s.recv(BUFFER_SIZE)
    s.send("CON")
    if data=="EOM":
        StartUp=False
    else:
        print(data)
while True:

    MESSAGE=input("Send: ")
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
 
    print("Received data:", data)
