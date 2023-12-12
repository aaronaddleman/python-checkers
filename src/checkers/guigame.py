import pygame

# class to start a pygame window
class GuiGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock

    def draw_board(self, board):
        # draw the board
        for row in board.grid:
            for col in row:
                # draw the board
                if col['color'] == 'black':
                    space_color = (0, 0, 0)
                if col['color'] == 'white':
                    space_color = (255, 255, 255)
                # draw the player peices
                if 'player' in col:
                    if col['player'] == 'white':
                        player_color = (255, 255, 255)
                    if col['player'] == 'black':
                        player_color = (0, 0, 0)
                    pygame.draw.circle(self.screen, player_color, (col['r'] * 100 + 50, col['c'] * 100 + 50), 40)
                pygame.draw.rect(self.screen, space_color, (col['r'] * 100, col['c'] * 100, 100, 100))
        pygame.display.update()
