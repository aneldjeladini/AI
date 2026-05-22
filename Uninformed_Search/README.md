# 🔍 Uninformed Search

> A collection of classic AI problems solved using **uninformed (blind) search** algorithms — BFS, DFS, IDS, and more — implemented in Python.


### 1. Repair Robot

**Problem Description**

A `10×10` grid contains a robot, two machines **M1** and **M2**, and parts needed to repair each machine. The robot must collect all required parts and repair both machines — navigating around wall-blocked tiles — using the **minimum number of actions**.

<img width="340" height="327" alt="repair_robot" src="https://github.com/user-attachments/assets/20524295-0880-4bdf-bbe3-96f80bd4689a" />


**Rules & Constraints**

- The robot moves in 4 directions or performs a repair action:
  ```
  dir = {"Up": (0, +1), "Down": (0, -1), "Left": (-1, 0), "Right": (+1, 0)}
  ```
- **M1 must be repaired before M2.** Parts for M2 cannot be collected until M1 is repaired.
- The robot may stand on a machine tile without having collected all parts, but **cannot repair until all parts are collected**.
- Stepping on an M2 part tile before M1 is repaired is allowed, but **the part is not collected**.
- Repairing a machine requires **`s` consecutive `"Repair"` actions** on the machine's tile. If the robot leaves the tile mid-repair, the repair **resets**.

**Input Format**

```
x,y             ← Robot starting position
m1_x,m1_y      ← Machine M1 position
s1              ← Steps to repair M1
m2_x,m2_y      ← Machine M2 position
s2              ← Steps to repair M2
m1              ← Number of parts for M1
x11,y11         ← Part positions for M1
...
m2              ← Number of parts for M2
x21,y21         ← Part positions for M2
...
```

> Grid size and wall positions are **fixed** across all test cases. Wall positions are initialized in the starter code.

**Goal:** Find the **shortest sequence of actions** to repair both machines.

<img width="1383" height="336" alt="repairRobotTestcases" src="https://github.com/user-attachments/assets/e2a6e57a-1ae2-4865-a846-a2fdd6cc397a" />


---

### 2. Snake

**Problem Description**

On a `10×10` board, a snake must eat all **green apples** while avoiding **red (poisonous) apples**, using the **minimum number of moves**.

<img width="618" height="286" alt="snake" src="https://github.com/user-attachments/assets/1eedaf93-9ad8-4399-a385-ee285bffbb2b" />


**Initial State**

- The snake initially occupies **3 cells**: 1 head + 2 body segments.
- Each green apple eaten causes the **body to grow by one cell** at the tail.

**Actions**

| Action | Description |
|---|---|
| `Move forward` | Move one cell in the current direction |
| `Turn right` | Move one cell to the right |
| `Turn left` | Move one cell to the left |

**Constraints**

- The snake **cannot collide with itself** (head hitting any body segment).
- The snake **cannot move outside the board**.
- Red apples are **fatal** — they must be avoided entirely.

**Input** (provided via starter code)

- `crveni_jabolki` — list of tuples with red apple positions `(x, y)`
- `zeleni_jabolki` — list of tuples with green apple positions `(x, y)`

> Board coordinates use a standard `(x, y)` system starting from zero. Board layout and snake's initial position are **fixed** across all test cases.

**Output:** A single `print()` call returning the **minimum sequence of moves** to eat all green apples.

---

### 3. Pacman

**Problem Description**

On a `10×10` board with obstacles, a character must eat **all dots** on the board using the **minimum number of moves**.

<img width="440" height="437" alt="pacman1" src="https://github.com/user-attachments/assets/61d62fa9-958b-44f1-a0a6-99ae43fa3045" />

<img width="410" height="225" alt="pacman2" src="https://github.com/user-attachments/assets/7da66e0c-e800-4dbf-98d8-b657b14852f5" />


**Actions**

| Action | Description |
|---|---|
| `Move forward` | Move one cell forward (blue) |
| `Move backward` | Move one cell backward (red) |
| `Turn left` | Move one cell to the left (gray) |
| `Turn right` | Move one cell to the right (green) |

> Colors in parentheses refer to the movement diagram in Figure 2.

**Constraints**

- The character **cannot move into obstacle tiles**.
- The **order of actions** in the successor function is important for reproducibility:
  ```
  Move forward → Move backward → Turn left → Turn right
  ```

**Input** (from standard input)

```
x y             ← Initial character position
direction       ← Facing direction: 'east', 'west', 'north', 'south'
n               ← Number of dots
x1 y1           ← Dot positions (one per line)
...
```

> Obstacle positions and board layout are **fixed** across all test cases. Initial position and dot positions change per test case.

