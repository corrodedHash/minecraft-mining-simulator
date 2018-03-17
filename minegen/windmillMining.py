from . import stepper

class WindmillMining:
    def __init__(self):
        self.stepper = stepper.Stepper()
        self.steps = list()

    def walk(self, amount = 1):
        for i in range(0, amount):
            self.stepper.step()
            self.steps.append(list(self.stepper.pos))

    def generate(self, sidechannelcount):
        for k in range(0, 4):
            for i in range(0, sidechannelcount // 2):
                self.walk(8)
                self.stepper.turnAround()
                self.walk(4)
                self.stepper.rotateCw()
                self.walk((sidechannelcount // 2) * 8)
                self.stepper.rotateCw()
                self.walk(4)
                self.stepper.rotateCw()
                self.walk((sidechannelcount // 2) * 8)
                self.stepper.rotateCcw()

            self.stepper.turnAround()
            self.walk((sidechannelcount // 2) * 8)
            self.stepper.rotateCw()

