import grid
import minegen.lapMining as lapMining
import minegen.windmillMining as windmillMining

def generateLapMining():
    x = lapMining.LapMining()
    myGrid = grid.Grid(x.steps)
    myGrid.draw(filename = "lap_0.svg", blocksize = 5)

    for i in range(1, 17):
        x.lap()
        if (bin(i).count("1") == 1):
            myGrid.draw("lap_" + str(i) + ".svg", blocksize = 5)

def generateWindmillMining():
    x = windmillMining.WindmillMining()
    myGrid = grid.Grid(x.steps)
    x.generate(10)
    myGrid.draw("wm_20.svg", blocksize = 5)

generateWindmillMining()
