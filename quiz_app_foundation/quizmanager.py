# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# QuizManager manages the quiz content
import os.path
import os
import quizparser
import datetime


class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder
        #TODO: the most recently selected quiz
        self.the_quiz = None
        self.quizzes = dict()
        self.results = None
        self.quiztaker = ""
                   
        if (os.path.exists(quizfolder) == False):
                raise FileNotFoundError ("quiz folder does not exist")
        self._build_quiz_list()
       
        
    def _build_quiz_list(self):
      
        dircontents = os.scandir(self.quizfolder)
        
        #TODO: parse the XML files in the directory
        for i,f in enumerate(dircontents):            
            if f.is_file():                
                parser = quizparser.QuizParser()
                self.quizzes[i+1] = parser.parse_quiz(f)
             

    #TODO: print a list of the currently installed quizzes
    def list_quizzes(self):
        for k,v in self.quizzes.items():
            print(f"({k} :  {v.name})")
            

    # start the given quiz for the user and return the results
    def take_quiz(self, quizid, username):
        self.quiztaker = username
        self.the_quiz = self.quizzes[quizid]
        self.results = self.the_quiz.take_quiz()
               
        #return(self.results)


    # prints the results of the most recently taken quiz
    def print_results(self):
        self.the_quiz.print_results(self.quiztaker)

    # save the results of the most recent quiz to a file
    # the file is named using the current date as
    # QuizResults_YYYY_MM_DD_N (N is incremented until unique)
    def save_results(self):
        today = datetime.datetime.now()
        filename = f"quizResults_{self.quiztaker}_{today.year}_{today.month}_{today.day}.txt"
        n=1
        while (os.path.exists(filename)):
            filename = f"quizResults_{self.quiztaker}_{today.year}_{today.month}_{today.day}_{n}.txt"
            n+=1
        
        with open(filename, "w") as f:
            self.the_quiz.print_results(self.quiztaker, f)   
        

if __name__ == "__main__":
    
    qm = QuizManager("quizzes")
    qm.list_quizzes()
