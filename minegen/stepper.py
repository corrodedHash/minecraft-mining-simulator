class Stepper:
    def __init__(self):
        self.pos = [0, 0]
        self.direction = [0, 1]

    def step(self):
        self.pos[0] += self.direction[0]
        self.pos[1] += self.direction[1]

    def rotateCcw(self):
        tmp = self.direction[0]
        self.direction[0] = self.direction[1]
        self.direction[1] = -tmp

    def rotateCw(self):
        tmp = self.direction[0]
        self.direction[0] = -self.direction[1]
        self.direction[1] = tmp

    def turnAround(self):
        self.direction[0] = -self.direction[0]
        self.direction[1] = -self.direction[1]
