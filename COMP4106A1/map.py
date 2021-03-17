import numpy as np
my_data = np.genfromtxt('input.csv', dtype=str, delimiter=',', autostrip=True)
ht = my_data

class Map():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #self.ht = np.random.randint(0, altitude, (width, height))
        self.ht = my_data

