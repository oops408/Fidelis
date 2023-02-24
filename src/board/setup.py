class ChessBoard:
    """
    Represents a chess board and the state of the game.
    """

    def __init__(self):
        """
        Initializes a new chess board with the starting positions of the pieces.
        """
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
        self.current_turn = 'white'

    def print_board(self):
        """
        Prints the current state of the chess board to the console.
        """
        for rank in self.board:
            print('+---+---+---+---+---+---+---+---+')
            print('| ' + ' | '.join(rank) + ' |')
        print('+---+---+---+---+---+---+---+---+')

    def move(self, start_pos, end_pos):
        """
        Moves a piece from the start position to the end position on the board.
        Returns True if the move is legal and False otherwise.
        """
        # Check that start and end positions are valid
        if not self.is_valid_pos(start_pos) or not self.is_valid_pos(end_pos):
            return False

        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Check that start position contains a piece belonging to the current player
        if self.board[start_row][start_col] == ' ' or \
           (self.current_turn == 'white' and self.board[start_row][start_col].islower()) or \
           (self.current_turn == 'black' and self.board[start_row][start_col].isupper()):
            return False

        # Check that end position is empty or contains an enemy piece
        if self.board[end_row][end_col] != ' ' and \
           ((self.current_turn == 'white' and self.board[end_row][end_col].isupper()) or \
            (self.current_turn == 'black' and self.board[end_row][end_col].islower())):
            return False

        # Check that the move is valid for the selected piece
        if self.board[start_row][start_col] == 'N' or self.board[start_row][start_col] == 'n':
            valid_moves = [(start_row + 1, start_col + 2), (start_row + 2, start_col + 1),
                           (start_row + 2, start_col - 1), (start_row + 1, start_col - 2),
                           (start_row - 1, start_col - 2), (start_row - 2, start_col - 1),
                           (start_row - 2, start_col + 1
