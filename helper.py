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