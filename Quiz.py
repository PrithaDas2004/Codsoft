# Define some questions as a list of dictionaries
questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["London", "Paris", "Berlin", "Rome"],
        "correct_answer": 1  # Index of the correct answer in the answers list
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answers": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_answer": 2
    },
    # Add more questions here...
]

# Function to ask a question and check the answer
def ask_question(question_data):
  print(question_data["question"])
  for i, answer in enumerate(question_data["answers"]):
    print(f"{i+1}. {answer}")
  user_answer = int(input("Enter your answer (by number): ")) - 1
  return user_answer == question_data["correct_answer"]

# Keep track of score
score = 0

# Loop through questions and ask
for question in questions:
  if ask_question(question):
    score += 1
    print("Correct!")
  else:
    print("Incorrect.")

# Print the final score
print(f"You finished the quiz with a score of {score} out of {len(questions)}.")
