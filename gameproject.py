import random
import time

def welcome():
    print("Welcome to the Advanced Computer Science Quiz!")
    playing = input("Do you want to play? (yes/no): ")
    if playing.lower() != "yes":
        print("Maybe next time!")
        quit()
    print("Great! Let's start :)")

def ask_question(question, answer, time_limit=10):
    """Ask a question with a timer and return if the answer was correct."""
    start_time = time.time()
    user_answer = input(question + " (You have " + str(time_limit) + " seconds): ")
    
    # Check if the answer was within the time limit
    if time.time() - start_time > time_limit:
        print("Time's up!")
        return False

    if user_answer.lower() == answer.lower():
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

def main():
    welcome()
    
    questions = {
        "What does CPU stand for?": "Central Processing Unit",
        "What does GPU stand for?": "Graphics Processing Unit",
        "What does RAM stand for?": "Random Access Memory",
        "What does PSU stand for?": "Power Supply Unit",
        "What does SSD stand for?": "Solid State Drive",
        "What does HTTP stand for?": "Hypertext Transfer Protocol",
        "What does AI stand for?": "Artificial Intelligence",
        "What does LAN stand for?": "Local Area Network"
    }
    
    score = 0
    num_questions = 4  # Number of questions to ask

    # Randomly select questions
    selected_questions = random.sample(list(questions.items()), num_questions)
    
    for question, answer in selected_questions:
        if ask_question(question, answer):
            score += 1

    # Calculate the score percentage
    score_percentage = (score / num_questions) * 100
    print("\nQuiz completed!")
    print(f"You answered {score} out of {num_questions} questions correctly.")
    print(f"Your score: {score_percentage}%")

    # Provide feedback based on performance
    if score_percentage == 100:
        feedback = "Excellent work! You mastered the quiz."
    elif score_percentage >= 75:
        feedback = "Great job! You have a strong understanding."
    elif score_percentage >= 50:
        feedback = "Good effort! Keep practicing to improve."
    else:
        feedback = "Keep learning! You'll get better with more study."
    
    print(feedback)
    
    # Save the score to a file
    with open("quiz_scores.txt", "a") as file:
        file.write(f"Score: {score_percentage}%\n")

if __name__ == "__main__":
    main()
