class SearchEntry():
    def __init__(self, x, y, g_cost, f_cost=0, pre_entry=None):
        self.x = x
        self.y = y
        self.g_cost = g_cost  # g
        self.f_cost = f_cost  # f
        self.pre_entry = pre_entry  # parent

    # current node position
    def getPos(self):
        return (self.x, self.y)

