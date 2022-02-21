"""All items that are part of the checkers game."""
import logging


class GameBoard:
    """Create a game board."""

    def __init__(self, total_rows=8, total_cols=8):
        """Initialize the board with rows, cols, and a grid."""
        self.total_rows = total_rows
        self.total_cols = total_cols
        self.grid = []

    def find_color(self, v1=0, v2=0):
        """Return color if value is even or odd."""
        if (v1 + v2) % 2 == 0:
            return "white"
        else:
            return "black"

    def build_board(self):
        """Build the matrix of the board."""
        # create an empty list of a row
        rows = []
        # loop over the total number of rows
        for i in range(self.total_rows):
            # create an empty list of cols
            cols = []
            # loop over the total number of cols
            for j in range(self.total_cols):
                # add the data of the cell to the cols
                position = f"{i}{j}"
                # find the color based on number
                color = self.find_color(v1=i, v2=j)
                data = {"r": i, "c": j, "p": position, "color": color}
                cols.append(data)
            # add the cols to the row
            rows.append(cols)
        self.grid = rows

    def print_board(self):
        """Print the current status of the board."""
        for row in self.grid:
            for col in row:
                if col['color'] == 'black':
                    symbol = "*"
                if col['color'] == 'white':
                    symbol = "-"
                print(symbol, end="")
            print("")


class Player:
    """Create a player."""

    def __init__(self, name=False):
        """Create a player to participate in the game."""
        self.name = name

    def stats(self):
        """Print the players status."""
        return {"points": 0}
