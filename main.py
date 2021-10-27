import socket
import numpy as np
import io

class numpysocket():
    def __init__(self):
        pass

    @staticmethod
    def startServer():
        port=7555
        server_socket=socket.socket() 
        server_socket.bind(('',port))
        server_socket.listen(1)
        print ('waiting for a connection...')
        client_connection,client_address=server_socket.accept()
        print ('connected to '),client_address[0]
        ultimate_buffer=''
        while True:
            receiving_buffer = client_connection.recv(1024)
            if not receiving_buffer: break
            ultimate_buffer+= receiving_buffer
            print ('-'),
        final_image=np.load(io.StringIO(ultimate_buffer))['frame']
        client_connection.close()
        server_socket.close()
        print ('\nframe received')
        return final_image

    @staticmethod
    def startClient(server_address,image):
        if not isinstance(image,np.ndarray):
            print ('not a valid numpy image')
            return
        client_socket=socket.socket()
        port=7555
        
        client_socket.connect((server_address, port))
        print ('Connected to %s on port %s') % (server_address, port)
        
        f = io.StringIO()
        np.savez_compressed(f,frame=image)
        f.seek(0)
        out = f.read()
        client_socket.sendall(out)
        client_socket.shutdown(1)
        client_socket.close()
        print ('image sent')
        pass