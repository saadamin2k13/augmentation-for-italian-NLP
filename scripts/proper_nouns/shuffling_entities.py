import random


# Function to shuffle the content of a text file
def shuffle_file_content(input_file, output_file):
    # Read data from the input file
    with open(input_file, 'r') as file:
        data = file.readlines()

    # Shuffle the data randomly
    random.shuffle(data)

    # Write the shuffled data to the output file
    with open(output_file, 'w') as file:
        file.writelines(data)


# Input and output file urdu_names
input_file_name = '../inside_context/p_nouns_from_sbn/names/female_names.txt'  # Replace with your input file name
output_file_name = '../inside_context/p_nouns_from_sbn/names/shuffled_female_names.txt'  # Replace with your desired output file name

# Shuffle the content of the input file and save it to the output file
shuffle_file_content(input_file_name, output_file_name)

print(f"Shuffled content saved to {output_file_name}")
