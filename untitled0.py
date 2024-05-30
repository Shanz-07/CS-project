#quiz - 11A
user_name = 'admin07'
user_pass = 'admin123'
answers_dict = {}
d = {}

def admin_login():
    print(' ')
    print("Please login with Valid Administrator User name and Password")
    print(' ')
    while True:
        admin_user = input("Enter the username: ")
        admin_pass = input("Enter the password: ")
        if admin_user == user_name and admin_pass == user_pass:
            print("Welcome! admin07")
            break
        else:
            print("Invalid username or password please try again")
admin_login()

def admin_questions():
    qu = int(input("Enter the number of categories you want: "))
    for i in range(qu):
        c = input("Enter the name of the category: ")
        e = int(input(f"Enter the number of questions for {c} category: "))
        questions = []
        answers = []  
        for j in range(e):
            f = input("Enter the question: ")
            questions.append(f)
            ans = input(f"Enter the answer for '{f}': ")
            answers.append(ans)
        d[c] = questions
        answers_dict[c] = dict(zip(questions, answers))  
    print(d)
    print(answers_dict)

admin_questions()

def modify_questions():
    mu = input("Enter the category of questions you want to modify: ")
    if mu in d:
        print(f"Questions in '{mu}' category: {d[mu]}")
        choice = input("Do you want to (A)dd or (R)emove a question? (A/R): ").upper()
        if choice == "A":
            new_question = input("Enter the new question: ")
            d[mu].append(new_question)
            print("Question added successfully!")
        elif choice == "R":
            print(f"Current questions: {d[mu]}")
            question_to_remove = input("Enter the question to remove: ")
            if question_to_remove in d[mu]:
                d[mu].remove(question_to_remove)
                print("Question removed successfully!")
            else:
                print("Question not found in the category.")
        else:
            print("Invalid choice.")
    else:
        print("Category not found.")
modify_questions()

def registration():
    u_r = input("Enter the name of the player playing: ")
    print("")
    print('Welcome,', u_r, '! The rules of the game are simple:')
    print("")
    print('You get to choose a category of questions you would want to proceed with.')
    print(" ")
    print('Try to answer these questions to increase your score by 1 point for each correct answer.')
    print("")
    print("If not attempted or wrong answer, there are no negative markings.")
    print(' ')
    print("Available categories are: ", list(d.keys()))
    print('')
    cat = input("Enter the category of the questions you want to attempt: ")

    if cat in d:
        print(f"You've chosen '{cat}' category. Let's start the game!")
        questions = d[cat]
        score = 0
        for idx, question in enumerate(questions, start=1):
            print(f"Question {idx}: {question}")
            user_answer = input("Your answer: ")
            actual_answer = answers_dict[cat].get(question)
            if user_answer.lower() == actual_answer.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {actual_answer}")

        print(f"Game Over! Your final score is: {score}")
    else:
        print("Category not found.")

registration()

