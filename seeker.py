import random

class Seeker:
    """The person looking for the Hider . 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    """

    def __init__(self):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._letter = ""
        
    def get_letter(self):
        """Gets the current letter.
        
        Returns:
            string: The current letter
        """
        return self._letter
        
    def move_letter(self, letter):
        """Moves to the given letter.

        Args:
            self (Seeker): An instance of Seeker.
            letter (string): The given letter.
        """
        self._letter = letter