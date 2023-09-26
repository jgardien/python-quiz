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
        while(True):
           
            print(f"(T)True or (F) False {self.text}")
            response = input ("> ")
            if len(response) == 0:
                print("Sorry this is not a valid respones, please try again ")
                continue
            response = response.lower()
            
            if response[0] != "t" and response[0] != "f":
                print("Sorry this is not a valid respones, please try again ")
                continue
            #Check if response is correct
            if response[0] == self.correct_answer:
                self.is_correct = True                
            break
 
class QuestionMultiple(Question):
    def __init__(self):
        super().__init__()
        self.answers = []
        
    def ask(self):
        while(True):
       
            print(f"{self.text}")
            for a in self.answers:  
                print(f"{a.name}  {a.text}")
            response = input ("> ")

            if len(response) == 0:
                print("Sorry this is not a valid respones, please try again ")
                continue
            
            response = response.lower()
            
            if response[0] == self.correct_answer:
                self.is_correct = True                
            break
        
class Answer:
    def __init__(self):
        pass
        self.text=""
        self.name=""
        
        
if __name__ == "__main__":
    q1 = QuestionTF()
    q1.text = "Broccoli is good for you"
    q1.points = 5
    q1.correct_answer = "t"
    q1.ask()
    q2 = QuestionMultiple()
    q2.text = "What is 2+2?"
    q2.points = 10
    q2.correct_answer = "b"
    ans = Answer()
    ans.name = "a"
    ans.text = "3"
    q2.answers.append(ans)
    ans = Answer()
    ans.name = "b"
    ans.text = "4"
    q2.answers.append(ans)
    ans = Answer()
    ans.name = "c"
    ans.text = "5"
    q2.answers.append(ans)
    q2.ask()

    print(q1.is_correct)
    print(q2.is_correct)
