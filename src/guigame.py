import pygame
import sys
from checkers.board import GameBoard
from checkers.player import Player

# Initialize Pygame
pygame.init()

# Window dimensions
window_width = 400
window_height = 400

# Create a Pygame window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Checkers Game")

# Colors (RGB format)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Initialize the game board and players
game_board = GameBoard()
game_board.build_board()
player_black = Player(color="black")
player_white = Player(color="white")
game_board.add_player_pieces(player_black=player_black, player_white=player_white)

# Function to draw the game board and pieces
def draw_board():
    for row in game_board.grid:
        for col in row:
            x = col['c'] * (window_width // game_board.total_cols)
            y = col['r'] * (window_height // game_board.total_rows)

            if col['color'] == 'black':
                pygame.draw.rect(window, black, (x, y, window_width // game_board.total_cols, window_height // game_board.total_rows))
            
            if col.get('player'):
                pygame.draw.circle(window, red if col['player'] == 'black' else white, (x + (window_width // game_board.total_cols) // 2, y + (window_height // game_board.total_rows) // 2), 20)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic here (e.g., handling player input, checking for game over)

    # Clear the screen
    window.fill(white)

    # Draw the game board and pieces
    draw_board()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
