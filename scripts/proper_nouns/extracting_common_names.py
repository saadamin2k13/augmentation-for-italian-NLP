# Read urdu_names from all_male_names.txt and female_names-1.txt into lists
with open('unique_male_names.txt', 'r') as male_file:
    male_names = [line.strip() for line in male_file]

with open('unique_female_names.txt', 'r') as female_file:
    female_names = [line.strip() for line in female_file]

# Convert the lists into sets for faster intersection check
male_names_set = set(male_names)
female_names_set = set(female_names)

# Find common urdu_names
common_names = male_names_set.intersection(female_names_set)

# Check if there are common urdu_names and print them
if common_names:
    print("Common urdu_names found:")
    for name in common_names:
        print(name)
else:
    print("No common urdu_names found.")
