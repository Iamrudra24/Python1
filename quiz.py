# In-memory data storage
users = {}
scores = {}
logged_in_user = None

def register():
    """Register a new user."""
    global users
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username in users:
        print("Username already exists. Please try a different one.")
    else:
        users[username] = password
        print("Registration successful!")

def login():
    """Log in an existing user."""
    global logged_in_user
    username = input("Enter Username: ")
    if username in users:
        for _ in range(3):
            password = input("Enter Password: ")
            if users[username] == password:
                logged_in_user = username
                print("Login successful!")
                return True
            else:
                print("Incorrect password. Try again.")
        print("Maximum attempts exceeded.")
        return False
    else:
        print("Username not found. Please register first.")
        return False

def attempt_quiz():
    """Attempt a quiz and save the score."""
    global scores, logged_in_user
    if logged_in_user is None:
        print("Please log in first to attempt the quiz.")
        return
    
    quiz = [
        {"question": "Which SQL keyword is used to retrieve unique values from a column?",
         "options": ["A. DISTINCT", "B. UNIQUE", "C. FILTER", "D. EXCLUSIVE"],
         "answer": "A"},
        {"question": "What is the purpose of the SQL GROUP BY clause?",
         "options": ["A. To arrange records in ascending order", "B. To filter records by criteria",
                     "C. To group rows with the same values", "D. To delete duplicate rows"],
         "answer": "C"}
    ]
    
    score = 0
    for q in quiz:
        print(f"\n{q['question']}")
        for opt in q['options']:
            print(opt)
        answer = input("Enter your answer (A-D): ").upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 10
        else:
            print("Incorrect.")
    
    scores[logged_in_user] = score
    print(f"Quiz complete! Your score: {score}")

def view_results():
    """View the logged-in user's results."""
    global scores, logged_in_user
    if logged_in_user is None:
        print("Please log in first to view your score.")
        return
    
    if logged_in_user in scores:
        print(f"{logged_in_user} has scored {scores[logged_in_user]} points.")
    else:
        print("No score available. Please attempt the quiz first.")

def main():
    """Main function to run the application."""
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. View Results")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                pass  # User logged in successfully
        elif choice == "3":
            attempt_quiz()
        elif choice == "4":
            view_results()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
main()
