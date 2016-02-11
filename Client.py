import re
import socket
import time
import sys
import ssl

HOST = 'localhost'
PORT = 5004


context = ssl.create_default_context()
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
# use the cacert.pem the check whether the certificate can be trusted
context.load_verify_locations("/cacert.pem")

#context = ssl.create_default_context()

conn = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname="Jun Lu")
conn.connect(("localhost", PORT))

# send the command message
conn.sendall(b'CMD_short:0')


# receive data
received = 0
while True:
    data = conn.recv(10000).decode()
    if not data:
        break
    received += 1
    print (data)
    time.sleep(0.5)

# print the times of recv() invoked
print(str(received) + ' messages received!')

conn.close()


