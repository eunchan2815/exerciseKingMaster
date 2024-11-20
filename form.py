import os;


class Question:

    previewQuestion = ""
    question = ""
    options = []


    hasBeenAnswered = False
    answer = ""

    def __init__(self, previewQuestion, question, options):
        self.previewQuestion = previewQuestion
        self.question = question
        self.options = options



class Form:

    formName = ""
    questionList = []

    def __init__(self, formName, questionList):
        self.formName = formName
        self.questionList = questionList


    def PrintQuestionProgress(self):

        for i in self.questionList:
            print("✔" if i.hasBeenAnswered else "?", end = " ")
            print(i.previewQuestion)


    def PrintFormInfo(self):
        os.system("clear")
        print()
        self.PrintQuestionProgress()
        print("\n----------------------------\n")


    def StartQuestion(self):

        for i in self.questionList:

            # PRINT PROGRESS AND DIVIDER LINE
            self.PrintFormInfo()
            
            print(i.question)
            
            # IF LIST IS EMPTY, USER WILL INPUT FREE STRING ANSWER
            # OR INPUT INDEX ANSWER BY OPTIONS WHEN OPTIONS IS EXISTS
            if (i.options): # IF LIST IS EMPTY
                for j in range(len(i.options)):
                    print(str(j + 1) + " : " + i.options[j])

                i.answer = input()

            else :
                i.answer = input()

            # IF ANSWER WAS INPUT, CHANGE FLAG AND GO NEXT QUESTION TO FOR-LOOP
            i.hasBeenAnswered = True



        self.PrintFormInfo()
        
        print('"' + self.formName + '" 설문을 완료했습니다. 다음 절차를 진행하시겠습니까?')
        input()
    


    def GetAnswerData(self, questionId):
        return self.questionList[questionId].answer

            



