import heapq

# Directions (down, up, right, left) - prioritize down first
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def a_star(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
   
    def valid_move(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X'
   
    open_list = [(heuristic(start, goal), 0, start)]
    g_cost = {start: 0}
    came_from = {}
   
    while open_list:
        _, current_g, current = heapq.heappop(open_list)
       
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]
       
        for dx, dy in DIRECTIONS:
            nx, ny = current[0] + dx, current[1] + dy
            if not valid_move(nx, ny):
                continue
            tentative_g = current_g + grid[nx][ny]
            if (nx, ny) not in g_cost or tentative_g < g_cost[(nx, ny)]:
                g_cost[(nx, ny)] = tentative_g
                f = tentative_g + heuristic((nx, ny), goal)
                heapq.heappush(open_list, (f, tentative_g, (nx, ny)))
                came_from[(nx, ny)] = current
   
    return None

# Grid, start, and goal
grid = [
    [1, 1, 5],
    [1, 'X', 1],
    [1, 1, 1]
]

start, goal = (0, 0), (2, 2)

path = a_star(grid, start, goal)
print("Path found:", path if path else "No path found")
