import socket


class PlayerServer():


    def YESORNO(self, strike, message):
        print(message)



    def hitOrStand(self, strike, message):
        print(message)
        if strike == 3:
            return "False"
        value = str(input("hit or stand: "))
        if value.upper() == "HIT":
            print("HIT")
            return "True"
        elif value.upper() == "STAND":
            print("STAND")
            return "False"
        else:
            print(f"Invalid Strike {strike + 1}")
            return self.hitOrStand(strike + 1, "")

    def runTCP(self, port):
        HITORSTAND = False
        NONE = False
        YESORNO = False
        socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socketServer.bind(('', port))

        while True:
            socketServer.listen(1000)

            while True:
                cs, addr = socketServer.accept()

                message = socketServer.recv(30)

                message = str(message.decode("utf-8"))

                if HITORSTAND:
                    HITORSTAND = False
                    cs.send(bytes(self.hitOrStand(0, message), 'utf-8'))
                    cs.close()
                    break
                if NONE:
                    NONE = False
                    cs.send(bytes("ACK", 'utf-8'))
                    cs.close()
                    break
                if YESORNO:
                    YESORNO = False
                    break


                match message:
                    case "NONE":
                        cs.send(bytes("ACK", 'utf-8'))
                        cs.close()
                        NONE = True
                        break
                    case "HitStand":
                        cs.send(bytes("ACK", 'utf-8'))
                        cs.close()
                        HITORSTAND = True
                        break
                    case "YORN":
                        YESORNO = True
                        cs.send(bytes("ACK", 'utf-8'))
                        cs.close()
                        break



                        # keep writing


    def __init__(self, port):
        self.runTCP(port)
        # TCP
        # diff port num
