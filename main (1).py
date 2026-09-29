print("Hello this is treasure hunt")
print("lets find out the treasure")

room_map = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["G"],
    "G": [""]
}

print("    A    ")
print("   / \\   ")
print("  B   C  ")
print("   \\ /   ")
print("    D    ")
print("    -    ")
print("    G    ")

print("Doors from each room", room_map)


# BFS - Breadth First Search
def bfs(start, goal):
    to_do = [start]
    visited = []
    order = []

    while to_do:
        room = to_do.pop(0)

        if room in visited:
            continue

        visited.append(room)
        order.append(room)

        if room == goal:
            return order

        for next_room in room_map[room]:
            if next_room and next_room not in visited and next_room not in to_do:
                to_do.append(next_room)

    return order


order = bfs("A", "G")

print("bfs checked the rooms :", order)
print("no. of rooms bfs checked", len(order))


# DFS - Depth First Search
def dfs(start, goal):
    to_do = [start]
    visited = []
    order = []

    while to_do:
        room = to_do.pop()

        if room in visited:
            continue

        visited.append(room)
        order.append(room)

        if room == goal:
            return order

        for next_room in reversed(room_map[room]):
            if next_room and next_room not in visited:
                to_do.append(next_room)

    return order


# Door costs
door_cost = {
    ("A", "B"): 1,
    ("B", "D"): 1,
    ("A", "C"): 5,
    ("C", "D"): 1,
    ("D", "G"): 1
}


def path_cost(path):
    total = 0

    for i in range(len(path) - 1):
        door = (path[i], path[i + 1])
        total = total + door_cost[door]

    return total


path1 = ["A", "B", "D", "G"]
path2 = ["A", "C", "D", "G"]

print("Path 1 A -> B -> D -> G costs:", path_cost(path1))
print("Path 2 A -> C -> D -> G costs:", path_cost(path2))


cost1 = path_cost(path1)
cost2 = path_cost(path2)

if cost1 < cost2:
    best_path = path1
    best_cost = cost1
else:
    best_path = path2
    best_cost = cost2

print("Path 1 cost:", cost1)
print("Path 2 cost:", cost2)

print()

print("The cheapest path is:", best_path, "with cost", best_cost)


# New door costs
door_cost[("A", "B")] = 4
door_cost[("A", "C")] = 1

cost1 = path_cost(["A", "B", "D", "G"])
cost2 = path_cost(["A", "C", "D", "G"])

print("New path1 (through B) cost:", cost1)
print("New path2 (through C) cost:", cost2)


# BFS and DFS order
bfs_order = bfs("A", "G")
dfs_order = dfs("A", "G")

print("BFS (Breadth First) checked:", len(bfs_order), "rooms ->", bfs_order)
print("DFS (Deep First) checked:", len(dfs_order), "rooms ->", dfs_order)


print("cheapest path:", best_path, "with cost", best_cost)

print("-" * 40)
print()

print("What we learned:")

print("* BFS checks the nearest rooms first (spreads out)")
print("* DFS dives deep down one path first")