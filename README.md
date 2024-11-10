# Python_basic_quiz_game
# Advanced Computer Science Quiz

Welcome to the **Advanced Computer Science Quiz**! This interactive, timed quiz covers fundamental computer science topics. Test your knowledge and track your scores!

## Features

- Timed questions: Each question has a limited time to answer.
- Random selection: The quiz randomly selects questions each time you play.
- Score tracking: Your score is calculated and stored in a file for future reference.
- Feedback: Personalized feedback based on your quiz performance.

## Technologies Used

- **Python**: The entire quiz is implemented in Python, utilizing basic libraries like `time` and `random` for functionality.

## Prerequisites

- Python 3.x installed on your system.

## Getting Started


   How to Play
When prompted, type yes to start the quiz.
Answer each question within the time limit displayed (default: 10 seconds per question).
After each question, you’ll receive feedback on whether your answer was correct.
At the end of the quiz, you’ll see your score, percentage, and personalized feedback.
Your score is saved in a file named quiz_scores.txt in the same directory.
Project Structure
quiz.py: Main script containing the quiz logic.
quiz_scores.txt: Automatically generated file that logs scores after each quiz attempt.
Code Explanation
welcome(): Greets the user and starts the quiz if they choose to play.
ask_question(question, answer, time_limit): Asks a question with a time limit and checks the answer.
main(): Manages quiz flow, selects random questions, calculates the score, and provides feedback.
Score Saving: After the quiz, the score percentage is saved to quiz_scores.txt for future reference.
Contributing
Contributions are welcome! If you'd like to improve the quiz or add new features, please fork the repository and create a pull request.

License
This project is open-source and available under the MIT License.
