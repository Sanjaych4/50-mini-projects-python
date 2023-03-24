# Day 42: A quiz application


# Define the questions and answers
questions = {
    
    # questions are generated using ChatGPT lol
    "Which of the following is the largest planet in our solar system?": {
        "a": "Jupiter",
        "b": "Saturn",
        "c": "Uranus",
        "d": "Neptune",
        "answer": "a"
    },
    "Who invented the telephone?": {
        "a": "Thomas Edison",
        "b": "Albert Einstein",
        "c": "Alexander Graham Bell",
        "d": "Isaac Newton",
        "answer": "c"
    },
    "Who is the creator of Python?": {
        "a": "Guido van Rossum",
        "b": "Bjarne Stroustrup",
        "c": "James Gosling",
        "d": "Larry Wall",
        "answer": "a"
    },
    "Which of the following is the longest river in Africa?": {
        "a": "Nile",
        "b": "Congo",
        "c": "Niger",
        "d": "Zambesi",
        "answer": "a"
    },
    "In which year did World War II begin?": {
        "a":"1940",
        "b":"1939",
        "c":"1941",
        "d":"1942",
        "answer": "b"
    },
    "Which famous artist painted the Mona Lisa?": {
        "a":"Michelangelo",
        "b":"Leonardo da Vinci",
        "c":"Pablo Picasso",
        "d":"Vincent van Gogh",
        "answer": "b"
    },
    "Which of the following is a type of pasta?": {
        "a":"Penne",
        "b":"Fettuccine",
        "c":"Rigatoni",
        "d":"All of the above",
        "answer": "d"
    },
    "Who wrote the novel To Kill a Mockingbird?": {
        "a":"Ernest Hemingway",
        "b":"Harper Lee",
        "c":"J.K. Rowling",
        "d":"Mark Twain",
        "answer": "b"
    },
    "Which planet in our solar system is known as the Red Planet?": {
        "a":"Mercury",
        "b":"Venus",
        "c":"Mars",
        "d":"Jupiter",
        "answer": "c"
    },
    "Which continent is home to the largest desert in the world?": {
        "a":"Africa",
        "b":"Asia",
        "c":"Antartica",
        "d":"South America",
        "answer": "a"
    },
    "Who was the first person to step on the moon?": {
        "a":"Buzz Aldrin",
        "b":"Michael Collins",
        "c":"Neil Armstrong",
        "d":"Yuri Gagarin",
        "answer": "c"
    },
    
    "What is the capital of Australia?": {
        "a": "Sydney",
        "b": "Melbourne",
        "c": "Canberra",
        "d": "Perth",
        "answer": "c"
    },
    "What is the highest mountain in the world?": {
        "a": "Mount Kilimanjaro",
        "b": "Mount Everest",
        "c": "Mount Fuji",
        "d": "Mount McKinley",
        "answer": "b"
    }
}

# Define a function to run the quiz
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question)
        for option in questions[question]:
            if option != "answer":
                print(option + ": " + questions[question][option])
        answer = input("Enter your answer (a, b, c, or d): ")
        if answer.lower() == questions[question]["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is " + questions[question]["answer"])
    print("You got " + str(score) + " out of " + str(len(questions)) + " questions correct.")

# Run the quiz
run_quiz(questions)
