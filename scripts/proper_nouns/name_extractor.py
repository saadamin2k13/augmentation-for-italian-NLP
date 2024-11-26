import re

# Define regular expression patterns to match male and female urdu_names
male_name_pattern = r'male\.n\.02 Name "(.*?)"'
female_name_pattern = r'female\.n\.02 Name "(.*?)"'

# Open the SBN file for reading

#### update file path accordingly #####

with open('gold_train.sbn', 'r') as sbn_file:
    sbn_data = sbn_file.readlines()

# Initialize lists and sets to store male and female urdu_names
all_male_names = []
unique_male_names = set()
all_female_names = []
unique_female_names = set()

# Loop through each line in the SBN data and extract male and female urdu_names
for line in sbn_data:
    male_match = re.search(male_name_pattern, line)
    female_match = re.search(female_name_pattern, line)

    if male_match:
        male_name = male_match.group(1)
        all_male_names.append(male_name)
        unique_male_names.add(male_name)

    if female_match:
        female_name = female_match.group(1)
        all_female_names.append(female_name)
        unique_female_names.add(female_name)

# Specify the urdu_names of the output text files for all and unique male and female urdu_names
all_male_output_file = 'all_male_names.txt'
unique_male_output_file = 'unique_male_names.txt'
all_female_output_file = 'all_female_names.txt'
unique_female_output_file = 'unique_female_names.txt'

# Write all male urdu_names to the male output file, one name per line
with open(all_male_output_file, 'w') as all_male_output:
    for name in all_male_names:
        all_male_output.write(name + '\n')

# Write unique male urdu_names to the unique male output file, one name per line
with open(unique_male_output_file, 'w') as unique_male_output:
    for name in unique_male_names:
        unique_male_output.write(name + '\n')

# Write all female urdu_names to the female output file, one name per line
with open(all_female_output_file, 'w') as all_female_output:
    for name in all_female_names:
        all_female_output.write(name + '\n')

# Write unique female urdu_names to the unique female output file, one name per line
with open(unique_female_output_file, 'w') as unique_female_output:
    for name in unique_female_names:
        unique_female_output.write(name + '\n')

print(f"Extracted all male names saved to {all_male_output_file}")
print(f"Extracted unique male names saved to {unique_male_output_file}")
print(f"Extracted all female names saved to {all_female_output_file}")
print(f"Extracted unique female names saved to {unique_female_output_file}")
