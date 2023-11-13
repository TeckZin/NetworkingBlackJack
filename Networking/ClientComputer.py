import socket



# data get send from GameMain to here to be sent of


# func

# def sendingpck para: packet

# loop to send messages to all players
def sentToALL(message, playersList):
    for player in playersList():
        if not player.isHouse:
            sentMessage(message, player.getIp(), player.getPort(), "NONE")


def sentMessage(message, ip, port, command):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((ip, port))

    clientSocket.sendall(bytes(command.encode('utf-8')))

    ACKORNACK = clientSocket.recv(50)

    clientSocket.close()

    if ACKORNACK == "ACK":
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((ip, port))

        clientSocket.sendall(bytes(message.encode('utf-8')))

        returnMessage = clientSocket.recv(50)

        clientSocket.close()

        return returnMessage

    # maybe could use this to get the hit or stand
