from collections import deque

# Initial and Goal states
start_state = ['R', 'R', 'R', '_', 'L', 'L', 'L']
goal_state = ['L', 'L', 'L', '_', 'R', 'R', 'R']

def get_successors(state):
    successors = []
    empty = state.index('_')

    # Check if a right-moving rabbit (R) can move left into the empty space
    if empty > 0 and state[empty - 1] == 'R':
        new_state = state[:]
        new_state[empty], new_state[empty - 1] = new_state[empty - 1], '_'
        successors.append(new_state)

    # R jumps over one rabbit to the left
    if empty > 1 and state[empty - 2] == 'R' and state[empty - 1] in ['L', 'R']:
        new_state = state[:]
        new_state[empty], new_state[empty - 2] = new_state[empty - 2], '_'
        successors.append(new_state)

    # Check if a left-moving rabbit (L) can move right into the empty space
    if empty < len(state) - 1 and state[empty + 1] == 'L':
        new_state = state[:]
        new_state[empty], new_state[empty + 1] = new_state[empty + 1], '_'
        successors.append(new_state)

    # L jumps over one rabbit to the right
    if empty < len(state) - 2 and state[empty + 2] == 'L' and state[empty + 1] in ['R', 'L']:
        new_state = state[:]
        new_state[empty], new_state[empty + 2] = new_state[empty + 2], '_'
        successors.append(new_state)

    return successors


# BFS implementation
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        current_tuple = tuple(current)
        if current_tuple in visited:
            continue
        visited.add(current_tuple)

        if current == goal:
            return path

        for succ in get_successors(current):
            queue.append((succ, path + [succ]))

    return None

# DFS implementation
def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        current_tuple = tuple(current)
        if current_tuple in visited:
            continue
        visited.add(current_tuple)

        if current == goal:
            return path

        for succ in reversed(get_successors(current)):
            stack.append((succ, path + [succ]))

    return None

# Helper to print the path nicely
def print_path(path, label):
    print(f"\n{label} Solution:")
    for step_num, state in enumerate(path):
        print(f"Step {step_num}: {''.join(state)}")

# Run the solutions
bfs_result = bfs(start_state, goal_state)
dfs_result = dfs(start_state, goal_state)

if bfs_result:
    print_path(bfs_result, "BFS")
else:
    print("No solution found using BFS.")

if dfs_result:
    print_path(dfs_result, "DFS")
else:
    print("No solution found using DFS.")
