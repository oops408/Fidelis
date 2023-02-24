class ChessGame:
    """
    Represents a game of chess.
    """

    def __init__(self):
        """
        Initializes a new game of chess.
        """
        self.board = ChessBoard()
        self.game_over = False

    def play(self):
        """
        Runs the game loop.
        """
        while not self.game_over:
            self.board.print_board()
            print(f"{self.board.current_turn.capitalize()}'s turn")

            # Get input from the player
            start_pos = input("Enter the starting position of the piece (e.g. 'a2'): ")
            end_pos = input("Enter the ending position of the piece (e.g. 'a4'): ")

            # Convert the input to row and column indices
            start_row, start_col = self.board.pos_to_index(start_pos)
            end_row, end_col = self.board.pos_to_index(end_pos)

            # Make the move
            if self.board.move((start_row, start_col), (end_row, end_col)):
                # Switch turns
                if self.board.current_turn == 'white':
                    self.board.current_turn = 'black'
                else:
                    self.board.current_turn = 'white'
            else:
                print("Invalid move. Try again.")

            # Check for end of game
            if self.is_game_over():
                self.game_over = True

    def is_game_over(self):
        """
        Checks if the game has ended.
        Returns True if the game has ended and False otherwise.
        """
        # Check for checkmate
    if self.board.is_checkmate():
        print("Checkmate!")
        return True

    # Check for stalemate
    if self.board.is_stalemate():
        print("Stalemate!")
        return True

    # Check for draw by repetition
    if self.board.is_draw_by_repetition():
        print("Draw by repetition!")
        return True

    # Check for draw by insufficient material
    if self.board.is_draw_by_insufficient_material():
        print("Draw by insufficient material!")
        return True

    return False
