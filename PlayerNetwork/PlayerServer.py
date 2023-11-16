import socket


class PlayerServer():

    def YESORNO(self, strike, message):
        print(message)

        if strike == 3:
            return 'N'
        value = str(input("Yes or No:"))
        if value.upper() == "Y":
            return 'Y'
        elif value.upper() == 'N':
            return 'N'
        message = f"Invalid strike number {strike}"
        return self.YESORNO(strike + 1, message)

    def hitOrStand(self, strike, message):
        print(message)
        if strike == 3:
            return 'False'
        value = str(input("hit or stand: "))
        if value.upper() == "HIT":
            print("HIT")
            return 'True'
        elif value.upper() == "STAND":
            print("STAND")
            return 'False'
        else:
            message = f"Invalid Strike {strike + 1}"
            return self.hitOrStand(strike + 1, message)

    def runTCP(self, port):
        HITORSTAND = False
        NONE = False
        YESORNO = False
        WINNER = False
        socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # port = 1235
        print(port)

        socketServer.bind(('', port))
        END = False
        while not END:

            socketServer.listen(1000)

            cs, addr = socketServer.accept()

            message = str(cs.recv(1000).decode())

            if HITORSTAND:
                HITORSTAND = False
                print("YOUR TURN")
                cs.sendall(bytes(self.hitOrStand(0, message).encode('utf-8')))
                cs.close()

            if NONE:
                NONE = False
                print("GENEREAL MESSAGE \n--------------------------------")
                print(message)
                cs.sendall(bytes('ACK'.encode('utf-8')))
                cs.close()

            if YESORNO:
                print("YOUR TURN")
                YESORNO = False
                cs.sendall(self.YESORNO(0, message).encode('utf-8'))
                cs.close()

            if WINNER:
                WINNER = False
                END = True
                print(message)
                cs.sendall(bytes('ACK'.encode('utf-8')))
                cs.close()
                socketServer.close()

            match message:
                case "NONE":
                    cs.sendall(bytes('ACK'.encode('utf-8')))
                    cs.close()
                    NONE = True

                case "HITORSTAND":
                    cs.sendall(bytes('ACK'.encode('utf-8')))
                    cs.close()
                    HITORSTAND = True

                case "YORN":
                    YESORNO = True
                    cs.sendall(bytes('ACK'.encode('utf-8')))
                    cs.close()

                case "END":
                    WINNER = True
                    cs.sendall(bytes('ACK'.encode('utf-8')))
                    cs.close()

                    # keep writing

    def __init__(self, port):
        self.runTCP(port)
        # TCP
        # diff port num
