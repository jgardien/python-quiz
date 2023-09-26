class QuizApp:
    def __init__(self):
        self.username = ""
    
    def startup(self):
        #print greeting
        self.greeting()
        self.username= input("Please enter our name: ")
        print(f"Welcome: {self.username}")
        
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
        print("That's not a valid selection. Please try again. ")
    
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
                #TO DO  List quizzes
                continue
            elif selection[0] == "T":
                try:
                    quiznumber = int(input("Enter the quiz number you want to run: "))
                    print(f"you have selected {quiznumber}")
                    # TODO Start quiz
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
        
            