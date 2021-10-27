import numpy as np
import socket
from mlsocket import MLSocket

server_ip = '164.11.72.118'
port = 9001

with MLSocket() as s:
    s.bind((server_ip, port))
    s.listen()
    conn, address = s.accept()
    print('connection established')

    with conn:
        array = conn.recv(1024) # This will block until it receives all the data send by the client, with the step size of 1024 bytes.