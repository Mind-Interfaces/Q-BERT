# rendering.py

class GameBoard:
    """Handles the graphical rendering of the Q*bert game."""
    
    def __init__(self):
        """Initialize the game board."""
        # For demonstration, initializing an empty 5x5 board
        self.board = [[None for _ in range(5)] for _ in range(5)]

    def render(self, qbert, coily):
        """Render the game board along with Q*bert and Coily.
        
        Parameters:
            qbert (Qbert): The Q*bert character object.
            coily (Coily): The Coily character object.
        """
        self.clear_board()
        self.place_character(qbert)
        self.place_character(coily)
        self.display_board()

    def clear_board(self):
        """Clear the board for a fresh render."""
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = None

    def place_character(self, character):
        """Place a character on the board.
        
        Parameters:
            character (object): The character object to place.
        """
        x, y = character.position
        self.board[x][y] = character.__class__.__name__[0]

    def display_board(self):
        """Display the board state."""
        for row in self.board:
            print(" ".join(cell if cell else "." for cell in row))
