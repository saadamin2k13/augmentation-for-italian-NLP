# Initialize dictionaries to store the mappings
name_to_shuffled = {}
shuffled_to_name = {}

# Read the original urdu_names from urdu_names.txt
with open('../outside_context/p_nouns_from_sbn/names/male/filtered_male_names-1.txt', 'r') as names_file:
    original_names = names_file.readlines()

# Read the shuffled urdu_names from shuffled_names.txt
with open('../outside_context/p_nouns_from_sbn/names/male/random_male_names-4.txt', 'r') as shuffled_names_file:
    shuffled_names = shuffled_names_file.readlines()

# Iterate through the original and shuffled urdu_names and create the dictionary
for original, shuffled in zip(original_names, shuffled_names):
    original = original.strip()  # Remove leading/trailing whitespace
    shuffled = shuffled.strip()  # Remove leading/trailing whitespace

    # Assign the mapping to the dictionaries
    name_to_shuffled[original] = shuffled
    shuffled_to_name[shuffled] = original

# Specify the name of the output text file
output_file = '../outside_context/p_nouns_from_sbn/names/male/male_names_mapping.txt'

# Write the dictionaries to the output text file
with open(output_file, 'w') as text_file:
    for name, shuffled in name_to_shuffled.items():
        text_file.write(f"'{name}' : '{shuffled}',\n")

print(f"Dictionary mappings saved to {output_file}")
