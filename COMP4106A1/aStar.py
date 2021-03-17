
import numpy as np
from SearchEntry import SearchEntry
#Final_Version
my_data = np.genfromtxt('input.csv', dtype=str, delimiter=',', autostrip=True)
ht = my_data
height = len(my_data[0])
width = len(my_data)
#print(width)
#print(height)

def AStarSearch(map, source, dest, temp_explored):  # source:start，dest是End

    def getNewPosition(map, locatioin, offset):  # 向下一个节点移动
        x, y = (location.x + offset[0], location.y + offset[1])
        if x < 0 or x >= map.width or y < 0 or y >= map.height:
            return None
        return (x, y)

    def getPositions(map, location):
        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        poslist = []
        for offset in offsets:
            pos = getNewPosition(map, location, offset)
            if pos is not None:

                flag = pos==dest.getPos()
                #print(flag)
                if(flag==True):
                    ht[pos[0]][pos[1]] = 0
                #print(ht[pos[0]][pos[1]],pos)
                if(ht[pos[0]][pos[1]]=='S'):
                    ht[pos[0]][pos[1]]=0
                if(ht[pos[0]][pos[1]]!='X' and ht[pos[0]][pos[1]]!='G' ):#and ht[pos[0]][pos[1]]!='G')
                    poslist.append(pos)
        # for i in poslist:
        #     temp_explored.append(i)

        return poslist

    # h(n)
    def calHeuristic(pos, dest):
        return abs(dest.x - pos[0]) + abs(dest.y - pos[1])

    # check if the position is in list
    def isInList(list, pos):
        if pos in list:
            return list[pos]
        # print(list)
        return None

    # add available adjacent positions
    def addAdjacentPositions(map, location, dest, openlist, closedlist):
        poslist = getPositions(map, location)

        for pos in poslist:
            # if position is already in closedlist, do nothing
            if isInList(closedlist, pos) is None:
                findEntry = isInList(openlist, pos)
                h_cost = calHeuristic(pos, dest)

                g_cost = location.g_cost + int(ht[pos[0], pos[1]])
                # temp_explored.append(pos)

                if findEntry is None:
                    # if position is not in openlist, add it to openlist
                    openlist[pos] = SearchEntry(pos[0], pos[1], g_cost, g_cost + h_cost, location)

                elif findEntry.g_cost > g_cost:

                    findEntry.g_cost = g_cost
                    findEntry.f_cost = g_cost + h_cost
                    findEntry.pre_entry = location.pre_entry

    # find a least cost position in openlist, return None if openlist is empty
    def getFastPosition(openlist):
        fast = None
        for entry in openlist.values():

            if fast is None:
                fast = entry
            elif fast.f_cost > entry.f_cost:
                fast = entry

        return fast

    openlist = {}
    closedlist = {}
    #print("Start:",source)
    #print("End:",dest)
    location = SearchEntry(source[0], source[1], 0.0)

    dest = SearchEntry(dest[0], dest[1], 0.0)
    openlist[source] = location
    route = [[dest.x, dest.y]]
    while True:
        location = getFastPosition(openlist)
        if location is None:  # not found valid path
            print("Can't find valid path for ",dest.getPos())
            # closedlist[location.getPos()] = location
            # openlist.pop(location.getPos())
            # addAdjacentPositions(map, location, dest, openlist, closedlist)
            # # print("open list:", openlist)
            # print("closed list:", closedlist.keys())
            # temp_explored.append(closedlist.keys())
            # temp_explored.append(dest)
            #print("temp_in_astar", temp_explored)
            return -1, [], temp_explored
            #break

        if location.x == dest.x and location.y == dest.y:
            break

        closedlist[location.getPos()] = location
        #print("locartion is ",location.getPos())
        openlist.pop(location.getPos())
        addAdjacentPositions(map, location, dest, openlist, closedlist)
        # print("open list:", openlist)
        #print("closed list:", location.getPos())
        temp_explored.append(location.getPos())
        #temp_explored.append(dest)

    while location.pre_entry is not None:
        location = location.pre_entry

        route.append([location.x, location.y])

    optimal=np.array(route)

    temp_optimal = optimal.copy()
    cl = np.array(route)
    c=0
    i=0
    while(i<len(cl)):
        # print(ht[cl[i][0]][cl[i][1]])
        c+=int(ht[cl[i][0]][cl[i][1]])
        i+=1

    temp_cost = c
    temp_explored.append(dest.getPos())
    return temp_cost, temp_optimal, temp_explored





