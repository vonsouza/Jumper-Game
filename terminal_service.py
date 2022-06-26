
class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)
      
    def write_draw(self, attempts): 
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print("\n")
        if(attempts == 4):
                print("  ___ ")
                print(" /___\  ")
                print(" \   /")
                print("  \ /")
                print("   O")
                print("  /|\ ")
                print("  / \ ")
                print("^^^^^^^")

        if(attempts == 3):
                print("      ")
                print(" /___\  ")
                print(" \   /")
                print("  \ /")
                print("   O")
                print("  /|\ ")
                print("  / \ ")
                print("^^^^^^^")

        if(attempts == 2):
                print("    ")
                print("    ")
                print(" \   /")
                print("  \ /")
                print("   O")
                print("  /|\ ")
                print("  / \ ")
                print("^^^^^^^")

        if(attempts == 1):
                print("    ")
                print("    ")
                print("  ")
                print("  \ /")
                print("   O")
                print("  /|\ ")
                print("  / \ ")
                print("^^^^^^^")

        if(attempts == 0):
                print("    ")
                print("    ")
                print("  ")
                print("   ")
                print("   x")
                print("  /|\ ")
                print("  / \ ")
                print("^^^^^^^")
    
    def do_hide_word(self, secret_word, guessed_correctly):
        for letter in secret_word:
            if letter in guessed_correctly:
                print(letter, end=" ")
            else :
                print(" _ ", end="")

    def get_answer(self, secret_word):
        print(" The secret word was: " + secret_word)
