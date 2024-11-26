# Read the dataset from a file
with open('noun_replacement_through_random_hyponyms.sbn', 'r') as f:
    dataset = f.readlines()

# Separate text and SBN and save them in separate files
text_file = open('cn_aug_text_only.txt', 'w')
sbn_file = open('cn_aug_sbn_only.txt', 'w')

for example in dataset:
    parts = example.strip().split('\t')
    if len(parts) == 2:
        text, sbn = parts
        text_file.write(text + '\n')
        sbn_file.write(sbn + '\n')

# Close the files
text_file.close()
sbn_file.close()
