from quizmanager import QuizManager
from quiz import *


class QuizApp:
    QUIZ_FOLDER = "quizzes"
    
    def __init__(self):
        self.username = ""
        self.result = None
        self.qm = QuizManager(QuizApp.QUIZ_FOLDER)
        
    
    def startup(self):
        #print greeting
        self.greeting()
        self.username= input("Please enter our name: ")
        print(f"Welcome: {self.username}")
        print()
        
    def greeting(self):
        print("^^^^^^^^^^^^")
        print("Hello, wellcome to this quiz program #QuizApp")
        print()
        
    def goodbye(self):
        print("^^^^^^^^^^^^")
        print(f"Goodbye, thanks for playing with me #QuizApp {self.username}")
        print("^^^^^^^^^^^^")
    
    def menu_header(self):      
        print("^^^^^^^^^^^^")
        print("Make a selection")
        print("M: Menu")
        print("L: List quizzes")
        print("T: Take quiz")
        print("E: Exit")
        print("^^^^^^^^^^^^")
         
    def menu_error(self):
        print("That's not a valid Menu selection. Please try again. ")
    
    def menu(self):
        self.menu_header()
        selection = ""    
 
        while (True):
            selection = input("Selection? ")
            
            if len(selection)==0:
                self.menu_error()
                continue
            
            selection = selection.capitalize()
            
            if selection[0] == "E":
                self.goodbye()
                break
            elif selection[0] == "M":
                self.menu_header()
                continue
            elif selection[0] == "L":
                print("\n Available quizzes are \n")
                #TO DO  List quizzese
                self.qm.list_quizzes()
                print()
                
                continue
            elif selection[0] == "T":
                try:
                    
                    quiznum  = int(input("Enter the quiz number you want to run: "))
                    print(f"you have selected {quiznum}")
                    # TODO Start quiz
                    self.qm.take_quiz(quiznum, self.username)
                    self.qm.print_results()
                    
                    dosave= input("Save the results? (y/n): ")
                    dosave = dosave.capitalize()
                    if  len(dosave) > 0 and dosave[0] =="Y":
                        self.qm.save_results()
                        
                except:
                    self.menu_error()
            else:
                self.menu_error()
    
 
        
    def run(self):
        self.startup()
        self.menu()
        
if __name__ == "__main__":
    app=QuizApp()
    app.run()    
        
            