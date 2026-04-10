class Robot:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction

    def move(self, grid):
        directions = {
            'up':    (-1, 0),
            'right': (0, 1),
            'down':  (1, 0),
            'left':  (0, -1)
        }
        dr, dc = directions[self.direction]
        while True:
            new_row = self.row + dr
            new_col = self.col + dc
            if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
                break
            if grid[new_row][new_col] == '#':
                break
            self.row = new_row
            self.col = new_col
            grid[self.row][self.col] = 'X'

    def turn(self):
        order = ['up', 'right', 'down', 'left']
        self.direction = order[(order.index(self.direction) + 1) % 4]


class Game:
    def __init__(self, grid, robot1, robot2):
        self.grid = grid
        self.robot1 = robot1
        self.robot2 = robot2

    def simulate(self):
        for _ in range(15):
            self.robot1.move(self.grid)
            self.robot1.turn()
            self.robot2.move(self.grid)
            self.robot2.turn()

    def count_cleaned(self):
        return sum(cell == 'X' for row in self.grid for cell in row)


if __name__ == "__main__":
    grid = [
        list('#..#..'),
        list('.#....'),
        list('#.....'),
        list('.#....'),
        list('...#..'),
    ]

    r1_row, r1_col, r1_dir = input().split()
    r2_row, r2_col, r2_dir = input().split()

    robot1 = Robot(int(r1_row), int(r1_col), r1_dir)
    robot2 = Robot(int(r2_row), int(r2_col), r2_dir)


    grid[robot1.row][robot1.col] = 'X'
    grid[robot2.row][robot2.col] = 'X'

    game = Game(grid, robot1, robot2)
    game.simulate()
    print(game.count_cleaned())