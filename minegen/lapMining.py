from . import stepper

class LapMining:
    def __init__(self):
        self.stepper = stepper.Stepper()
        self.steps = list()
        self.lapcount = 0
        self.step()
        self.stepper.rotateCw()

    def step(self):
        for i in range(0, 4):
            self.stepper.step()
            self.steps.append(list(self.stepper.pos))

    def stepT(self):
        self.step()
        self.stepper.rotateCcw()
        self.step()
        self.stepper.turnAround()
        self.step()
        self.step()
        for i in range(0, self.lapcount * 2 ):
            self.step()

    def lap(self):
        for i in range(0, 4):
            self.stepT()

        self.step()
        self.stepper.rotateCcw()
        self.step()
        self.stepper.rotateCw()

        self.lapcount += 1
        

