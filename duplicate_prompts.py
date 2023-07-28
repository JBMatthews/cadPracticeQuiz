import json

def find_duplicate_prompts(data):
    prompt_counts = {}
    duplicate_prompts = []

    for prompt in data:
        question = prompt.get("question")
        if question in prompt_counts:
            prompt_counts[question] += 1
            if prompt_counts[question] == 2:
                duplicate_prompts.append(question)
        else:
            prompt_counts[question] = 1

    return duplicate_prompts

def main():
    with open("quiz_data.json", "r") as file:
        data = json.load(file)

    duplicate_prompts = find_duplicate_prompts(data)
    print("Duplicate Prompts:")
    counter = 0
    for prompt in duplicate_prompts:
        counter += 1
        print(f"{counter}. {prompt}")

    total_duplicates = len(duplicate_prompts)
    print(f"Total Number of Duplicates: {total_duplicates}")

if __name__ == "__main__":
    main()
