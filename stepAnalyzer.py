class StepAnalyzer:
    def __init__(self, steps):
        self.steps = sorted(steps, key=lambda x: (x[0], x[1]))
        self.minX = min(steps, key=lambda x: x[0])
        self.maxX = max(steps, key=lambda x: x[0])
        self.minY = min(steps, key=lambda x: x[1])
        self.maxY = max(steps, key=lambda x: x[1])
