


class Packet:
    deck = [str]
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

    def setDeck(self, deck: list[str]):
        self.perviousDeck = self.deck
        self.deck = deck


    def setHit(self, hit: bool):
        self.hit = hit


