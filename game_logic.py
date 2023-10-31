# Standard library imports
import time

# Local application imports
from characters import Qbert, Coily
from rendering import GameBoard

def initialize_game():
    """Initialize game state and objects."""
    qbert = Qbert()
    coily = Coily()
    game_board = GameBoard()
    return qbert, coily, game_board

def run_game():
    """Main game loop."""
    qbert, coily, game_board = initialize_game()
  
    while True:
        # Render the game board
        game_board.render(qbert, coily)
        
        # Update character positions
        qbert.move()
        coily.move()
        
        # Artificial delay for demonstration
        time.sleep(0.1)
