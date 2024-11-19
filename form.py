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
        for i in self.questionList:
            if (i.previewQuestion == questionId):
                return i.answer

            



bodyInfoQuestions = [
    Question("성별", "안녕하세요. 당신의 성별을 알려주세요.", ["남성", "여성"] ),
    Question("나이 ", "나이를 입력해주세요.", [] ),
    Question("키", "키(cm)를 알려주세요.", [] ),
    Question("몸무게", "몸무게(kg)를 알려주세요.", [] ),
    Question("이름", "이름이 무엇인가요?", [] ),]

bodyInfoForm = Form("정보 조사", bodyInfoQuestions)





bodyInfoForm.StartQuestion()
print(bodyInfoForm.GetAnswerData("성별"))
