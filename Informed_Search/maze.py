import math

from searching_framework import Problem, astar_search

class Maze(Problem):
    def __init__(self,initial,grid_size,obstacles,goal=None):
        super().__init__(initial,goal)
        self.grid_size = grid_size
        self.obstacles = obstacles

    dirs = {'Up':(0,1), 'Down': (0,-1), 'Left': (-1,0), 'Right 2': (2,0), 'Right 3': (3,0)}

    def valid(self,x,y):
        return self.grid_size > x >= 0 and self.grid_size > y >= 0 and (x,y) not in self.obstacles

    def successor(self, state):

        succ = {}

        man_x,man_y = state


        for dir,(x,y) in self.dirs.items():
            nx = man_x + x
            ny = man_y + y

            if dir == 'Right 2':
                if not self.valid(nx-1,ny):
                    continue

            if dir == 'Right 3':
                if not (self.valid(nx-1,ny) and self.valid(nx-2,ny)):
                    continue


            if self.valid(nx,ny):
                succ[f'{dir}'] = nx,ny

        return succ


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def h(self,node):
        x, y = node.state
        gx, gy = self.goal

        dx = abs(gx - x)
        dy = abs(gy - y)

        return math.ceil(dx / 3) + dy




if __name__ == '__main__':

    board_size = int(input().strip())
    num_obstacles = int(input().strip())

    obstacles = []
    for i in range(num_obstacles):
        obstacle = tuple(int(elem) for elem in input().strip().split(','))
        obstacles.append(obstacle)

    obstacles = tuple(obstacles)

    man_pos = tuple(int(elem) for elem in input().strip().split(','))
    house_pos = tuple(int(elem) for elem in input().strip().split(','))

    problem = Maze((man_pos[0],man_pos[1]),board_size,obstacles,house_pos)
    result = astar_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("No solution")




