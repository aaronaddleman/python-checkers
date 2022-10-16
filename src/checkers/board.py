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
        results = ""
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
                    results += f"| {col['r']},{col['c']} {player_peice} {space_color}"
                else:
                    results += f"| {player_peice} {space_color}"
        return results

    def stats(self):
        """Return the stats of the board."""
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

    def check_space_status(self, row=None, col=None, mode=None):
        """Return the status of a space."""
        if row is None:
            raise "Must have a row defined."
        if row > self.total_rows or row < 1:
            raise f"Row must be between 1 and {self.total_rows}."
        if col is None:
            raise "Must have a col defined."
        if col > self.total_cols or col < 1:
            raise f"Col must be between 1 and {self.total_cols}."
        # mode
        mode_values = ["is_occupied", "is_free", "player_color"]
        if mode is None or mode not in mode_values:
            raise f"Mode must be one of these values: {mode_values}"
        # get selected space
        selected_space = self.grid[row][col]
        # return the selected space
        if mode == "is_occupied" or mode == "player_color":
            return selected_space.get('player', False)

    def possible_moves(self, row=None, col=None):
        """List possible moves for selected row and column."""
        list_of_moves = []
        player_color = self.check_space_status(row=row,
                                               col=col,
                                               mode="player_color")
        if player_color == "black":
            new_row = row - 1
        new_row = row + 1

        if col < 7:
            list_of_moves.append({"r": new_row, "c": col + 1})
        if col > 0:
            list_of_moves.append({"r": new_row, "c": col - 1})
        return list_of_moves
