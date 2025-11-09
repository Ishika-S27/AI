import heapq

DIRS = [(1,0), (-1,0), (0,1), (0,-1)]  # down, up, right, left

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X'

def build_path(came_from, end):
    path = [end]
    while end in came_from:
        end = came_from[end]
        path.append(end)
    path.reverse()
    return path

def greedy(grid, start, goal):
    heap = [(manhattan(start, goal), start)]
    came_from = {}
    visited = set()

    while heap:
        _, current = heapq.heappop(heap)
        if current == goal:
            path = build_path(came_from, current)
            cost = sum(grid[x][y] for x,y in path)
            return path, cost
        if current in visited:
            continue
        visited.add(current)

        for dx, dy in DIRS:
            nx, ny = current[0] + dx, current[1] + dy
            if valid(grid, nx, ny) and (nx, ny) not in visited:
                if (nx, ny) not in came_from:
                    came_from[(nx, ny)] = current
                    heapq.heappush(heap, (manhattan((nx, ny), goal), (nx, ny)))
    return None, float('inf')

def astar(grid, start, goal):
    heap = [(manhattan(start, goal), 0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while heap:
        _, g, current = heapq.heappop(heap)
        if current == goal:
            path = build_path(came_from, current)
            return path, cost_so_far[current]

        for dx, dy in DIRS:
            nx, ny = current[0] + dx, current[1] + dy
            if valid(grid, nx, ny):
                new_cost = g + grid[nx][ny]
                if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                    cost_so_far[(nx, ny)] = new_cost
                    priority = new_cost + manhattan((nx, ny), goal)
                    heapq.heappush(heap, (priority, new_cost, (nx, ny)))
                    came_from[(nx, ny)] = current
    return None, float('inf')

# Example grid with costs; 'X' means blocked
grid = [
    [1, 1, 5, 1],
    [2, 'X', 1, 1],
    [2, 2, 1, 1],
    [1, 1, 1, 1]
]

start = (0, 0)
goal = (3, 3)

g_path, g_cost = greedy(grid, start, goal)
a_path, a_cost = astar(grid, start, goal)

print("Greedy Best-First Search:")
print("Path:", g_path)
print("Cost:", g_cost)

print("\nA* Search:")
print("Path:", a_path)
print("Cost:", a_cost)