**Output:** A single `print()` call returning the **minimum sequence of moves** to eat all dots.

---

### 4. Molecule

**Problem Description**

Three atoms — **H1**, **O**, and **H2** — are placed on a `7×9` board with grey obstacle tiles. The player must push the atoms into the shape of a **water molecule (H₂O)** using the **fewest moves**.

<img width="501" height="298" alt="molecule" src="https://github.com/user-attachments/assets/57711523-d3d7-4605-98b0-22f5df80e316" />


**Movement Rules**

- Each move: choose **one atom** and **push it** in one of four directions.
- The atom **slides** in that direction until it hits an obstacle or another atom, stopping in the adjacent cell.
- Atoms **cannot leave the board** and **cannot rotate**.
- H1 and H2 are **distinct** atoms (H1 has a right-link, H2 has a left-link).

**Actions**

| Action | Description |
|---|---|
| `RightX` | Move atom X to the right |
| `LeftX` | Move atom X to the left |
| `UpX` | Move atom X up |
| `DownX` | Move atom X down |

> Where `X` ∈ `{H1, O, H2}`

**Goal:** Arrange all three atoms into the target molecule configuration in **any valid position** on the board.

> Board layout and obstacle positions are **fixed**. Starting positions of all three atoms change per test case.

**Output:** A single `print()` call returning the **minimum movement sequence**.

---

### 5. Tower of Hanoi

**Problem Description**

`N` circular pillars are arranged in a row. On one pillar, `M` stone blocks of different sizes are stacked as a tower (largest at the bottom). The goal is to **move the entire tower to a target pillar**, preserving the original order, in the **minimum number of steps**.

<img width="491" height="268" alt="hanoi" src="https://github.com/user-attachments/assets/eb860900-ac1d-4397-8ff1-db50244ae56c" />


**Rules**

- Only the **top block** of any pillar may be moved at each step.
- A block may only be placed on another pillar if it is **smaller than the current top block** of that pillar, or if the pillar is **empty**.

**Input** (from standard input, handled in starter code)

- Each pillar is represented as a **tuple** of integers (block sizes, top to bottom).
- Initial and goal states are read from standard input.

**Output Format**

Print the **minimum number of steps**, followed by the sequence of moves:

```
<minimum steps>
MOVE TOP BLOCK FROM PILLAR i TO PILLAR j
MOVE TOP BLOCK FROM PILLAR i TO PILLAR j
...
```

---

### 6. Stars

**Problem Description**

A **knight**, a **bishop**, and **three stars** are placed on an `8×8` chessboard. Both figures must work together to **collect all three stars** using the **minimum number of total moves**.

<img width="317" height="312" alt="stars1" src="https://github.com/user-attachments/assets/e7a21e23-dfbb-4fd2-81d0-dbfc2bd183d9" />


**Movement Rules**

**Knight** — moves in an **L-shape** (Macedonian letter Г), with up to 8 possible landing positions:

<img width="300" height="297" alt="stars2" src="https://github.com/user-attachments/assets/4be45747-c986-420e-84fc-58b92013e60a" />


| Move | Name | Direction |
|---|---|---|
| `K1` | Knight move 1 | Up + Up + Left |
| `K2` | Knight move 2 | Up + Up + Right |
| `K3` | Knight move 3 | Right + Right + Up |
| `K4` | Knight move 4 | Right + Right + Down |
| `K5` | Knight move 5 | Down + Down + Right |
| `K6` | Knight move 6 | Down + Down + Left |
| `K7` | Knight move 7 | Left + Left + Down |
| `K8` | Knight move 8 | Left + Left + Up |

**Bishop** — moves **one step diagonally** in one of four directions:

<img width="288" height="291" alt="stars3" src="https://github.com/user-attachments/assets/38962123-bdf1-42e0-8a22-288a488486f9" />


| Move | Name | Direction |
|---|---|---|
| `B1` | Bishop move 1 | Up-Left |
| `B2` | Bishop move 2 | Up-Right |
| `B3` | Bishop move 3 | Down-Left |
| `B4` | Bishop move 4 | Down-Right |

**Constraints**

- A star is collected when either figure **lands on its tile**.
- The two figures **cannot occupy the same position** at any time.
- Neither figure **can leave the board**.
- Figures **do not attack each other** — only collecting stars matters.
- The sequence in which the figures are moved is **arbitrary** — either can be moved at any step.

> Board layout is fixed (`8×8`). Star positions and starting positions of both figures change per test case. Input is handled by the starter code.

**Output:** A single `print()` call returning the **minimum move sequence** for both figures to collect all three stars.

---

### 7. Explorer

**Problem Description**

