import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import random  # Import the random module

# Initialize the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to check if a word is a common noun and exists in various forms in the text
def is_common_noun_in_text(word, text):
    # Generate possible forms of the word
    forms = set()
    forms.add(word.lower())  # Lower-case
    forms.add(word.upper())  # Upper-case
    forms.add(word.capitalize())  # Cap-case
    forms.add(lemmatizer.lemmatize(word.lower(), 'v'))  # Base form (verb)

    # Check if any form of the word is present in the text
    for form in forms:
        if form in text.lower():
            return True
    return False

# Function to replace common nouns with random hypernyms
def replace_common_nouns_with_hyponyms(sentence, logical_representation):
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)

    # Extract nouns from the logical representation for all possible senses (from .n.01 to .n.09)
    logical_nouns = []
    for sense in range(1, 100):  # Iterate from .n.01 to .n.09
        logical_nouns += [word.split('.')[0] for word in logical_representation.split() if
                          word.endswith(f'.v.{sense:02d}')]

    # Replace common nouns with random hypernyms
    replaced_sentence = sentence

    for word in logical_nouns:
        if is_common_noun_in_text(word, sentence):
            synsets = wordnet.synsets(word)
            if synsets:
                hyponyms = []
                for synset in synsets:
                    hyponyms.extend(synset.hyponyms())  # Get a list of hyponyms for each synset

                if hyponyms:
                    # Choose a random hyponym from the list
                    random_hyponym = random.choice(hyponyms)
                    #random_hyponym = random.choice([t for t in hyponyms if t.name().split('.')[0] != word])

                    hyponym_word = random_hyponym.name().split('.')[0]
                    # Replace nouns in both case-sensitive and case-insensitive forms
                    replaced_sentence = replaced_sentence.replace(word, hyponym_word)
                    replaced_sentence = replaced_sentence.replace(word.capitalize(), hyponym_word.capitalize())
                    logical_representation = logical_representation.replace(word, hyponym_word)
                else:
                    hyponym_word = word
                    logical_representation = logical_representation.replace(word, hyponym_word)

    return replaced_sentence, logical_representation

# Read the dataset from "gold_train.sbn"
input_filename = "../italian-english/italian_gold_silver_eng_dataset.txt"
output_filename = "../italian-english/augmentation/english_aug_dataset_files/verb/eng_verb_aug.sbn"

with open(input_filename, "r") as infile:
    lines = infile.readlines()

# Perform common noun replacement and save the output
replaced_dataset = []

for line in lines:
    sentence, logical_representation = line.strip().split('\t')
    replaced_sentence, replaced_logical_representation = replace_common_nouns_with_hyponyms(sentence,
                                                                                             logical_representation)
    replaced_dataset.append((replaced_sentence, replaced_logical_representation))

# Save the output to "noun_replacement_through_first_hypernym.sbn"
with open(output_filename, "w") as outfile:
    for sentence, logical_representation in replaced_dataset:
        outfile.write(f"{sentence}\t{logical_representation}\n")
