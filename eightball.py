import random
import time

# Open the 8 ball text file
f = open('responses.txt', 'r')

# Read the whole file and store each line in a list
responses = f.readlines()

# Ask the user to input a yes or no question
question = input("Please ask me 'Yes' or 'No' question ")

# Pause for a couple seconds
time.sleep(2)

# Print a response
print(random.choice(responses))
