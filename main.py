import numpy as np
from mlsocket import MLSocket

class numpysocket():
    def __init__(self):
        pass

    def __enter__(self):
        return self

    @staticmethod
    def startServer(server_ip, port):
        with MLSocket() as s:
            s.bind((server_ip, port))
            s.listen()
            conn, address = s.accept()
            print('connection established')

            with conn:
                array = conn.recv(1024) # This will block until it receives all the data send by the client, with the step size of 1024 bytes.
            
        return array

    @staticmethod
    def startClient(server_ip, port):
        array = np.random.randint(0,255, size=(150,150))
        with MLSocket as s:
            s.connect((server_ip, port))
            s.send(array)