from collections import deque

goal_state = [1,2,3,4,5,6,7,8,0]

def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = index // 3, index % 3
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for r,c in moves:
        new_row, new_col = row + r, col + c
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = state[:]
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(new_state)
    return neighbors

def bfs(start):
    visited = set()
    queue = deque([(start, [])])
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path + [state]
        visited.add(tuple(state))
        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in visited:
                queue.append((neighbor, path + [state]))
    return None

print("Enter the initial 8 puzzle state (use 0 for blank)")
start_state = list(map(int, input("Enter 9 numbers separated by space: ").split()))

solution = bfs(start_state)

if solution:
    print("Solution found!")
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print()
else:
    print("No solution found.")
