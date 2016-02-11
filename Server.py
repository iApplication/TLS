import re
import socket
import time
import sys
import ssl
import select

HOST = 'localhost'
PORT = 5004

# create a context holding the key and the certificate
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="/junlu.crt", keyfile="/junlu_key.pem", password="password")

serverSocket = None
clientsConnection = []
CmdMap = dict()

# the function is for initializing socket for the server
def socketInit():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5) # listen on the port
    sock.settimeout(0.1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return sock

def acceptAndAddClient(serverSocket, clientsConnection, context):
    try:
        (client, address) = serverSocket.accept()
        print("client " + str(address) + " has connected")

        connstream = context.wrap_socket(client, server_side=True)
        # add client
        clientsConnection.append(connstream)
    except socket.timeout:
        # do nothing
        return

def readCommandAndResponse(clientsConnection):
    try:
        rlist, wlist, elist = select.select(clientsConnection, [], [], 0.1)
    except:
        return

    for sock in rlist:
        data = sock.recv(1024)
        if not data: break

        message = data.decode('utf-8')
        print(message)
        cmdIndex = message.find('CMD_short:0')

        if cmdIndex == -1:
            sock.send(b'Wrong command!\n')
        else:
            for i in range(0,15):
                sock.send(bytes('This is PMU data ' + str(i) + '\n', 'utf-8'))
            # remove client and shut down socket
            clientsConnection.remove(sock)
            sock.shutdown(socket.SHUT_RDWR)


serverSocket = socketInit()

while True:
    acceptAndAddClient(serverSocket, clientsConnection, context)
    readCommandAndResponse(clientsConnection)

