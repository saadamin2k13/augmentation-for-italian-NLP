import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

def find_antonym(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    return antonyms

def get_adjectives_without_antonyms(dataset):
    adjectives_without_antonyms = set()
    for line in dataset:
        _, logical_representation = line.strip().split('\t')
        logical_adjectives = [word.split('.')[0] for word in logical_representation.split() if word.endswith('.a.01')]
        for adjective in logical_adjectives:
            antonyms = find_antonym(adjective)
            if not antonyms:
                adjectives_without_antonyms.add(adjective)
    return adjectives_without_antonyms

# Replace 'input_filename' with the path to your dataset file
input_filename = "./silver/silver.sbn"

with open(input_filename, "r") as infile:
    lines = infile.readlines()

adjectives_without_antonyms = get_adjectives_without_antonyms(lines)

print("Adjectives without antonyms in WordNet:")
for adjective in adjectives_without_antonyms:
    print(adjective)
