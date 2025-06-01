import random

message = input("Let's predict your future! Please insert your question: ")

# Store the random choice in a variable
eight_ball = random.choice([
    "Yes - definitely.",
    "It is decidedly so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
])

print("The answer is:", eight_ball)