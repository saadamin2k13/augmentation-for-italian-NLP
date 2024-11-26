import re

# Define regular expression patterns to match state urdu_names
state_name_pattern_01 = r'state\.n\.01 Name "(.*?)"'
state_name_pattern_03 = r'state\.n\.03 Name "(.*?)"'
state_name_pattern_04 = r'state\.n\.04 Name "(.*?)"'

# Open the SBN file for reading
with open('gold_train.sbn', 'r') as sbn_file:
    sbn_data = sbn_file.readlines()

# Initialize lists and sets to store state urdu_names
all_state_names_01 = []
unique_state_names_01 = set()
all_state_names_03 = []
unique_state_names_03 = set()
all_state_names_04 = []
unique_state_names_04 = set()

# Loop through each line in the SBN data and extract state urdu_names
for line in sbn_data:
    state_match_01 = re.search(state_name_pattern_01, line)
    state_match_03 = re.search(state_name_pattern_03, line)
    state_match_04 = re.search(state_name_pattern_04, line)

    if state_match_01:
        state_name = state_match_01.group(1)
        all_state_names_01.append(state_name)
        unique_state_names_01.add(state_name)

    if state_match_03:
        state_name = state_match_03.group(1)
        all_state_names_03.append(state_name)
        unique_state_names_03.add(state_name)

    if state_match_04:
        state_name = state_match_04.group(1)
        all_state_names_04.append(state_name)
        unique_state_names_04.add(state_name)

# Specify the urdu_names of the output text files for all and unique state urdu_names
all_state_output_file_01 = 'all_state_names_01.txt'
unique_state_output_file_01 = 'unique_state_names_01.txt'
all_state_output_file_03 = 'all_state_names_03.txt'
unique_state_output_file_03 = 'unique_state_names_03.txt'
all_state_output_file_04 = 'all_state_names_04.txt'
unique_state_output_file_04 = 'unique_state_names_04.txt'

# Write all state urdu_names (n.01) to the output file, one name per line
with open(all_state_output_file_01, 'w') as all_state_output_01:
    for name in all_state_names_01:
        all_state_output_01.write(name + '\n')

# Write unique state urdu_names (n.01) to the output file, one name per line
with open(unique_state_output_file_01, 'w') as unique_state_output_01:
    for name in unique_state_names_01:
        unique_state_output_01.write(name + '\n')

# Write all state urdu_names (n.03) to the output file, one name per line
with open(all_state_output_file_03, 'w') as all_state_output_03:
    for name in all_state_names_03:
        all_state_output_03.write(name + '\n')

# Write unique state urdu_names (n.03) to the output file, one name per line
with open(unique_state_output_file_03, 'w') as unique_state_output_03:
    for name in unique_state_names_03:
        unique_state_output_03.write(name + '\n')

# Write all state urdu_names (n.04) to the output file, one name per line
with open(all_state_output_file_04, 'w') as all_state_output_04:
    for name in all_state_names_04:
        all_state_output_04.write(name + '\n')

# Write unique state urdu_names (n.04) to the output file, one name per line
with open(unique_state_output_file_04, 'w') as unique_state_output_04:
    for name in unique_state_names_04:
        unique_state_output_04.write(name + '\n')

print(f"Extracted all state names (n.01) saved to {all_state_output_file_01}")
print(f"Extracted unique state names (n.01) saved to {unique_state_output_file_01}")
print(f"Extracted all state names (n.03) saved to {all_state_output_file_03}")
print(f"Extracted unique state names (n.03) saved to {unique_state_output_file_03}")
print(f"Extracted all state names (n.04) saved to {all_state_output_file_04}")
print(f"Extracted unique state names (n.04) saved to {unique_state_output_file_04}")
