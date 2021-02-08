import socket
import threading
import os
import time

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("\t\t\t\t--------------------------------")
print("\t\t\t\t######### CHATTIFY APP #########")
print("\t\t\t\t--------------------------------")

serverip = input("\n\t\tEnter Your IP :")
serverport = 2222

clientip = input("\n\t\tEnter Your Friends IP :")
clientport = 2222

s.bind( (serverip,serverport) )

def send():
     while True:
            msg = input("Your Message : ").encode()
            s.sendto(msg,(clientip,clientport))
            if msg.decode() == "exit" or msg.decode() == "quit":
                os._exit(1)
def recv():
     while True:
            msg = s.recvfrom(1024)
            if msg[0].decode() == "exit" or msg[0].decode() == "quit":
                os._exit(1)
            print('\n\t\t\t\t\t\tReceived Msg : '+msg[0].decode())
            time.sleep(10)

t1 = threading.Thread(target=recv)
t1.start()

t2 = threading.Thread(target=send)
t2.start()

