import json

# Read the JSON file
with open('quiz_data.json') as file:
    data = json.load(file)

# Count the number of questions/prompts
question_count = len(data['questions'])

# Print the result
print(f"Number of questions/prompts: {question_count}")