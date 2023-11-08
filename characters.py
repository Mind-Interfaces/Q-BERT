# characters.py

class Qbert:
    """Represents the main character, Q*bert."""
    
    # Class-level constant for initial position
    INITIAL_POSITION = (0, 0)
    
    def __init__(self):
        """Initialize Q*bert's position."""
        self.position = self.INITIAL_POSITION

    def move(self, new_position):
        """Update Q*bert's position based on game logic.
        
        Parameters:
            new_position (tuple): The new position for Q*bert.
        """
        # Validate new_position before updating
        if self.is_valid_position(new_position):
            self.position = new_position
    
    def is_valid_position(self, position):
        """Check if the given position is valid.
        
        Parameters:
            position (tuple): The position to validate.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        # For demonstration, assuming all positions are valid
        return True


class Coily:
    """Represents Coily, one of Q*bert's adversaries."""
    
    # Class-level constant for initial position
    INITIAL_POSITION = (3, 3)
    
    def __init__(self):
        """Initialize Coily's position."""
        self.position = self.INITIAL_POSITION

    def move(self, target_position):
        """Update Coily's position to chase Q*bert.
        
        Parameters:
            target_position (tuple): Q*bert's current position.
        """
        # Simple AI logic to move Coily towards Q*bert
        x, y = self.position
        target_x, target_y = target_position

        if x < target_x:
            x += 1
        elif x > target_x:
            x -= 1

        if y < target_y:
            y += 1
        elif y > target_y:
            y -= 1

        self.position = (x, y)
