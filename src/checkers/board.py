"""Manage the board object(s)."""


def find_color(column=0, row=0):
    """Return color if value is even or odd."""
    if (column + row) % 2 == 0:
        return "white"
    return "black"


class GameBoard:
    """Create a game board."""

    def __init__(self, total_rows=8, total_cols=8):
        """Initialize the board with rows, cols, and a grid."""
        self.total_rows = total_rows
        self.total_cols = total_cols
        self.grid = []

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
                color = find_color(column=i, row=j)
                data = {"r": i, "c": j, "p": position, "color": color}
                cols.append(data)
            # add the cols to the row
            rows.append(cols)
        self.grid = rows

    def add_player_pieces(self, player_white=None, player_black=None):
        """Add player pieces to the board."""
        # white side, first 3 rows
        for index, row in enumerate(self.grid):
            if index < 3:
                for col in row:
                    if col['color'] == 'black':
                        # add a player peice
                        col['player'] = 'white'
                        col['player_symbol'] = player_white.player_symbol
            if index > 4:
                for col in row:
                    if col['color'] == 'black':
                        # add a player peice
                        col['player'] = 'black'
                        col['player_symbol'] = player_black.player_symbol

    def print_board(self, showNumbers=False):
        """Print the current status of the board."""
        for row in self.grid:
            for col in row:
                if col['color'] == 'black':
                    space_color = "b"
                if col['color'] == 'white':
                    space_color = "w"
                # set default player peice to be blank
                player_peice = "  "
                # if a player exists and is white
                if col.get('player'):
                    player_peice = f" {col['player_symbol']}"
                # print the columns in the row
                if showNumbers:
                    print(f"| {col['r']},{col['c']} {player_peice} {space_color}", end="")
                else:
                    print(f"| {player_peice} {space_color}", end="")

            print("")

    def stats(self):
        """Return the stats of the board"""
        data = {
            'num_of_player_pieces': 0,
            'num_of_black_pieces': 0,
            'num_of_white_pieces': 0
        }

        for row in self.grid:
            for col in row:
                if col.get('player'):
                    data['num_of_player_pieces'] += 1
                    if col['player'] == 'black':
                        data['num_of_black_pieces'] += 1
                    if col['player'] == 'white':
                        data['num_of_white_pieces'] += 1

        return data

    def possible_moves(self, row=None, col=None):
        """List possible moves for selected row and column"""
        list_of_moves = []
        new_row = row + 1
        if col < 7:
            list_of_moves.append({"r": new_row, "c": col + 1})
        if col > 0:
            list_of_moves.append({"r": new_row, "c": col - 1})
        return list_of_moves
