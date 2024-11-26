# Read the dataset from a file
with open(
        '../../data-augmentation-versions/adjective_augmentation/adjective_replacement_with_antonyms_x1.sbn', 'r') as f:
    dataset = f.readlines()

# Separate text and SBN and save them in separate files
text_file = open('eng_gold_silver/adj/eng_gold_adj_text.txt', 'w')
sbn_file = open('eng_gold_silver/adj/ita_gold_adj_sbn.txt', 'w')

for example in dataset:
    parts = example.strip().split('\t')
    if len(parts) == 2:
        text, sbn = parts
        text_file.write(text + '\n')
        sbn_file.write(sbn + '\n')

# Close the files
text_file.close()
sbn_file.close()
