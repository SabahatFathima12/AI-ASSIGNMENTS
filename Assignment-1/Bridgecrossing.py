from collections import deque
from itertools import combinations

# Crossing times
people = {
    'Amogh': 5,
    'Ameya': 10,
    'Grandmother': 20,
    'Grandfather': 25
}

# Initial state: everyone on the left side, umbrella on left, time = 0
initial_state = (frozenset(people.keys()), frozenset(), 'left', 0)
goal_set = frozenset(people.keys())

# Generate all valid next states
def get_moves(state):
    left, right, side, time = state
    next_states = []

    if side == 'left':
        pairs = list(combinations(left, 2)) + list(combinations(left, 1))
        for group in pairs:
            duration = max(people[p] for p in group)
            new_time = time + duration
            if new_time <= 60:
                new_left = left - frozenset(group)
                new_right = right | frozenset(group)
                new_state = (new_left, new_right, 'right', new_time)
                next_states.append((new_state, group))
    else:
        for group in combinations(right, 1):
            duration = people[group[0]]
            new_time = time + duration
            if new_time <= 60:
                new_left = left | frozenset(group)
                new_right = right - frozenset(group)
                new_state = (new_left, new_right, 'left', new_time)
                next_states.append((new_state, group))

    return next_states

# Check goal condition
def is_goal(state):
    left, right, side, time = state
    return right == goal_set and side == 'right' and time <= 60

# BFS search
def bfs():
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if is_goal(state):
            return path + [(state, ())]
        if state in visited:
            continue
        visited.add(state)
        for new_state, move in get_moves(state):
            queue.append((new_state, path + [(state, move)]))
    return None

# DFS search
def dfs():
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if is_goal(state):
            return path + [(state, ())]
        if state in visited:
            continue
        visited.add(state)
        for new_state, move in reversed(get_moves(state)):
            stack.append((new_state, path + [(state, move)]))
    return None

# Pretty-printing function
def print_solution(path, label):
    print(f"\n{label} Solution:")
    for i, (state, move) in enumerate(path):
        left, right, side, time = state
        print(f"\nStep {i}:")
        print(f"  Left side: {sorted(left)}")
        print(f"  Right side: {sorted(right)}")
        print(f"  Umbrella is on: {side}")
        print(f"  Time elapsed: {time} min")
        if move:
            print(f"  Move: {', '.join(move)}")

# Run both searches
bfs_result = bfs()
dfs_result = dfs()

if bfs_result:
    print_solution(bfs_result, "BFS")
else:
    print("No solution found using BFS.")

if dfs_result:
    print_solution(dfs_result, "DFS")
else:
    print("No solution found using DFS.")
