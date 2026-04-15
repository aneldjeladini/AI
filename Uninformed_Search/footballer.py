from searching_framework import Problem, breadth_first_graph_search


class Footballer(Problem):
    def __init__(self,initial,opponents,goal=None):
        super().__init__(initial,goal)
        self.opponents = opponents
        self.max_x = 8
        self.max_y = 6

    def check_valid(self,state):
        fx, fy, bx, by = state
        op1 = self.opponents[0]
        op2 = self.opponents[1]
        if fx < 0 or fx >= self.max_x or fy < 0 or fy >= self.max_y or bx < 0 or bx >= self.max_x or by < 0 or by >= self.max_y or (fx,fy) == (bx,by) or (fx,fy) in self.opponents or (bx,by) in self.opponents or max(abs(bx-op1[0]),abs(by-op1[1])) <= 1 or max(abs(bx-op2[0]),abs(by-op2[1]))<=1:
            return False
        return True

    def successor(self, state):

        succ = {}

        fx,fy,bx,by = state

        directions = [("up",(0,1)), ("down",(0,-1)), ("right",(1,0)), ("up-right",(1,1)), ("down-right",(1,-1))]

        for dir,(dx,dy) in directions:
            nx = fx + dx
            ny = fy + dy
            move_state = nx, ny,bx,by
            if self.check_valid(move_state):
                succ[f"Move man {dir}"] = move_state

            if (nx,ny) == (bx,by):
                nbx = bx + dx
                nby = by + dy
                push_state = nx,ny,nbx,nby
                if self.check_valid(push_state):
                    succ[f"Push ball {dir}"] = push_state



        return succ

    def goal_test(self, state):
        bx,by = state[2],state[3]
        return (bx,by) in self.goal

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]



if __name__ == '__main__':


    f_pos = tuple(map(int,input().split(',')))
    b_pos = tuple(map(int,input().split(',')))
    initial = (f_pos[0],f_pos[1],b_pos[0],b_pos[1])
    opponents = ((3,3),(5,4))
    goal = ((7,2),(7,3))
    footballer = Footballer(initial,opponents,goal)
    result = breadth_first_graph_search(footballer)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")