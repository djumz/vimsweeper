import os
import keyboard  # Install with: pip install keyboard

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_matrix(n, player_pos):
    """Create an n x n matrix with the player at a specific position."""
    matrix = [["." for _ in range(n)] for _ in range(n)]
    x, y = player_pos
    matrix[x][y] = "X"
    return matrix

def display_matrix(matrix):
    """Display the matrix in the terminal."""
    for row in matrix:
        print(" ".join(row))

def move_player(pos, direction, n):
    """Move the player within bounds of the matrix."""
    x, y = pos
    if direction == "w" and x > 0:       # Move up
        x -= 1
    elif direction == "s" and x < n - 1: # Move down
        x += 1
    elif direction == "a" and y > 0:     # Move left
        y -= 1
    elif direction == "d" and y < n - 1: # Move right
        y += 1
    return x, y

def main():
    n = int(input("Enter the size of the matrix (n): "))
    player_pos = (n // 2, n // 2)  # Start in the center of the matrix

    print("Use 'w', 'a', 's', 'd' to move. Press 'q' to quit.")
    while True:
        clear_screen()
        matrix = create_matrix(n, player_pos)
        display_matrix(matrix)

        # Wait for a key press
        key = keyboard.read_event(suppress=True)
        if key.event_type == "down":  # Only handle keypress events
            move = key.name.lower()

            if move == "q":
                print("Exiting the game!")
                break
            elif move in ["w", "a", "s", "d"]:
                player_pos = move_player(player_pos, move, n)

if __name__ == "__main__":
    main()

