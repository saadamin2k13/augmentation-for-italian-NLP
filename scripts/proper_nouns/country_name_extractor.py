import re

# Define a regular expression pattern to match country urdu_names
country_name_pattern = r'country\.n\.02 Name "(.*?)"'

# Open the SBN file for reading
with open('gold_train.sbn', 'r') as sbn_file:
    sbn_data = sbn_file.readlines()

# Initialize lists and a set to store country urdu_names
all_country_names = []
unique_country_names = set()

# Loop through each line in the SBN data and extract country urdu_names
for line in sbn_data:
    country_match = re.search(country_name_pattern, line)

    if country_match:
        country_name = country_match.group(1)
        all_country_names.append(country_name)
        unique_country_names.add(country_name)

# Specify the urdu_names of the output text files for all and unique country urdu_names
all_country_output_file = 'all_country_names.txt'
unique_country_output_file = 'unique_country_names.txt'

# Write all country urdu_names to the output file, one name per line
with open(all_country_output_file, 'w') as all_country_output:
    for name in all_country_names:
        all_country_output.write(name + '\n')

# Write unique country urdu_names to the output file, one name per line
with open(unique_country_output_file, 'w') as unique_country_output:
    for name in unique_country_names:
        unique_country_output.write(name + '\n')

print(f"Extracted all country names saved to {all_country_output_file}")
print(f"Extracted unique country names saved to {unique_country_output_file}")
