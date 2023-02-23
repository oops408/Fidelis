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

    def print_board(self):
        """
        Prints the current state of the chess board to the console.
        """
        for rank in self.board:
            print('+---+---+---+---+---+---+---+---+')
            print('| ' + ' | '.join(rank) + ' |')
        print('+---+---+---+---+---+---+---+---+')
