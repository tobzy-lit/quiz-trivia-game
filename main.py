import random

def main():

    print("===== Quiz Master =====")

    questions = [
        {
            "question": "What is 15 + 27?",
            "options": [
                "A. 32",
                "B. 42",
                "C. 52",
                "D. 38"
            ],
            "answer": "B"
        },
        {
            "question": "What is 12 x 8?",
            "options": [
                "A. 86",
                "B. 92",
                "C. 96",
                "D. 108"
            ],
            "answer": "C"
        },
        {
            "question": "What is the square root of 81?",
            "options": [
                "A. 7",
                "B. 8",
                "C. 9",
                "D. 10"
            ],
            "answer": "C"
        },
        {
            "question": "If x + 7 = 15, what is the value of x?",
            "options": [
                "A. 6",
                "B. 7",
                "C. 8",
                "D. 9"
            ],
            "answer": "C"
        },
        {
            "question": "What is 25% of 200?",
            "options": [
                "A. 25",
                "B. 40",
                "C. 50",
                "D. 75"
            ],
            "answer": "C"
        }
    ]

    random.shuffle(questions)
 
    player_name = input("Enter your name : ").strip().title()
    print(f"welcome to Quiz Master, {player_name}!")
    print("-" * 38)

    score = 0
    total_questions = len(questions)

    

    for question in questions:
        question_text = question["question"]
        question_options = question["options"]
        print(question_text)
        for option in question_options:
            print(option)

        while True:
            chosen_option = input("choose an option (A,B,C,D): ").strip().upper()
            if chosen_option in ("A","B","C","D"):
                break
            else:
                print("Invalid option! Please choose A, B, C, or D. ")
                
                
                
        display_answer = question["answer"]
        if chosen_option == display_answer:
            score += 1
            print(f"The correct answer is: {display_answer} ✅")
        else:
            print("Incorrect correct! ❌")
            print(f"Correct! The answer is: {display_answer}")
    percentage = (score / total_questions) * 100
    print("~" * 38)
    print(f"Quiz completed, {player_name}!")
    print(f"Your score: {score}/{total_questions}")
    print(f"Percentage: {percentage}%")
    print("-" * 38)

if __name__ == "__main__":
    main()

 