import socket, pickle
from BlackJackGame import Packet


sockFile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1234

# binding any network interface to the port number
sockFile.bind(('', port))

while True:
    # the que to connect to the server
    sockFile.listen(30)

    # addr = ip, cs is the data == client socket
    while True:
        cs, addr = sockFile.accept()

        print(addr)

        dataString = cs.recv(1024)
        packet = pickle.loads(dataString)
        print(packet.hit)

        cs.send(bytes('Accept', 'utf-8'))
        cs.close()



s.close()