from collections import deque

class State:
    def __init__(self, monkey_pos, box_pos, monkey_height, has_banana):
        self.monkey_pos = monkey_pos
        self.box_pos = box_pos
        self.monkey_height = monkey_height
        self.has_banana = has_banana

    def is_goal(self):
        return self.has_banana

    def __eq__(self, other):
        return (self.monkey_pos == other.monkey_pos and
                self.box_pos == other.box_pos and
                self.monkey_height == other.monkey_height and
                self.has_banana == other.has_banana)

    def __hash__(self):
        return hash((self.monkey_pos, self.box_pos, self.monkey_height, self.has_banana))

def get_next_states(state):
    states = []
    if state.monkey_pos != state.box_pos:
        states.append(State(state.box_pos, state.box_pos, state.monkey_height, state.has_banana))
    if state.monkey_pos == state.box_pos and state.monkey_height == "floor":
        states.append(State(state.monkey_pos, state.box_pos, "on_box", state.has_banana))
    if state.monkey_height == "on_box" and state.monkey_pos == "middle":
        states.append(State(state.monkey_pos, state.box_pos, state.monkey_height, True))
    return states

def bfs(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        state, path = queue.popleft()
        if state.is_goal():
            return path
        if state not in visited:
            visited.add(state)
            for next_state in get_next_states(state):
                queue.append((next_state, path + [next_state]))
    return None

monkey_position = input("Enter monkey position (left/middle/right): ")
box_position = input("Enter box position (left/middle/right): ")

initial = State(monkey_position, box_position, "floor", False)
solution = bfs(initial)

if solution:
    print("Monkey got the banana!")
    print("Steps:")
    for step in solution:
        print("Monkey:", step.monkey_pos, "| Box:", step.box_pos, "| Height:", step.monkey_height, "| Has Banana:", step.has_banana)
else:
    print("No solution found.")
