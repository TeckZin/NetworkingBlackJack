import socket
from Networking import ComputerServer


# data get send from GameMain to here to be sent of


# func

# def sendingpck para: packet


def sentMessage(message, ip, port):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((ip, port))

    clientSocket.sendall(bytes(message.encode('utf-8')))

    returnMessage = clientSocket.recv(50)

    clientSocket.close()
    # maybe could use this to get the hit or stand

    return ComputerServer.listenToMessageHitorStand(port)
