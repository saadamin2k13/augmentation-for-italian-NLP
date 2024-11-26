############################################################################################

# the code below will extract all examples containing adverbs along with their example number
# (corresponding to original examples) and save the adverb examples in a new text file.

############################################################################################

# import re
#
# # Open the file and read lines
# with open('adverb_replacement_with_synonyms_x1.sbn', 'r') as file:
#     lines = file.readlines()
#
# # Function to check if an adverb representation is present in the logical part
# def contains_adverb(line):
#     # Use a regular expression to match any adverb representation
#     return re.search(r'\b\w+\.r\.\d+\b', line) is not None
#
# # Extract examples containing the specified adverb representation
# matching_examples = [(i + 1, line.strip()) for i, line in enumerate(lines) if contains_adverb(line)]
#
# # Print or save the matching examples with line numbers
# #for example_number, example in matching_examples:
#  #   print(f"Example {example_number}: {example}")
#
# # If you want to save matching examples with line numbers to a new file, you can use the following:
# with open('adverb_examples_with_numbers.txt', 'w') as output_file:
#      for example_number, example in matching_examples:
#          output_file.write(f"Example {example_number}: {example}\n")

############################################################################################

# the code below will extract all examples containing adverbs without their example number
# (corresponding to original examples) and save the adverb examples in a new text file.

############################################################################################

import re

# Open the file and read lines
with open('adverb_replacement_with_synonyms_x1.sbn', 'r') as file:
    lines = file.readlines()

# Function to check if an adverb representation is present in the logical part
def contains_adverb(line):
    # Use a regular expression to match any adverb representation
    return re.search(r'\b\w+\.r\.\d+\b', line) is not None

# Extract examples containing the specified adverb representation
matching_examples = [line.strip() for line in lines if contains_adverb(line)]

# Print or save the matching examples
# for example in matching_examples:
#     print(example)

# If you want to save matching examples to a new file, you can use the following:
with open('adverb_aug_examples_only_manually_corrected.txt', 'w') as output_file:
    for example in matching_examples:
        output_file.write(example + '\n')
