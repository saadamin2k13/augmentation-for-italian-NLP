# # # import nltk
# # # from nltk.corpus import wordnet
# # # import re
# # #
# # # nltk.download('wordnet')
# # #
# # # def find_antonym(word):
# # #     antonyms = []
# # #     for syn in wordnet.synsets(word):
# # #         for lemma in syn.lemmas():
# # #             if lemma.antonyms():
# # #                 antonyms.append(lemma.antonyms()[0].name())
# # #     return antonyms
# # #
# # # def replace_adjectives(input_file, output_file):
# # #     with open(input_file, 'r') as f:
# # #         input_data = f.read()
# # #
# # #     lines = input_data.split('\n')
# # #     new_lines = []
# # #
# # #     for line in lines:
# # #         parts = line.split('\t')
# # #         if len(parts) != 2:
# # #             new_lines.append(line)
# # #             continue
# # #
# # #         text, sbn = parts[0], parts[1]
# # #         sbn_tokens = sbn.split()
# # #
# # #         for i in range(len(sbn_tokens)):
# # #             if re.match(r'^[a-zA-Z]+\.a\.\d{2}$', sbn_tokens[i]):
# # #                 adjective = sbn_tokens[i].split('.')[0]
# # #                 antonyms = find_antonym(adjective)
# # #                 if antonyms:
# # #                     new_adjective = antonyms[0]
# # #                     sbn_tokens[i] = sbn_tokens[i].replace(adjective, new_adjective)
# # #                     text = text.replace(adjective, new_adjective)
# # #
# # #         new_sbn = ' '.join(sbn_tokens)
# # #         new_line = '\t'.join([text, new_sbn])
# # #         new_lines.append(new_line)
# # #
# # #     with open(output_file, 'w') as f:
# # #         f.write('\n'.join(new_lines))
# # #
# # # input_file = "gold_train.sbn"
# # # output_file = "replaced_adjectives.sbn"
# # replace_adjectives(input_file, output_file)
#
#
# import nltk
# from nltk.corpus import wordnet
# import re
# import random
#
# nltk.download('wordnet')
#
# def find_antonym(word):
#     antonyms = []
#     for syn in wordnet.synsets(word):
#         for lemma in syn.lemmas():
#             if lemma.antonyms():
#                 antonyms.append(lemma.antonyms()[0].name())
#     return antonyms
#
# def is_adjective_in_text(word, text):
#     # Generate possible forms of the word
#     forms = set()
#     forms.add(word.lower())  # Lower-case
#     forms.add(word.upper())  # Upper-case
#     forms.add(word.capitalize())  # Cap-case
#
#     # Check if any form of the word is present in the text
#     for form in forms:
#         if form in text.lower():
#             return True
#     return False
#
# def replace_adjectives_with_antonyms(sentence, logical_representation):
#     # Tokenize the sentence
#     tokens = nltk.word_tokenize(sentence)
#
#     # Extract adjectives from the logical representation for all possible senses (from .a.01 to .a.09)
#     logical_adjectives = []
#     for sense in range(1, 10):  # Iterate from .a.01 to .a.09
#         logical_adjectives += [word.split('.')[0] for word in logical_representation.split() if
#                               word.endswith(f'.a.{sense:02d}')]
#
#     # Replace adjectives with their antonyms
#     replaced_sentence = sentence
#
#     for word in logical_adjectives:
#         if is_adjective_in_text(word, sentence):
#             antonyms = find_antonym(word)
#             print(antonyms)
#             if antonyms:
#                 random_antonym = random.choice(antonyms)
#                 # Replace adjectives in both case-sensitive and case-insensitive forms
#                 replaced_sentence = replaced_sentence.replace(word, random_antonym)
#                 replaced_sentence = replaced_sentence.replace(word.capitalize(), random_antonym.capitalize())
#                 logical_representation = logical_representation.replace(word, random_antonym)
#
#     return replaced_sentence, logical_representation
#
# # Read the dataset from "gold_train.sbn"
# input_filename = "gold_train.sbn"
# output_filename = "adjective_replacement_through_antonyms.sbn"
#
# with open(input_filename, "r") as infile:
#     lines = infile.readlines()
#
# # Perform adjective replacement and save the output
# replaced_dataset = []
#
# for line in lines:
#     sentence, logical_representation = line.strip().split('\t')
#     replaced_sentence, replaced_logical_representation = replace_adjectives_with_antonyms(sentence,
#                                                                                            logical_representation)
#     replaced_dataset.append((replaced_sentence, replaced_logical_representation))
#
# # Save the output to "adjective_replacement_through_antonyms.sbn"
# with open(output_filename, "w") as outfile:
#     for sentence, logical_representation in replaced_dataset:
#         outfile.write(f"{sentence}\t{logical_representation}\n")
#
#
# # import nltk
# # from nltk.corpus import wordnet
# # import re
# # import random
# #
# # #nltk.download('wordnet')
# #
# # def find_antonym(word):
# #     antonyms = []
# #     for syn in wordnet.synsets(word):
# #         for lemma in syn.lemmas():
# #             if lemma.antonyms():
# #                 antonyms.append(lemma.antonyms()[0].name())
# #     return antonyms
# #
# # def is_adjective_in_text(word, text):
# #     # Generate possible forms of the word
# #     forms = set()
# #     forms.add(word.lower())  # Lower-case
# #     forms.add(word.upper())  # Upper-case
# #     forms.add(word.capitalize())  # Cap-case
# #
# #     # Check if any form of the word is present in the text
# #     for form in forms:
# #         if form in text.lower():
# #             return True
# #     return False
# #
# # def replace_adjectives_with_antonyms(sentence, logical_representation):
# #     # Tokenize the sentence
# #     tokens = nltk.word_tokenize(sentence)
# #
# #     # Extract adjectives from the logical representation for all possible senses (from .a.01 to .a.09)
# #     logical_adjectives = []
# #     for sense in range(1, 10):  # Iterate from .a.01 to .a.09
# #         logical_adjectives += [word.split('.')[0] for word in logical_representation.split() if
# #                               word.endswith(f'.a.{sense:02d}')]
# #
# #     # Replace adjectives with their antonyms
# #     replaced_sentence = sentence
# #
# #     for word in logical_adjectives:
# #         if is_adjective_in_text(word, sentence):
# #             antonyms = find_antonym(word)
# #             if antonyms:
# #                 antonym = random.choice(antonyms)
# #                 # Replace adjectives in both case-sensitive and case-insensitive forms
# #                 replaced_sentence = replaced_sentence.replace(word, antonym)
# #                 replaced_sentence = replaced_sentence.replace(word.capitalize(), antonym.capitalize())
# #                 logical_representation = logical_representation.replace(word, antonym)
# #
# #     return replaced_sentence, logical_representation
# #
# # # Read the dataset from "gold_train.sbn"
# # input_filename = "gold_train.sbn"
# # output_filename = "adjective_replacement_through_antonyms.sbn"
# #
# # with open(input_filename, "r") as infile:
# #     lines = infile.readlines()
# #
# # # Perform adjective replacement and save the output
# # replaced_dataset = []
# #
# # for line in lines:
# #     sentence, logical_representation = line.strip().split('\t')
# #     replaced_sentence, replaced_logical_representation = replace_adjectives_with_antonyms(sentence,
# #                                                                                            logical_representation)
# #     replaced_dataset.append((replaced_sentence, replaced_logical_representation))
# #
# # # Save the output to "adjective_replacement_through_antonyms.sbn"
# # with open(output_filename, "w") as outfile:
# #     for sentence, logical_representation in replaced_dataset:
# #         outfile.write(f"{sentence}\t{logical_representation}\n")

