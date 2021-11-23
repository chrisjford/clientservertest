import numpy as np
from mlsocket import MLSocket


server_ip = '164.11.72.118'
port = 5777

array = np.random.randint(0,255, size=(150,150))

with MLSocket() as s:
    s.connect((server_ip, port))

    while True:
        array = np.random.randint(0,255, size=(150,150))
        s.send(array)