A little man must reach his **home** on a board, while two **moving obstacles** patrol the board vertically. If the man and an obstacle occupy the same tile, the man is destroyed.

<img width="666" height="246" alt="explorer" src="https://github.com/user-attachments/assets/657ad74f-82a5-4a9a-9b3e-98643b2eed34" />


**Movement Rules**

- The man moves **one tile** per step: `Up`, `Down`, `Left`, or `Right`.
- **Obstacle 1** moves **downward** initially; **Obstacle 2** moves **upward** initially.
- Each obstacle moves **one tile per step** in sync with the man's movement.
- When an obstacle reaches the **end of the board**, it **reverses direction** and continues.
- If the man and an obstacle are on the **same tile**, the man is **destroyed** — this state is invalid.

**Actions**

| Action | Description |
|---|---|
| `Right` | Move the man one position right |
| `Left` | Move the man one position left |
| `Up` | Move the man one position up |
| `Down` | Move the man one position down |

> Board layout, obstacle starting positions, and initial movement directions are **fixed** across all test cases. The man's starting position and the house position change per test case. Input is handled by the starter code.

**Output:** A single `print()` call returning the **movement sequence** that brings the man to the house.

---

### 8. Strip

**Problem Description**

On a strip of `L` cells, `N` numbered disks are placed in the first `N` cells in increasing order. The goal is to move all disks to the **last `N` cells** in **decreasing order**, using the **minimum number of moves**.

<img width="1087" height="197" alt="strip" src="https://github.com/user-attachments/assets/6aee3407-c64a-4e5a-af4e-a09f5657509e" />


**Movement Rules**

A disk can be moved in two ways:

- **One step** — into an **adjacent empty cell** (left or right).
- **Jump** — **over exactly one adjacent disk** into the empty cell beyond it (the jumped-over cell must contain a disk, the destination must be empty).

Disks **cannot move outside the strip**.

**Actions**

| Action | Description |
|---|---|
| `R1: Disk i` | Move disk `i` one cell to the right (adjacent empty) |
| `R2: Disk i` | Move disk `i` over one cell to the right (jump) |
| `L1: Disk i` | Move disk `i` one cell to the left (adjacent empty) |
| `L2: Disk i` | Move disk `i` over one cell to the left (jump) |

> The **order of actions** in the successor function is important: `R1 → R2 → L1 → L2`, applied for each cell on the strip sequentially from the beginning. Deviating from this order may yield a valid but different solution path.

**Input** (from standard input)

```
N       ← Number of disks
L       ← Length of the strip
```

**Output:** A single `print()` call returning the **minimum move sequence** to bring all disks to their goal positions.

---

### 9. Balls

**Problem Description**

On an `N×N` board (where `N > 3` is an odd number), indistinguishable balls are placed on usable cells. By jumping one ball over an adjacent ball in one of **six directions**, the jumped-over ball is **removed**. The goal is to reduce the board to **exactly one ball**, placed in the **central cell of the first row**.

<img width="1366" height="484" alt="balls_combined" src="https://github.com/user-attachments/assets/f8248a60-e789-4b82-a556-acf927e3cc87" />


**Movement Rules**

- Select a ball and jump it **over an adjacent ball** in one of six directions.
- The **jumped-over** cell must contain a ball; the **landing** cell must be empty.
- The jumped-over ball is **removed** after the move.
- Balls **cannot move outside the board**.
- Black-colored cells are **unusable** — balls can never be placed there.

**Actions**

| Action | Description |
|---|---|
| `Up Left: (x=x_val, y=y_val)` | Jump the ball at `(x_val, y_val)` in the up-left direction |
| `Up Right: (x=x_val, y=y_val)` | Jump the ball at `(x_val, y_val)` in the up-right direction |
| `Down Left: (x=x_val, y=y_val)` | Jump the ball at `(x_val, y_val)` in the down-left direction |
| `Down Right: (x=x_val, y=y_val)` | Jump the ball at `(x_val, y_val)` in the down-right direction |
| `Left: (x=x_val, y=y_val)` | Jump the ball at `(x_val, y_val)` to the left |
| `Right: (x=x_val, y=y_val)` | Jump the ball at `(x_val, y_val)` to the right |

> Coordinates follow the standard `(x, y)` coordinate system.

**Input** (from standard input)

```
N M             ← Board width and height
k               ← Number of balls
x1 y1           ← Ball positions (one per line)
...
o               ← Number of obstacles
x y             ← Obstacle position
```

> Board shape is **fixed** across all test cases. Board size `N`, number of balls, and obstacle positions change per test case.

**Output:** A single `print()` call returning the **minimum sequence of moves** (minimum balls clicked) to reach the goal state.

