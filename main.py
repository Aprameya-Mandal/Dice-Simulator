import random

class Dice:
    def __init__(self, tnotdwsctmott=None):
        if tnotdwsctmott in range(1, 7):
            self.tnotdwsctmott = tnotdwsctmott # The Number Of The Dice Which Should Come The Most Of The Time
        else:
            raise ValueError("tnotdwsctmott must be in range(1, 7)")
    def roll(self):
        arr = list(range(1, 7))
        if self.tnotdwsctmott:
            for i in range(6):
                arr.insert(random.choice(range(0, 6)), self.tnotdwsctmott)
        result = random.choice(arr)
        return result, arr


if __name__ == "__main__":
    d1 = Dice(6)
    print(d1.roll())
