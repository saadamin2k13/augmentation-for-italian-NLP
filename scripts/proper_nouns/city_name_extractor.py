import re

# Define regular expression patterns to match city urdu_names
city_name_pattern_01 = r'city\.n\.01 Name "(.*?)"'
city_name_pattern_03 = r'city\.n\.03 Name "(.*?)"'

# Open the SBN file for reading
with open('gold_train.sbn', 'r') as sbn_file:
    sbn_data = sbn_file.readlines()

# Initialize lists and sets to store city urdu_names
all_city_names_01 = []
unique_city_names_01 = set()
all_city_names_03 = []
unique_city_names_03 = set()

# Loop through each line in the SBN data and extract city urdu_names
for line in sbn_data:
    city_match_01 = re.search(city_name_pattern_01, line)
    city_match_03 = re.search(city_name_pattern_03, line)

    if city_match_01:
        city_name = city_match_01.group(1)
        all_city_names_01.append(city_name)
        unique_city_names_01.add(city_name)

    if city_match_03:
        city_name = city_match_03.group(1)
        all_city_names_03.append(city_name)
        unique_city_names_03.add(city_name)

# Specify the urdu_names of the output text files for all and unique city urdu_names
all_city_output_file_01 = 'all_city_names_01.txt'
unique_city_output_file_01 = 'unique_city_names_01.txt'
all_city_output_file_03 = 'all_city_names_03.txt'
unique_city_output_file_03 = 'unique_city_names_03.txt'

# Write all city urdu_names (n.01) to the output file, one name per line
with open(all_city_output_file_01, 'w') as all_city_output_01:
    for name in all_city_names_01:
        all_city_output_01.write(name + '\n')

# Write unique city urdu_names (n.01) to the output file, one name per line
with open(unique_city_output_file_01, 'w') as unique_city_output_01:
    for name in unique_city_names_01:
        unique_city_output_01.write(name + '\n')

# Write all city urdu_names (n.03) to the output file, one name per line
with open(all_city_output_file_03, 'w') as all_city_output_03:
    for name in all_city_names_03:
        all_city_output_03.write(name + '\n')

# Write unique city urdu_names (n.03) to the output file, one name per line
with open(unique_city_output_file_03, 'w') as unique_city_output_03:
    for name in unique_city_names_03:
        unique_city_output_03.write(name + '\n')

print(f"Extracted all city names (n.01) saved to {all_city_output_file_01}")
print(f"Extracted unique city names (n.01) saved to {unique_city_output_file_01}")
print(f"Extracted all city names (n.03) saved to {all_city_output_file_03}")
print(f"Extracted unique city names (n.03) saved to {unique_city_output_file_03}")
