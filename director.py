import random

from terminal_service import TerminalService
from seeker import Seeker

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        ATTEMPTS is a constant is the number of attempts the player will have to find the secret word
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """
    

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        ATTEMPTS = 4
        self._is_playing = True
        self._seeker = Seeker()
        self._terminal_service = TerminalService()
        self._attempts = ATTEMPTS
        self._guessed_correctly = []
        self._secret_word = ""

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        words = ["chair", "book", "pencil", "paper", "glue", "desk", "music", "home", "cake", "mouse", "song"]

        words_size = len(words)
        self._secret_word = words[random.randint(0, words_size)]

        self._terminal_service.do_hide_word(self._secret_word, self._guessed_correctly)
        self._terminal_service.write_draw(self._attempts)

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        
        self._finish()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        new_guess_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._seeker.move_letter(new_guess_letter)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        if self._seeker.get_letter() not in self._secret_word:
            self._attempts -= 1
        else :
            #the player found a correct letter
            self._guessed_correctly.append(self._seeker.get_letter())
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.do_hide_word(self._secret_word, self._guessed_correctly)
        self._terminal_service.write_draw(self._attempts)

        if self._attempts <= 0:
            self._is_playing = False
        if len(self._guessed_correctly) >= len(self._secret_word):
            self._is_playing = False

    def _finish(self):
        """Shows the correct answer to player.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.get_answer(self._secret_word)