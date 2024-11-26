import re

# Open the file and read lines
with open('adverb_replacement_with_synonyms_x1.sbn', 'r') as file:
    lines = file.readlines()

# Function to check if a line does not contain any adverb representation
def does_not_contain_adverb(line):
    # Use a regular expression to check if no adverb representation is present
    return re.search(r'\b\w+\.r\.\d+\b', line) is None

# Extract examples that do not contain adverbs
non_adverb_examples = [line.strip() for line in lines if does_not_contain_adverb(line)]

# Save examples without adverbs to a new file
output_filename = 'examples_without_adverbs.txt'
with open(output_filename, 'w') as output_file:
    for example in non_adverb_examples:
        output_file.write(example + '\n')

print(f"Examples without adverbs saved to {output_filename}")
