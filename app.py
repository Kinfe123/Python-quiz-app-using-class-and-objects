from Question import Question

questions = [
    "Which one is most trending pro language:\n(a)Python\n(b)Java\n(c)C\n(d)Ruby\nAnswer: ",
    "Which one is the super class of all error: \n(a)Exceptions\n(b)Errors\n(c)Throwable\n(d)None\nAnswer: ",
    "Which is help us to remove white space:\n(a)Split\n(b)Join\n(c)Stipe\n(d)All\nAnswer: "
    
]
question_ques =[
    Question(questions[0] , "a"),
    Question(questions[1] , "c"),
    Question(questions[2] , "c")
]
def takeTest(question_ques):
    score = 0
    for question in question_ques:
        answer = input(question.ques)
        if answer == question.answer:
            score+=1
    print(f"You got {score} / {len(questions)}")
takeTest(question_ques)