import nltk
from nltk.corpus import wordnet
import re
import random

nltk.download('wordnet')

# Manually curated list of antonyms (add your own)
manual_antonyms = {
    "shocked": ['unsurprised'],
    "allergic": ['immune', 'resistant', 'unresponsive'],
    "favorite": ['disliked', 'unpopular', 'least-favorite'],
    "naked": ['clothed'],
    "unbeatable": ['beatable'],
    "amused": ['bored'],
    "amazing": ['ordinary'],
    "old-fashioned": ['modern'],
    "puzzled": ['clear'],
    "riveting": ['boring'],
    "homesick": ['content'],
    "paraplegic": ['able-bodied'],
    "messy": ['tidy'],
    "absurd": ['logical'],
    "disgusted": ['pleased'],
    "laid-back": ['uptight'],
    "heartbroken": ['elated'],
    "astonished": ['unsurprised'],
    "excellent": ['poor'],
    "proficient": ['inexperienced'],
    "not_guilty": ['guilty'],
    "commonplace": ['extraordinary'],
    "according": ['disagreeing'],
    "orange": ['non-orange'],
    "famous": ['unknown'],
    "magnificent": ['ordinary'],
    "shaky": ['stable'],
    "worn_out": ['refreshed'],
    "shaken": ['steady'],
    "fed_up": ['satisfied'],
    "aspiring": ['settled'],
    "anxious": ['calm'],
    "acquainted": ['unfamiliar'],
    "sore": ['painless'],
    "silent": ['noisy'],
    "self-proclaimed": ['humble'],
    "scared": ['brave'],
    "upper": ['lower'],
    "sunny": ['cloudy'],
    "ruined": ['restored'],
    "manipulative": ['honest'],
    "dizzy": ['steady'],
    "deadly": ['harmless'],
    "tiny": ['huge'],
    "outraged": ['pleased'],
    "mad": ['sane'],
    "overdue": ['early'],
    "risky": ['safe'],
    "purple": ['non-purple'],
    "frustrated": ['satisfied'],
    "frantic": ['calm'],
    "groggy": ['alert'],
    "two-faced": ['genuine'],
    "newborn": ['mature'],
    "smashed": ['intact'],
    "autobiographical": ['fictional'],
    "dumb": ['intelligent'],
    "defective": ['flawless'],
    "stressful": ['relaxing'],
    "well-known": ['obscure'],
    "world-wide": ['local'],
    "out_of_print": ['in-print'],
    "beige": ['colorful'],
    "nonsense": ['sense'],
    "waterproof": ['non-waterproof'],
    "understanding": ['misunderstanding'],
    "brown": ['non-brown'],
    "utter": ['partial'],
    "olympic": ['non-olympic'],
    "orphaned": ['parented'],
    "silly": ['serious'],
    "notorious": ['unknown'],
    "lucrative": ['unprofitable'],
    "huge": ['tiny'],
    "ancient": ['modern'],
    "deserted": ['populated'],
    "inseparable": ['separable'],
    "drunken": ['sober'],
    "magic": ['mundane'],
    "unimpressed": ['impressed'],
    "overweight": ['underweight'],
    "middle-aged": ['young'],
    "anorexic": ['healthy'],
    "merry": ['sad'],
    "neck_and_neck": ['unequal'],
    "indie": ['mainstream'],
    "prone": ['averse'],
    "state": ['unsettle'],
    "hallucinating": ['sane'],
    "hesitant": ['confident'],
    "grey": ['colorful'],
    "in_effect": ['ineffective'],
    "decapitated": ['intact'],
    "final": ['initial'],
    "gullible": ['skeptical'],
    "terrible": ['wonderful'],
    "booked": ['available'],
    "mediocre": ['exceptional'],
    "exhausting": ['energizing'],
    "teenage": ['adult'],
    "terrifying": ['comforting'],
    "exceptional": ['average'],
    "insolent": ['respectful'],
    "humiliating": ['uplifting'],
    "ajar": ['closed'],
    "skillful": ['unskilled'],
    "horrified": ['delighted'],
    "great": ['terrible'],
    "lesbian": ['heterosexual'],
    "secret": ['open'],
    "vigorous": ['feeble'],
    "scary": ['comforting'],
    "jealous": ['content'],
    "antique": ['modern'],
    "bright_blue": ['dull'],
    "unperturbed": ['disturbed'],
    "ruling": ['subject'],
    "located": ['misplaced'],
    "suspicious": ['trusting'],
    "fierce": ['gentle'],
    "over": ['under'],
    "fabulous": ['ordinary'],
    "innovative": ['conventional'],
    "unbiased": ['biased'],
    "epic": ['ordinary'],
    "close_at_hand": ['distant'],
    "mistaken": ['correct'],
    "ironic": ['straightforward'],
    "economical": ['extravagant'],
    "sleepy": ['awake'],
    "yellow": ['non-yellow'],
    "futile": ['effective'],
    "disappointed": ['satisfied'],
    "dyslexic": ['fluent'],
    "conceited": ['humble'],
    "undiscovered": ['well-known'],
    "dumbfounded": ['unsurprised'],
    "arcane": ['well-known'],
    "chestnut": ['non-chestnut'],
    "delicious": ['unappetizing'],
    "headstrong": ['flexible'],
    "irrefutable": ['debatable'],
    "smashing": ['failure'],
    "rare": ['common'],
    "handsome": ['ugly'],
    "total": ['partial'],
    "recent": ['ancient'],
    "outstanding": ['mediocre'],
    "faded": ['vibrant'],
    "lazy": ['diligent'],
    "hazel": ['non-hazel'],
    "outdated": ['modern'],
    "empathetic": ['indifferent'],
    "biased": ['unbiased'],
    "good-for-nothing": ['valuable'],
    "parliamentary": ['autocratic'],
    "venomous": ['harmless'],
    "charming": ['repulsive'],
    "gorgeous": ['ugly'],
    "countless": ['finite'],
    "in_love": ['indifferent'],
    "fake": ['genuine'],
    "hereditary": ['acquired'],
    "boastful": ['humble'],
    "awesome": ['awful'],
    "all_right": ['terrible'],
    "excruciating": ['bearable'],
    "handicapped": ['able-bodied'],
    "vital": ['trivial'],
    "swarthy": ['pale'],
    "sticky": ['slippery'],
    "bilingual": ['monolingual'],
    "wealthy": ['impoverished'],
    "cozy": ['uncomfortable'],
    "arrogant": ['humble'],
    "pink": ['non-pink'],
    "first-class": ['low-class'],
    "about": ['definite'],
    "roasted": ['raw'],
    "escaped": ['captured'],
    "divorced": ['married'],
    "decayed": ['fresh'],
    "wounded": ['uninjured'],
    "corporate": ['individual'],
    "bulky": ['compact'],
    "man-made": ['natural'],
    "blue": ['non-blue'],
    "ok": ['terrible'],
    "at_large": ['captured'],
    "diaphanous": ['opaque'],
    "economic": ['extravagant'],
    "elder": ['younger'],
    "paralyzed": ['mobile'],
    "gray-haired": ['young'],
    "nuts": ['sane'],
    "agog": ['indifferent'],
    "crimson": ['pale'],
    "electronic": ['analog'],
    "poisonous": ['harmless'],
    "aristocratic": ['common'],
    "crazy": ['sane'],
    "adjacent": ['distant'],
    "wonderful": ['terrible'],
    "light-blue": ['dark'],
    "embarrassed": ['confident'],
    "athletic": ['unathletic'],
    "entire": ['partial'],
    "nervous": ['calm'],
    "southeastern": ['northwestern'],
    "cute": ['ugly'],
    "excessive": ['moderate'],
    "shabby": ['stylish'],
    "stocky": ['slender'],
    "pathetic": ['impressive'],
    "lonely": ['accompanied'],
    "tired_of": ['enthusiastic_about'],
    "splendid": ['ordinary'],
    "pedantic": ['relaxed'],
    "top-secret": ['public'],
    "used_to": ['unfamiliar_with'],
    "abhorrent": ['admirable'],
    "polluted": ['clean'],
    "hammered": ['sober'],
    "various": ['identical'],
    "angelic": ['devilish'],
    "cynical": ['optimistic'],
    "obscene": ['decent'],
    "baffled": ['certain'],
    "iron": ['fragile'],
    "confusing": ['clear'],
    "tragic": ['joyful'],
    "abysmal": ['excellent'],
    "wooden": ['flexible'],
    "abandoned": ['inhabited'],
    "bright-red": ['dull'],
    "stoned": ['sober'],
    "northeastern": ['southwestern'],
    "tipsy": ['sober'],
    "creepy": ['comforting'],
    "funny": ['serious'],
    "salted": ['unsalted'],
    "weird": ['normal'],
    "belligerent": ['peaceful'],
    "expert": ['novice'],
    "vulgar": ['refined'],
}

