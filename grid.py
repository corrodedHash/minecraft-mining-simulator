import cairo

class Grid:
    def __init__(self, steps):
        self.width = 500
        self.height = 500
        self.steps = steps 

    def draw(self, filename, blocksize):
        surface = cairo.SVGSurface(filename, self.width, self.height)
        context = cairo.Context(surface)
        for x, y in self.steps:
            if ((x + y) % 2 == 0):
                context.set_source_rgba(0, 0, 1, 0.3)
            else:
                context.set_source_rgba(0, 1, 0, 0.3)
            x = x * blocksize + self.width // 2
            y = y * blocksize + self.height // 2
            context.rectangle(x, y, blocksize, blocksize)
            context.fill()
        surface.finish()
