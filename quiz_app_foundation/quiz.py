# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# The Quiz and Question classes define a particular quiz
import datetime
import sys
import random
class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0
        self.completion_time = 0

    def print_header(self):
        print("\n\n*******************************************")
        print(f"QUIZ NAME: {self.name}")
        print(f"DESCRIPTION: {self.description}")
        print(f"QUESTIONS: {len(self.questions)}")
        print(f"TOTAL POINTS: {self.total_points}")
        print("*******************************************\n")

    def print_results(self, quiztaker, thefile = sys.stdout):
        print("*******************************************", file =thefile, flush=True)
        print(f"Results for {quiztaker} ", file =thefile, flush=True)
        today=datetime.datetime.now()
        print(f'Date:  {today.strftime("%D")}', file =thefile, flush=True)
        print(f'Elapsed Time:  {self.completion_time}', file =thefile, flush=True)
        
        print(f"Correct count of questions {self.correct_count } out of {len(self.questions)} ", file =thefile, flush=True)    
        print(f"Total score {self.score} out of {self.total_points}", file =thefile, flush=True)    
        print("*******************************************\n", file =thefile, flush=True)

    def take_quiz(self):
        # initialize the quiz state
        
        self.score = 0
        self.correct_count = 0
        self.completion_time = 0
        for q in self.questions:
            q.is_correct = False
        # print the header
        self.print_header()
        # random order of questions
        random.shuffle(self.questions)
        # execute each question and record the result
       
        starttime  = datetime.datetime.now()
        for q in self.questions:
            q.ask()
            if (q.is_correct):
                self.correct_count += 1
                self.score += q.points
            print("------------------------------------------------\n")             
        endtime  = datetime.datetime.now()

        if self.correct_count != len(self.questions):
           answer = input (f"\n whoud you like to retake failed questions? (y/n)").lower()
           if answer[0] == 'y':
               wrong_qs = [q for q in self.questions if q.is_correct == False]
               for q in wrong_qs:
                    q.ask()
                    if (q.is_correct):
                        self.correct_count += 1
                        self.score += q.points
                    print("------------------------------------------------\n")
               endtime  = datetime.datetime.now() 
                
        self.completion_time = endtime-starttime
        # remouevo los milisegundos molestos de la duración, atento que costó
        self.completion_time = datetime.timedelta(seconds=round(self.completion_time.total_seconds()))

        # return the results
        return (self.score, self.correct_count, self.total_points)


class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False


class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while (True):
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")
            
            if (len(response) == 0):
                print("Sorry, that's not a valid response. Please try again")
                continue

            response = response.lower()
            if (response[0] != "t" and response[0] != "f"):
                print("Sorry, that's not a valid response. Please try again")
                continue

            if response[0] == self.correct_answer:
                self.is_correct = True

            break


class QuestionMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while (True):
            print(self.text)
            for a in self.answers:
                print(f"{a.name}) {a.text}")

            response = input("? ")

            if (len(response) == 0):
                print("Sorry, that's not a valid response. Please try again")
                continue

            response = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct = True

            break


class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""


