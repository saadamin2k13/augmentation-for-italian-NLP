# # Read unique female urdu_names into a set
# with open('unique_female_names.txt', 'r') as female_file:
#     female_names = {line.strip() for line in female_file}
#
# # Read unique male urdu_names into a list
# with open('unique_male_names.txt', 'r') as male_file:
#     male_names = [line.strip() for line in male_file]
#
# # Remove female urdu_names that are also in the male urdu_names set
# filtered_male_names = [name for name in male_names if name not in female_names]
#
# # Save the filtered male urdu_names into a separate text file
# with open('filtered_male_names-1.txt', 'w') as filtered_file:
#     for name in filtered_male_names:
#         filtered_file.write(name + '\n')
#
# print("Filtered male urdu_names saved to 'filtered_male_names-1.txt'")

# Read unique female urdu_names into a set
with open('../../common_noun_augmented_data/ss_noun_distribution/sst-data-processing/unique_nouns_sbn.txt', 'r') as female_file:
    female_names = {line.strip() for line in female_file}

# Read unique male urdu_names into a list
with open('../../common_noun_augmented_data/ss_noun_distribution/sst-data-processing/filtered_nouns_through_sst.txt', 'r') as male_file:
    male_names = [line.strip() for line in male_file]

# Remove female urdu_names that are also in the male urdu_names set
filtered_male_names = [name for name in male_names if name not in female_names]

# Save the filtered male urdu_names into a separate text file
with open(
        '../../common_noun_augmented_data/ss_noun_distribution/sst-data-processing/noun_difference_bwt_sbn_and_sst.txt', 'w') as filtered_file:
    for name in filtered_male_names:
        filtered_file.write(name + '\n')

print("Filtered male urdu_names saved to 'filtered_male_names-1.txt'")
