# Read text and SBN from separate files
with open('./augmentation/english_aug_dataset_files/verb/ita_verb_text.txt', 'r') as text_file, open(
        './augmentation/english_aug_dataset_files/verb/ita_verb_sbn.txt', 'r') as sbn_file:
    text_lines = text_file.readlines()
    sbn_lines = sbn_file.readlines()

# Ensure both lists have the same number of lines
if len(text_lines) != len(sbn_lines):
    raise ValueError("The number of lines in text and SBN files does not match.")

# Combine text and SBN and save them back to a single file
with open('augmentation/italian_dataset/verb_aug_x1.sbn', 'w') as combined_file:
    for text, sbn in zip(text_lines, sbn_lines):
        combined_file.write(f"{text.strip()}\t{sbn.strip()}\n")