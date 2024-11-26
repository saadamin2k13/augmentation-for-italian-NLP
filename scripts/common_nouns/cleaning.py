import re

# Define the input and output file paths
input_file_path = 'cn_aug_text_only.txt'  # Change this to the path of your input text file
output_file_path = 'cn_aug_text_cleaned.txt'  # Change this to the path where you want to save the cleaned data

def remove_underscores_and_hyphens(text):
    # Use regular expression to replace underscores and hyphens with spaces
    cleaned_text = re.sub(r'[_-]', ' ', text)
    return cleaned_text

# Read data from the input file
with open(input_file_path, 'r') as input_file:
    data = input_file.readlines()

# Process and clean the data
cleaned_data = [remove_underscores_and_hyphens(sentence) for sentence in data]

# Save the cleaned data to the output file
with open(output_file_path, 'w') as output_file:
    for sentence in cleaned_data:
        output_file.write(sentence)

print(f"Cleaned data saved to {output_file_path}")
