import numpy as np
import socket
from mlsocket import MLSocket
from main import numpysocket

server_ip = '164.11.72.118'
port = 9001

numpysocket.startClient(server_ip, port)