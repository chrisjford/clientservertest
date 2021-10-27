import numpy as np
import socket
from main import numpysocket

server_ip = '164.11.72.118'
port = 9001

numpysocket.startClient(server_ip, port)