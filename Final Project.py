from data import dictionary, awards, finalRound
from data import validateInput, isValidAnswer, fifthGraderAnswer
import random
dictionary = {
    1: {
        '1st grade environmental science:Which bin would you recycle a water bottle in?\na) plastic b) paper c) aluminum d) glass': 'a',
        '1st grade biology:How many major oceans are there on Earth? a) 3 b) 4 c) 5 d) 6': 'c'
    },
    2: {
        '2nd grade ecology:Fill in the blank. Soil is the ______ for many animals.\na) Food b) Home c) Atmosphere d) Resource': 'b',
        '2nd grade earth science: The following is not a layer of the Earth? a) Atmosphere b) Crust  c) Mantle d) Core': 'a'
    },
    3: {
        '3rd grade chemistry:Two properties of matter are volume and ______\na) Property b) Matter c) Mass d) Electricity': 'c',
        '3rd grade astronomy, Which planet is closest to the Sun? a) Mars b) Venus  c) Uranus d) Mercury': 'd'
    },
    4: {
        '4th grade physics: On which surface would a ball move slowly because of friction?\na) Wood b) Title c) Marble floor d) Carpet': 'd',
        '4th grade zoology: What is the sequence of the life cycle stages of metamorphosis? a) wake up, eat, sleep, deathb) egg, pupa, larva, adult c) egg, larva, pupa, adult d) born, hungry, sleeping, death': 'c'
    },
    5: {
        '5th grade computer science:Name the part that sends signals to other parts of the computer and tells it what to do.\nA) CPU B) Motherboard C) Icon D)Hard Drive: ': 'a'
    }
}

awards = {1: 1000, 2: 2000, 3: 3000, 4: 4000, 5: 5000}

def fifthGraderAnswer():
    choices = ['a','b','c','d']
    randomIndex = random.randint(0, 3)
    return choices[randomIndex]


def isValidAnswer(answer, correctAnswer, successMessage, failureMessage):
    if answer == correctAnswer:
        print(successMessage)
        return True
    else:
        print(failureMessage)
        return False
    
def validateInput(choices, choice):
    return choice in choices


def finalRound(total_award):

    
    print("\nLast Question!! Proof that your 5th grade Biology didn't fail you, answer question 5 correctly and take home all you money, but of you answer incorrectly you will be going home with nothing!Good luck !")
    print("You can either play and risk it all or leave with what you've earned\n")
    user_input = input("Would you like to keep playing? Enter Y/YES or N/NO: ")
    options = ["YES", "Y", "N", "NO"]

    while not validateInput(options, user_input):
        user_input = input("Enter Y/YES or N/NO")
    
    if user_input == "YES" or user_input == "Y":

        grade_5_question = list(dictionary[5].keys())[0]
        grade_5_answer = dictionary[5][grade_5_question]
        user_answer = input(grade_5_question + "\nYour answer: ")

        while not validateInput(["a", "b", "c", "d"], user_answer):
            user_answer = input("Please enter choices a, b, c, d: ")

        successMessage = "\nCongratulations! You have won the 5th grade question award of $"+ str(awards[5])
        failureMessage = "\nYou have answered the 5th-grade question incorrectly and lost your award!"
        
        if isValidAnswer(user_answer, grade_5_answer, successMessage, failureMessage):
            total_award[0] += awards[5]
        else:
            total_award[0] = 0

        

   

    print("Thanks for playing! Overall Total award: $" + str(total_award[0]) + "\n")

def playGame():
    
    list1 = []
    total_award = [0]

    while len(list1) < 4:
        grade = input("Enter grade category (1-4): ")
        if not validateInput(["1","2", "3", "4"], grade):
            print("Invalid input. Enter a valid choice\n")
            continue

        grade = int(grade)
        if grade in list1:
            print("You have already selected this grade category!")
            continue

        list1.append(grade)
       
        
        if grade not in dictionary:
            print("Invalid grade category!")
            
        else:
            for i, question in enumerate(dictionary[grade]):
                answer_key = str(grade) + str(i+1)
                response = "\nEnter save if you want to be saved by a 5th grader.\nYour answer: "
                user_answer = input(question + response)
                correctAnswer = dictionary[grade][question]

                while not validateInput(["a","b","c", "d", "save"],user_answer):
                    user_answer = input("Please enter choices a, b, c, d or save: ")

                if(user_answer == "save"):
                    randomAnswer = fifthGraderAnswer()
                    failMessage = "NOT SAVED! Fifth grader answered: " + randomAnswer + ". Correct Answer is: " + correctAnswer
                    if isValidAnswer(randomAnswer, correctAnswer, "SAVED!" , failMessage):
                        total_award[0] += awards[grade]

                else:
                    failMessage = "WRONG! Correct Answer is: " + correctAnswer
                    if isValidAnswer(user_answer, correctAnswer, "CORRECT!", failMessage):
                        total_award[0] += awards[grade]
                print("Total award: " + str(total_award[0]) + "\n")
 
    print("Total award: " + str(total_award[0]) + "\n")


    finalRound(total_award)







playGame()


