import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper import Helper


class AttendanceCalculator:
    def __init__(self):
        self.helper = Helper()

        # ============ Array Variable ============
        # Note: Class Array Position [ 0 = Lecture Class | 1 = Tutorial Class | 2 = Practical Class ]
        self.arr_oneClassDuration = [None] * 3 
        self.arr_classDuration = [None] * 3
        self.arr_classTime = [1] * 3 
        self.arr_missedClass = [0] * 3
        self.arr_TotalAttendTime = [0] * 3
        self.class_time = None

    def main_header(self):
            print('-' * 40)
            print(f'{"":8} Attendance Calculate')
            print('-' * 40)

    def set_semester(self):
        while (True):
            self.helper.clr_scr()
            self.main_header()
            self.semester_type = input("Enter Semester Type (Long/Short): ").strip().lower()
            if (self.semester_type == "short" or self.semester_type == "s"):
                self.semester_type = "Short Semester"
                self.semester_period = 8
                break
            elif (self.semester_type == "long" or self.semester_type == "l"):
                self.semester_type = "Long Semester"
                self.semester_period = 14
                break
            else: 
                self.helper.error_display("System: Please only enter long or short!")
                

        self.barlistOut = self.semester_period - 2
        print(f"System: Semester Period Set to {self.semester_period} weeks.")   

        self.options_menu() # Pass to the options menu function


    def options_menu(self):
        from main import Main
        self.main = Main()
        while True:
            self.helper.clr_scr()

            print('-' * 40)
            print(f'{"":13} Options Menu')
            print('-' * 40)
            print("[1] Set Class Duration\n[2] Attendance Calculate\n[3] Return to Menu\n", '-' * 39, "\n")

            options_choose = input("Enter the Opitons (1 - 3): ")
            match options_choose:
                case '1':
                    self.class_duration()
                    continue
                case '2':
                    if (self.semester_type == "Short Semester"):
                        if any(x is None for x in self.arr_classDuration):
                            self.helper.error_display("System: Class Duration Cannot Be Empty!")
                        else:
                            self.calculation("short_semester")
                            continue
                    elif (self.semester_type == "Long Semester"):
                        if any(x is None for x in self.arr_classDuration):
                            self.helper.error_display("System: Class Duration Cannot Be Empty!")
                        else:
                            self.calculation("long_semester")
                            continue
                case '3':
                    return self.main.run()
                case _:
                    self.helper.error_display("System: Please Only Enter (1-3)!")


    def class_duration(self):
        self.helper.clr_scr()

        def class_duration_table():     # Display the Current Duration for (Lecture / Practical / Tutorial) classes
            print('-' * 40)
            if any(x is not None for x in self.arr_classDuration):
                print(f"Semester Type: {self.semester_type} ({self.semester_period} Weeks)")
                print('-' * 40)
                print("[NOTE: Class Duration Per Weeks]\n")
                print(f"Lecture Duration(mins)   : {self.arr_classDuration[0]}")
                print(f"Tutorial Duration(mins)  : {self.arr_classDuration[1]}")
                print(f"Practical Duration(mins) : {self.arr_classDuration[2]}")
            else:
                print(f'{"":6} Currently Data Still Empty')
            print('-' * 40)

        def class_time_modify(class_type):    # Change the Current Class Duration
            while True:
                self.helper.clr_scr()
                class_duration_table()
                if (class_type == "lecture_class"):
                    print(f"[Note] Current Class Time: {self.arr_classTime[0]} per weeks")
                elif (class_type == "tutorial_class"):
                    print(f"[Note] Current Class Time: {self.arr_classTime[1]} per weeks")
                elif (class_type == "practical_class"):
                    print(f"[Note] Current Class Time: {self.arr_classTime[2]} per weeks")
                
                modify_time = input("\nDo you want to modify class time(Y/N): ").strip().upper()

                match modify_time:
                    case 'Y' | 'y':
                        while True:
                            try:
                                self.class_time = int(input("Enter Class Time(per week): "))
                                if (self.class_time > 5 or self.class_time < 1):
                                    self.helper.error_display("System: Invalid Class Time Range!")
                                    class_duration_table()
                                else:
                                    if (class_type == "lecture_class"):
                                        self.arr_classTime[0] = self.class_time
                                    elif (class_type == "tutorial_class"):
                                        self.arr_classTime[1] = self.class_time
                                    elif (class_type == "practical_class"):
                                        self.arr_classTime[2] = self.class_time
                                    break
                            except ValueError:
                                self.helper.error_display("System: Please Enter Digit Only!")
                                class_duration_table()
                        break
                    case 'N' | 'n':
                        return
                    case _:
                        self.helper.error_display("System: Please only enter Y or N!")


        def change_duration_options():
            while True:
                self.helper.clr_scr()
                class_duration_table()
                print("\n[1] Change Lecture Class Duration\n[2] Change Tutorial Class Duration\n[3] Change Practical Class Duration\n[4] Return to Options Menu\n", '-' * 39, "\n")
                self.change_duration_choice = input("Enter The Class Type to Change Duration (1-4): ")

                match self.change_duration_choice:
                    case "1":
                        self.helper.clr_scr()
                        class_duration_table()
                        while True:
                            while True:
                                try:
                                    self.class_duration_time = int(input("\nEnter Lecture Class Duration(mins): "))
                                    break
                                except ValueError:
                                    self.helper.error_display("System: Please Enter Digit Only!")
                                    class_duration_table()

                            if (self.class_duration_time < 0 or self.class_duration_time > 200):
                                self.helper.error_display("System: Invalid Class Duration Range!")
                                class_duration_table()
                            elif (not self.class_duration_time == 0):
                                class_time_modify("lecture_class")   
                                break
                            elif (self.class_duration_time == 0): 
                                self.arr_classTime[0] = 0
                                break
                            else:
                                self.arr_oneClassDuration[0] = self.class_duration_time
                                break   
                            
                        self.arr_oneClassDuration[0] = self.class_duration_time
                        total_classDuration = self.class_duration_time * self.arr_classTime[0]
                        self.arr_classDuration[0] = total_classDuration

                        self.helper.clr_scr()
                        return change_duration_options() # After modify the class time, return back to the change_duration_options

                    case "2":
                        self.helper.clr_scr()
                        class_duration_table()
                        while True:
                            while True:
                                try:
                                    self.class_duration_time = int(input("\nEnter Tutorial Class Duration(mins): "))
                                    break
                                except ValueError:
                                    self.helper.error_display("System: Please Enter Digit Only!")
                                    class_duration_table()

                            if (self.class_duration_time < 0 or self.class_duration_time > 200):
                                self.helper.error_display("System: Invalid Class Duration Range!")
                                class_duration_table()
                            elif (not self.class_duration_time == 0):
                                class_time_modify("tutorial_class")   
                                break
                            elif (self.class_duration_time == 0): 
                                self.arr_classTime[1] = 0
                                break
                            else:
                                self.arr_oneClassDuration[1] = self.class_duration_time
                                break   
                            
                        self.arr_oneClassDuration[1] = self.class_duration_time
                        total_classDuration = self.class_duration_time * self.arr_classTime[1]
                        self.arr_classDuration[1] = total_classDuration

                        self.helper.clr_scr()
                        return change_duration_options() # After modify the class time, return back to the change_duration_options
                    case "3":
                        self.helper.clr_scr()
                        class_duration_table()
                        while True:
                            while True:
                                try:
                                    self.class_duration_time = int(input("\nEnter Practical Class Duration(mins): "))
                                    break
                                except ValueError:
                                    self.helper.error_display("System: Please Enter Digit Only!") 
                                    class_duration_table()

                            if (self.class_duration_time < 0 or self.class_duration_time > 200):
                                self.helper.error_display("System: Invalid Class Duration Range!")
                                class_duration_table()
                            elif (not self.class_duration_time == 0):
                                class_time_modify("practical_class")   
                                break
                            elif (self.class_duration_time == 0): 
                                self.arr_classTime[2] = 0
                                break
                            else:
                                self.arr_oneClassDuration[2] = self.class_duration_time
                                break   
                        self.arr_oneClassDuration[2] = self.class_duration_time
                        total_classDuration = self.class_duration_time * self.arr_classTime[2]
                        self.arr_classDuration[2] = total_classDuration

                        self.helper.clr_scr()
                        return change_duration_options() # After modify the class time, return back to the change_duration_options
                    case "4":
                        self.helper.clr_scr()
                        return self.options_menu()
                    case _:
                        self.helper.error_display("System: Please Only Enter (1-4)!")


        while True:
            self.helper.clr_scr()
            class_duration_table()

            self.change_duration_choice = input("\nDo You Want to Change Class Duration (Y/N): ")

            match self.change_duration_choice:
                case 'Y' | 'y':
                    change_duration_options()
                    break
                case 'N' | 'n':
                    return # Do not change the class duration, return back to the options menu
                case _:
                    self.helper.error_display("System: Please only enter Y or N!")

    def calculation(self, semester_type):
        def calculation_header():
            print('-' * 40)
            print(f'{"":9} Attendance Calculation')
            print('-' * 40)
            
        def missed_time_error():
            if (semester_type == "long_semester" and self.missed_time > 14):
                self.helper.error_display("System: Invalid Study Week Range!")
                return True
            elif (semester_type == "short_semester" and self.missed_time > 8):
                self.helper.error_display("System: Invalid Study Week Range!")
                return True
            elif (self.current_study_week < self.missed_time):
                self.helper.error_display("System: Missed Time Cannot More Than Current Week!")
                return True
            elif any(x is None or x == 0 for x in self.arr_classDuration):
                self.helper.error_display("System: Don't Have Class in Semester!")
                return True
            return False
        
        def set_missed_header():
            print('-' * 40)
            print(f'{"":9} Set Missed Class')
            print('-' * 40)
            
        def attendance_calculation(): 
            # All The Attendance Calculation and Display Result
            currentPresentTime = sum(self.arr_TotalAttendTime)
            currentTotalTime = (self.current_study_week * sum(self.arr_classDuration))
            
            percentage = (currentPresentTime / currentTotalTime) * 100
            
            self.helper.clr_scr()
            
            print('-' * 40)
            print(f'{"":9} Attendance Percentage')
            print('-' * 40)
            print(f"Attendance Percentage: {percentage:.2f}\n")
            print('-' * 40)
            
            
            
        def missed_class_choice():
            while True:
                self.helper.clr_scr()
                set_missed_header()
                print("[1] Lecture Class\n[2] Tutorial Class\n[3] Practical Class\n[4] Start Attendance Calculation\n", "-" * 39, "\n")
                
                self.missed_choice = input("Enter Missed Class Type (1-4): ")


                match self.missed_choice:
                    case '1':
                        while True:
                            try:
                                self.helper.clr_scr()
                                set_missed_header()
                                self.missed_time = int(input("Enter Lecture Class Missed Time: "))
                                if missed_time_error():
                                    continue
                                #take Note
                                self.arr_missedClass[0] = self.missed_time
                                self.missed_Attendtime = self.arr_missedClass[0] * self.arr_oneClassDuration[0]
                                self.totalTime = self.arr_classDuration[0] * self.current_study_week 
                                self.arr_TotalAttendTime[0] = self.totalTime - self.missed_Attendtime
                                
                                break
                                
                            except ValueError:
                                self.helper.error_display("System: Please Enter Digit Only!")   
                        
                    case '2':
                        while True:
                            try:
                                self.helper.clr_scr()
                                set_missed_header()
                                self.missed_time = int(input("Enter Tutorial Class Missed Time: "))
                                if missed_time_error():
                                    continue
                                #take Note
                                self.arr_missedClass[1] = self.missed_time
                                self.missed_Attendtime = self.arr_missedClass[1] * self.arr_oneClassDuration[1]
                                self.totalTime = self.arr_classDuration[1] * self.current_study_week 
                                self.arr_TotalAttendTime[1] = self.totalTime - self.missed_Attendtime

                                break
                                
                            except ValueError:
                                self.helper.error_display("System: Please Enter Digit Only!")  
                    case '3':
                        while True:
                            try:
                                self.helper.clr_scr()
                                set_missed_header()
                                self.missed_time = int(input("Enter Practical Class Missed Time: "))
                                if missed_time_error():
                                    continue
                                #take Note
                                self.arr_missedClass[2] = self.missed_time
                                self.missed_Attendtime = self.arr_missedClass[2] * self.arr_oneClassDuration[2]
                                self.totalTime = self.arr_classDuration[2] * self.current_study_week 
                                self.arr_TotalAttendTime[2] = self.totalTime - self.missed_Attendtime

                                break
                                
                            except ValueError:
                                self.helper.error_display("System: Please Enter Digit Only!")   
                    case '4':
                        attendance_calculation()
                        
                        self.helper.function_not_deploy("More Function will be Deploy!") #------------------------------ REMOVE
                        sys.exit()
                    case _:
                        self.helper.error_display("System: Please Only Enter (1-4)!")
                                
            
        if (semester_type == "long_semester"):
            while True:
                try:
                    self.helper.clr_scr()
                    calculation_header()
                    self.current_study_week = int(input("Enter Currently Week: "))
                    if (self.current_study_week < 0 or self.current_study_week > 14):
                        self.helper.error_display("System: Invalid Study Week Range!")
                    else:
                        break
                except ValueError:
                    self.helper.error_display("System: Please Enter Digit Only!")
            while True:
                self.missed_options = input("Do You Have Missed Class(Y/N): ").strip().lower()
                match self.missed_options:
                    case 'n':                                                   
                        self.arr_TotalAttendTime[0] = (self.arr_classDuration[0] * self.current_study_week)              
                        self.arr_TotalAttendTime[1] = (self.arr_classDuration[1] * self.current_study_week)
                        self.arr_TotalAttendTime[2] = (self.arr_classDuration[2] * self.current_study_week)           
                        attendance_calculation()
                        
                        self.helper.function_not_deploy("More Function will be Deploy!") #------------------------------ REMOVE
                        sys.exit()
                    case 'y':
                        missed_class_choice()
                        break    
                    case _:
                        self.helper.error_display("System: Please only enter Y or N!")    
                    
        elif (semester_type == "short_semester"):
            while True:
                try:
                    self.helper.clr_scr()
                    calculation_header()
                    self.current_study_week = int(input("Enter Currently Week: "))
                    if (self.current_study_week < 0 or self.current_study_week > 8):
                        self.helper.error_display("System: Invalid Study Week Range!")
                    else:
                        break
                except ValueError:
                    self.helper.error_display("System: Please Enter Digit Only!")
            while True:
                self.missed_options = input("Do You Have Missed Class(Y/N): ").strip().lower()
                match self.missed_options:
                    case 'n':
                        attendance_calculation()
                    case 'y':
                        missed_class_choice()
                        break    
                    case _:
                        self.helper.error_display("System: Please only enter Y or N!")            
                

