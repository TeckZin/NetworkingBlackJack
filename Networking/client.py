import socket, pickle
from BlackJackGame import Packet

def inputRequest(strike):
    if strike == 3:
        return False
    answer = str(input("Ready to connect[y/n]: "))
    if answer.upper() == "Y":
        return True
    elif answer.upper() == "N":
        return False
    return inputRequest(strike + 1)


host = socket.gethostname()

port = 1234

flag = inputRequest(0)
while flag:
    clientSocketFile = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocketFile.connect((host, port))
    packet = Packet.Packet(True)
    packet.setHit(True)
    dataString = pickle.dumps(packet)
    clientSocketFile.send(dataString)


    print(clientSocketFile.recv(50))
    flag = inputRequest(0)

clientSocketFile.close()
