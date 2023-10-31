# utils.py

def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points.
    
    Parameters:
        point1 (tuple): Coordinates of the first point.
        point2 (tuple): Coordinates of the second point.
        
    Returns:
        float: The Euclidean distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


def is_adjacent(point1, point2):
    """Check if two points are adjacent on the game board.
    
    Parameters:
        point1 (tuple): Coordinates of the first point.
        point2 (tuple): Coordinates of the second point.
        
    Returns:
        bool: True if adjacent, False otherwise.
    """
    return calculate_distance(point1, point2) == 1.0


def log_event(event):
    """Log an event to the console for debugging purposes.
    
    Parameters:
        event (str): Description of the event to log.
    """
    print(f"Event: {event}")
