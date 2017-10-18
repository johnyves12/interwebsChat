import socket
from threading import Thread
from SocketServer import ThreadingMixIn
from datetime import datetime


TCP_IP = '0.0.0.0'
TCP_PORT = 62
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
newMessage=False
saveConversation=False
messages=['','','','','','','','','','']
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []
connections = []

codes= "100: Connection working\n101: Data received\n102: Bad checksum\n103: Executing command"
class Main:

   
        
    def main(self):
        while True:
            tcpsock.listen(4)
            print("Waiting for incoming connections...")
            global conn
            (conn, (ip,port)) = tcpsock.accept()
            
            newthread = ClientThread(ip,port)
            newthread.start()
            threads.append(newthread)
            connections.append(newthread)
            if newMessage==True:
                newMessage=False
                for connection in self.connection:
                    # update
                    connection.update(newMessg)
                    #future Mathieu: write newMessg to file if save is on
                    for i in range(9):
                        messages[i]=messages[i+1]
                    messages[9]=newMessg
                    
              
    
class ClientThread(Thread):
 
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New thread started for "+ip+":"+str(port))
        
        for i in range(len(messages)):
            conn.send(messages[i])
            conn.recv(2048)
        conn.send("EOM")
 
    def run(self):
        while True:
            data = conn.recv(2048)
            if not data: break
            print("received data:", data)
            newMessage=True
            newMessg=data
            if "/version" in data:
                 conn.send("Demo version")
 
            if "/echo" in data:
                 data = data.replace("/echo","")
                 conn.send(data)
                 
            if "/codes" in data:
                conn.send(codes)

            if "/time" in data:
                conn.send(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
    
 

 
 

 
main=Main()
main.main()
 
for t in threads:
    t.join()
