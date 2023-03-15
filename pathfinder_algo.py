import pygame
from queue import PriorityQueue

def heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current): #traverse from end node to start node
    traversal_path = []
    while current in came_from:
        current = came_from[current]
        traversal_path.append(current)
    return traversal_path
        

def algorithm(grid,start,end): #A* Algorithm
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from ={} #what nodes came from where so we can create the final path
    g_score = {spot: float("inf") for row in grid for spot in row} #keeps track of shortest possible node
    g_score[start]=0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start]= heuristic(start.get_pos(), end.get_pos())#how long we think it will take to get to end node

    open_set_hash = {start}

    while not open_set.empty(): #allows to close whilst running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2] #open set is a priority queue - put is to push in queue
        open_set_hash.remove(current)

        if current == end: #make final path
            pathing_list = reconstruct_path(came_from, end)
            return pathing_list

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:#allows to add to a better found path
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + heuristic(neighbour.get_pos(),end.get_pos())
                if neighbour not in open_set_hash:
                    count+=1
                    open_set.put((f_score[neighbour],count, neighbour))
                    open_set_hash.add(neighbour)
                    
        

        if current != start:
            pass #Doesn't do anything

    return False #no path found