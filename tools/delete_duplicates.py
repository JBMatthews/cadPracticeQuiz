import json

def remove_duplicate_prompts(data):
    prompt_counts = {}
    duplicate_indices = []

    for index, question in enumerate(data["questions"]):
        prompt = question.get("prompt")
        if prompt in prompt_counts:
            prompt_counts[prompt].append(index)
        else:
            prompt_counts[prompt] = [index]

    for prompt, indices in prompt_counts.items():
        if len(indices) > 1:
            duplicate_indices.extend(indices)

    for index in reversed(sorted(duplicate_indices)):
        del data["questions"][index]

def main():
    with open("quiz_data.json", "r") as file:
        data = json.load(file)

    remove_duplicate_prompts(data)

    with open("quiz_data_cleaned.json", "w") as outfile:
        json.dump(data, outfile, indent=2)

    print("Duplicate prompts removed. Cleaned data saved to 'sample_data_cleaned.json'.")

if __name__ == "__main__":
    main()
