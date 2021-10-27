import numpy as np
import socket
from main import numpysocket

server_address = '164.11.72.118'
image = np.random.randint(0,255, size=(150,150))

numpysocket.startClient(server_address, image)