<img width="432" height="203" alt="Balls_TestCases" src="https://github.com/user-attachments/assets/b905a817-671a-4dc7-be9a-644a7ccd3fdf" />

---

### 10. Squares

**Problem Description**

On a `5×5` board, **5 gray squares** are placed at random positions. Each square has an index that determines its **target position on the left diagonal** of the board. The goal is to move all squares to their correct diagonal positions using the **minimum number of moves**.

<img width="717" height="372" alt="squares_combined" src="https://github.com/user-attachments/assets/22a7c910-f9fb-4516-a857-9711f4cb7dbd" />


**Movement Rules**

- Each move: choose **one square** and move it **one step** in one of four directions.
- A square **cannot move outside the board**.
- **Multiple squares may occupy the same position** simultaneously.

**Actions** are named: `Move square X up/down/left/right` (where `X` is the square's index 1–5).

**Successor Function Order**

Actions are tried in the following order: for each square (1 → 5), try `up`, `down`, `left`, `right`.

**State Representation**

The state is a tuple of `(x, y)` positions ordered by square index:

```python
# Example: initial state from Figure 1
state = ((2, 4), (3, 1), (4, 1), (1, 2), (0, 0))
```

> Board size is **fixed** (`5×5`). Square positions are read from standard input and change per test case. Validity checking is handled by the provided `check_valid` function.

<img width="476" height="187" alt="squaresTestCases" src="https://github.com/user-attachments/assets/3395343a-9af5-4c30-b8ed-7286f510f3ca" />

---

### 11. Footballer

**Problem Description**

On an `8×6` board, a man must **push a ball into the goal** (marked in gray) while avoiding **static opponents** (marked in blue). The man pushes the ball by moving into the ball's tile in a given direction.

<img width="402" height="302" alt="footballer" src="https://github.com/user-attachments/assets/869b195b-d061-44da-901e-6323eab7f7a4" />


**Movement Rules**

- The man can move in **5 directions**: `up`, `down`, `right`, `up-right`, `down-right`.
- If the ball is **directly in front** of the man in his movement direction, the ball is **pushed** one step in that direction.
- The man **cannot occupy** the same tile as the ball or any opponent.
- The ball **cannot be placed on or adjacent** (horizontally, vertically, or diagonally) to any opponent's tile.

**Actions**

| Action | Condition |
|---|---|
| `Move man up/down/right/up-right/down-right` | Man moves, ball not pushed |
| `Push ball up/down/right/up-right/down-right` | Man moves and pushes the ball |

**Implementation Requirements**

- Implement the **successor function** for all 5 movement directions.
- Implement **`goal_test`** — checks if the ball is in the goal area.
- Implement **`check_valid`** — checks that the man and ball positions are legal.

> Board size is **fixed** (`8×6`). Opponent and goal positions are **fixed** across all test cases. Man and ball starting positions change per test case and are read from standard input.

**Goal:** Find the **minimum number of steps** to push the ball into the goal.

---

### 12. Two Boxes

**Problem Description**

On a `5×5` board, a person must **push two boxes** into the **bottom-right corner** of the board (marked in red). The person can push a box by moving into its tile — but boxes can only be **pushed, not pulled**. Only **one box may occupy a single position** at a time.

<img width="397" height="376" alt="two_boxes" src="https://github.com/user-attachments/assets/bbaa0564-7530-4bbd-a055-063ce43679e3" />


**Movement Rules**

- The person moves **one step** per action: `up`, `down`, `left`, or `right`.
- If a box is in the direction of movement, it is **pushed one step** in that direction.
- A box **cannot be pulled**.
- **Two boxes cannot share the same tile**.

**Actions**

| Action | Condition |
|---|---|
| `Move man up/down/left/right` | Person moves, no box pushed |
| `Push box 1/2 up/down/left/right` | Person moves and pushes box 1 or 2 |

> Actions are tried in order: `up → down → left → right`.

**State Representation**

The state is a tuple of `(x, y)` positions for the person and both boxes:

```python
# Example: initial state from Figure 1
state = ((0, 0), (2, 2), (3, 3))  # (person, box1, box2)
```

**Implementation Requirements**

- Implement the **successor function** with actions in the order: `up`, `down`, `left`, `right`.
- Implement **`goal_test`** — checks if both boxes are in the bottom-right corner.
- Implement **`check_valid`** — ensures the state is legal (no two boxes on the same tile, no out-of-bounds).

> Board size is **fixed** (`5×5`). Person and box starting positions change per test case and are read from standard input.

**Goal:** Find the **minimum number of steps** to push both boxes to the goal.

---


> 📌 *All problems are solved using uninformed search. No heuristics are used — only BFS, DFS, IDS, or UCS depending on the problem requirements.*
