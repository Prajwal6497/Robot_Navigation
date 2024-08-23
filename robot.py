# grid dimensions
GRID_ROWS = 4
GRID_COLS = 5

# possible directions and their corresponding movements on the grid
DIRECTIONS = {
    'N': (-1, 0),  # North: move up (decrease row)
    'E': (0, 1),   # East: move right (increase column)
    'S': (1, 0),   # South: move down (increase row)
    'W': (0, -1)   # West: move left (decrease column)
}

# possible direction changes
RIGHT_TURNS = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
LEFT_TURNS = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}

def move_robot(commands):
    # Initial position, direction
    row, col, direction = 0, 0, 'S'

    for command in commands:
        if command == 'M':
            # new position
            delta_row, delta_col = DIRECTIONS[direction]
            new_row, new_col = row + delta_row, col + delta_col
            
            # Check the new position is within the grid boundaries
            if 0 <= new_row < GRID_ROWS and 0 <= new_col < GRID_COLS:
                row, col = new_row, new_col
        elif command in DIRECTIONS:
            # Change the direction
            if command == direction:
                continue  
            direction = command

    # Return the final position and direction
    return (row, col, direction)

if __name__ == "__main__":
    commands = input("Enter the command sequence: ")
    final_position = move_robot(commands)
    print(f"Robot Location: {final_position}")
