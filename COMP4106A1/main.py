from pathfinding import pathfinding
if __name__ == '__main__':
    optimalcost = pathfinding('input.csv','optimal.txt','explored.txt')
    print("optimal cost is:",optimalcost)
