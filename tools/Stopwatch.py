import time
class Stopwatch:
    def __init__(self):
        self.start = int(round(time.time() * 1000))

    def elapsedTime(self):
        now = int(round(time.time() * 1000))
        return (now - self.start) / 1000
