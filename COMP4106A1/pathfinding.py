
import numpy as np
import copy
from map import Map
from aStar import AStarSearch

my_data = np.genfromtxt('input.csv', dtype=str, delimiter=',', autostrip=True)
ht = my_data
height = len(my_data[0])
width = len(my_data)
def pathfinding(input_filename, optimal_path_filename, explored_list_filename):
    my_data = np.genfromtxt(input_filename, dtype=str, delimiter=',', autostrip=True)
    print("Current Marix")
    print(my_data)


    def startP():

        s = list(zip(*np.where(my_data == "S")))
        s1 = s[0]
        return s1

    def findE():

        e = list(zip(*np.where(my_data == "G")))
        return e


    map_original = Map(width, height)
    source = startP()
    print("Start:", source)

    dest_list1 = findE()
    dest_list = dest_list1
    print("End::", dest_list)
    final_explored_list = []
    final_cost = -1
    final_optimal = []


    for dest in dest_list:

        temp_explored = []
        #temp_explored.append(source)

        map = copy.deepcopy(map_original)

        temp_cost, temp_optimal, temp_explored = AStarSearch(map, source, dest, temp_explored)

        ht[dest[0]][dest[1]] = 'G'
        if final_cost == -1 or temp_cost < final_cost:
            final_explored_list = temp_explored
            #print("final explored", temp_explored)
            final_cost = temp_cost
            final_optimal = temp_optimal

    print("optimal path is:\n", final_optimal[::-1])
        # print('FinalEXPL:',final_explored_list)
    print("explored_list is: ", final_explored_list)
        #print("cost: ", final_cost)
        # f = final_optimal

    f = open(optimal_path_filename, "w")
    f.write(str(final_optimal[::-1]))#path[::-1] reverse list
    f.close()
    f = open(explored_list_filename, "w")
    # f.write(str(sorted(list(set(final_explored_list)))))
    f.write(str(final_explored_list))

    f.close()

    return final_cost
