from Student.Attendance import AttendanceCalculator
from helper import Helper

#-----------------RUN PROGRAM-----------------
class Main:
    def __init__(self):
        self.attendance = AttendanceCalculator()
        self.helper = Helper()
        
    def run(self):
        while True:
            self.helper.clr_scr() # Temporary Used
            
            print('-' * 40)
            print(f'{"":14} VaultReco')
            print('-' * 40)
            print("[1] Course Structure\n[2] Attendance Calculate\n[3] CGPA Result Calculate\n[4] Exit\n")
            
            main_options = input("Enter the Opitons (1 - 4): ")
            
            match main_options:
                case '1':
                    self.helper.function_not_deploy("Sorry, Function Not Yet Deploy!")
                case '2':
                    self.attendance.set_semester()
                    break
                case '3':
                    self.helper.function_not_deploy("Sorry, Function Not Yet Deploy!")
                case '4':
                    return 0
                case _:
                    self.helper.error_display("System: Please Only Enter (1-4)!")
        
if __name__ == "__main__":
    system = Main()
    system.run()                 

