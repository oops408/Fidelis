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
        self.white_to_move = True
        self.castling_rights = 'KQkq'
        self.en_passant_target = '-'
        self.halfmove_clock = 0
        self.fullmove_number = 1

    def move_piece(self, move):
        """
        Moves a piece on the chess board according to the specified move.
        """
        # TODO: Implement move_piece method

    def generate_legal_moves(self):
        """
        Generates a list of legal moves for the current player.
        """
        # TODO: Implement generate_legal_moves method

    def is_checkmate(self):
        """
        Determines whether the current player is in checkmate.
        """
        # TODO: Implement is_checkmate method

    def is_stalemate(self):
        """
        Determines whether the current player is in stalemate.
        """
        # TODO: Implement is_stalemate method

    def is_draw(self):
        """
        Determines whether the game is a draw.
        """
        # TODO: Implement is_draw method
