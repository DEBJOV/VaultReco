import os, subprocess
import getpass

class Helper:
    def error_display(self, error_message):
    # Print the required error message
    # Print the getpass and clear screen
        print(error_message)
        getpass.getpass("Press ENTER to try again...")
        self.clr_scr()

    def clr_scr(self): 
    # Note: Clear Screen Function:
    # 1. cls use in Windows
    # 2. tput, reset use in MacOS

        if os.name == 'nt':
            subprocess.run(["cls"])
        else:
            subprocess.run(["tput", "reset"])

    def function_not_deploy(self, sorry_message):
        print("-" * 10)
        print(sorry_message)
        print("-" * 10)
        getpass.getpass("Press ENTER to try again...")
        self.clr_scr()
        
    def return_options_menu(self):
        print("-" * 10)
        print("System: Redirect to Options Menu")
        print("-" * 10)
        getpass.getpass("Press ENTER to Options Menu...")
        self.clr_scr()
        
        
# NOTE: To access the color font function, {COLOR.RED}Sentences{COLOR.RESET}
class Color:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    RESET = "\033[0m"
    BOLD = "\033[1m"