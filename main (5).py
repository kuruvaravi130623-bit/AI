map_data = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
def is_consistent(region, color, assignment):
    for neighbor in map_data[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False

    return True
def solve_map(assignment):
    # If every region has a color, we are done
    if len(assignment) == len(map_data):
        return assignment

    # Choose the next uncolored region
    for region in map_data:
        if region not in assignment:
            break

    # Try each color
    for color in colors:
        if is_consistent(region, color, assignment):
            assignment[region] = color

            result = solve_map(assignment)

            if result is not None:
                return result

            # Backtrack
            del assignment[region]

    return None
solution = solve_map({})

print("Solution:")

for region, color in solution.items():
    print(region, "=", color)