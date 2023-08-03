import json

def find_duplicate_prompts(data):
    prompt_counts = {}
    duplicate_prompts = []

    for question in data["questions"]:
        prompt = question.get("prompt")
        if prompt in prompt_counts:
            prompt_counts[prompt] += 1
            if prompt_counts[prompt] == 2:
                duplicate_prompts.append(prompt)
        else:
            prompt_counts[prompt] = 1

    return duplicate_prompts

def main():
    with open("quiz_data_cleaned.json", "r") as file:
        data = json.load(file)

    duplicate_prompts = find_duplicate_prompts(data)
    print("Duplicate Prompts:")
    for prompt in duplicate_prompts:
        print(prompt)

    total_duplicates = len(duplicate_prompts)
    print(f"Total Number of Duplicates: {total_duplicates}")

if __name__ == "__main__":
    main()