def find_antonym(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    return antonyms

def is_adjective_in_text(word, text):
    # Generate possible forms of the word
    forms = set()
    forms.add(word.lower())  # Lower-case
    forms.add(word.upper())  # Upper-case
    forms.add(word.capitalize())  # Cap-case

    # Check if any form of the word is present in the text
    for form in forms:
        if form in text.lower():
            return True
    return False

def replace_adjectives(sentence, logical_representation):
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)

    # Extract adjectives from the logical representation for all possible senses (from .a.01 to .a.09)
    logical_adjectives = []
    for sense in range(1, 10):  # Iterate from .a.01 to .a.09
        logical_adjectives += [word.split('.')[0] for word in logical_representation.split() if
                              word.endswith(f'.a.{sense:02d}')]

    # Replace adjectives
    replaced_sentence = sentence

    for word in logical_adjectives:
        if is_adjective_in_text(word, sentence):
            antonyms = find_antonym(word)

            # Use a manually curated list if available
            if word in manual_antonyms:
                antonyms.extend(manual_antonyms[word])

            if antonyms:
                antonym = random.choice(antonyms)
                # Replace adjectives in both case-sensitive and case-insensitive forms
                replaced_sentence = replaced_sentence.replace(word, antonym)
                replaced_sentence = replaced_sentence.replace(word.capitalize(), antonym.capitalize())
                logical_representation = logical_representation.replace(word, antonym)

    return replaced_sentence, logical_representation

# Read the dataset from "gold_train.sbn"
input_filename = "../italian-english/italian_gold_silver_eng_dataset.txt"
output_filename = "../italian-english/augmentation/english_aug_dataset_files/adj/eng_adjective_aug.sbn"

with open(input_filename, "r") as infile:
    lines = infile.readlines()

# Perform adjective replacement and save the output
replaced_dataset = []

for line in lines:
    sentence, logical_representation = line.strip().split('\t')
    replaced_sentence, replaced_logical_representation = replace_adjectives(sentence,
                                                                           logical_representation)
    replaced_dataset.append((replaced_sentence, replaced_logical_representation))

# Save the output to "adjective_replacement_with_antonyms_x1.sbn"
with open(output_filename, "w") as outfile:
    for sentence, logical_representation in replaced_dataset:
        outfile.write(f"{sentence}\t{logical_representation}\n")
