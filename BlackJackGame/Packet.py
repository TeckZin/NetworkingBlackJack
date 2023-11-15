class Packect:
    deck = []
    hit = False
    perviousDeck = []




    def __init__(self, tf: bool):
        if tf:
            self.housePacket()
        else:
            self.playerPacket()

    def housePacket(self) -> bool:
        return True

    def playerPacket(self) -> bool:
        return False
