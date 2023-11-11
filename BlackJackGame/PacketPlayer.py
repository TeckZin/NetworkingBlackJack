from BlackJackGame import Player


class PacketPlayer:
    player = Player


    ip = str
    port = int

    def __init__(self, tf: bool, ip: str, port: int):
        self.ip = ip
        self.port = port
        if tf:
            self.housePacket()
        else:
            self.playerPacket()

    def housePacket(self) -> bool:
        return True

    def playerPacket(self) -> bool:
        return False

    def setPlayer(self, player: Player):
        self.player = player

    def getIp(self) -> str:
        return self.ip


