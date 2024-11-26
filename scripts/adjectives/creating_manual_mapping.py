# Read the data from your text file
with open('./silver/silver_custom_adjectives_with_antonyms.txt', 'r') as file:
    data = file.readlines()

# Create a dictionary to store the data
antonyms_dict = {}

# Parse the data and populate the dictionary
for line in data:
    words = line.strip().split(" - ")
    if len(words) == 2:
        antonym_list = antonyms_dict.get(words[0], [])
        antonym_list.append(words[1])
        antonyms_dict[words[0]] = antonym_list

# Convert the dictionary into the desired pattern
output = "{\n"
for key, values in antonyms_dict.items():
    output += f'    "{key}": {str(values)},\n'
output += "}"

# Write the output to a new text file
with open('./silver/silver_dict_antonyms.txt', 'w') as file:
    file.write(output)
