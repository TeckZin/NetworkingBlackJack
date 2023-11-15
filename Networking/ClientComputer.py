import socket

# data get send from GameMain to here to be sent of


# func

# def sendingpck para: packet

# loop to send messages to all players
def sentToALL(message, playersList):
    print(playersList)
    idx = 0
    for player in playersList:
        if idx != 0:
            sentMessage(message, player.getIp(), player.getPort(), "NONE")

        idx += 1



def sentMessage(message, ip, port, command):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((ip, 1235))
    print("connected")
    clientSocket.sendall(bytes(command.encode('utf-8')))
    print(command)
    ACKORNACK = str(clientSocket.recv(50).decode())
    print(ACKORNACK)

    clientSocket.close()

    if ACKORNACK == "ACK":
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((ip, 1235))

        clientSocket.sendall(bytes(message.encode('utf-8')))

        returnMessage = str(clientSocket.recv(50).decode())

        clientSocket.close()

        return returnMessage

    # maybe could use this to get the hit or stand
