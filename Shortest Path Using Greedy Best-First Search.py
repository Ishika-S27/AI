import heapq

# Grid (5x5): S = Start, G = Goal, X = Blocked, . = Free
grid = [
    ['S', '.', '.', '.', '.'],
    ['.', 'X', 'X', '.', '.'],
    ['.', '.', '.', 'X', '.'],
    ['.', 'X', '.', '.', 'G']
]

start = (0, 0)
goal = (3, 4)

# Manhattan distance function
def h(pos):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def greedy_bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    heap = [(h(start), start, [start])]  # (priority, current_position, path)

    while heap:
        _, current, path = heapq.heappop(heap)

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = current[0] + dx, current[1] + dy
            next_cell = (nx, ny)

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] != 'X' and next_cell not in visited:
                    heapq.heappush(heap, (h(next_cell), next_cell, path + [next_cell]))

    return None  # No path found

# Run the search
path = greedy_bfs(grid, start, goal)

# Print the result
if path:
    print("Path found:")
    for step in path:
        print(step)
else:
    print("No path found.")
