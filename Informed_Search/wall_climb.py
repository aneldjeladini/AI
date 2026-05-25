from searching_framework import Problem, astar_search


class Climb(Problem):
    def __init__(self,initial,allowed,goal=None):
        super().__init__(initial,goal)
        self.allowed = allowed
        self.grid_w = 5
        self.grid_h = 9

    dirs = {'Wait':(0,0), 'Up 1': (0,1), 'Up 2': (0,2), 'Up-right 1': (1,1),
               'Up-right 2': (2,2), 'Up-left 1': (-1,1), 'Up-left 2': (-2,2)}


    def move_house(self,hx,direction):
        if direction == 'left':
            if hx == 0:
                return hx + 1, 'right'
            return hx - 1, 'left'
        else:
            if hx == self.grid_w - 1:
                return hx - 1, 'left'
            return hx + 1, 'right'

    def valid(self,mx,my,hx,hy):
        in_bounds = 0 <= mx < self.grid_w and 0 <= my < self.grid_h
        return in_bounds and ((mx, my) in self.allowed or (mx, my) == (hx, hy))

    def successor(self, state):

        succ = {}

        man_x, man_y,house_x,house_y,house_direction = state

        for action, (x,y) in self.dirs.items():
            nmx = man_x + x
            nmy = man_y + y
            nhx,new_house_dir = self.move_house(house_x,house_direction)

            if self.valid(nmx,nmy,nhx,house_y):
                succ[f'{action}'] = nmx,nmy,nhx,house_y,new_house_dir


        return succ

    def h(self,node):
        mx, my, hx, hy, hd = node.state
        return (hy - my) // 2


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        mx,my,hx,hy,dir = state
        return (mx,my) == (hx,hy)



if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    man_pos = tuple(int(elem) for elem in input().strip().split(','))
    house_pos = tuple(int(elem) for elem in input().strip().split(','))
    house_direction = input().strip()

    initial = (man_pos[0],man_pos[1],house_pos[0],house_pos[1],house_direction)

    problem = Climb(initial,allowed)
    result = astar_search(problem)

    if result:
        print(result.solution())
    else:
        print('No solution')

