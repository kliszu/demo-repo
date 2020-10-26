from modules import student
from modules import question

question_prompts = [
    "what color ae apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "WHat color are bananas?\n(a) Teal\n(b) Mgenta\n(c) Yellow\n\n" ,
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
student1 = student("jim", "law", 3.1, False)
student2 = student("Pam", "Art", 4.1, True)

questions = [
   question(question_prompts[0],"a") ,
   question(question_prompts[1],"c") ,
   question(question_prompts[2],"b")
]

def run_test(qestions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got "+str(score)+" / "+str(len(questions))+" correct")

print(student2.on_honor_roll())