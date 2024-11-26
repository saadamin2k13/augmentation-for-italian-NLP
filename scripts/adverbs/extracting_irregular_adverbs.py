import re

in_file = '../../adjective_augmentation/silver/silver.sbn'
out_file = 'silver/silver_adverbs.txt'

adverbs = set()

with open(in_file) as f:
  lines = f.readlines()

for line in lines:
  text, logic = line.split('\t')

  matches = re.findall(r'\w+\.r.\d+', logic)

  for match in matches:
    adverb = match.split('.')[0]
    adverbs.add(adverb)

adverbs = list(adverbs)

with open(out_file, 'w') as f:
  for adverb in adverbs:
    f.write(adverb + '\n')

############################################

#
# import nltk
# import random
# from nltk.corpus import wordnet
# import re
# nltk.download('wordnet')
#
# manual_synonyms = {
#     "somewhat": ["slightly", "a little", "moderately"],
#     "away": ["gone", "absent", "off"],
#     "bareback": ["without a saddle", "unmounted"],
#     "all_of_a_sudden": ["suddenly"],
#     "all of a sudden": ["suddenly"],
#     "on board": ["aboard"],
#     "on_board": ["aboard"],
#     "sweetly": ["pleasantly", "charmingly", "nicely"],
#     "wrong": ["incorrectly", "mistakenly", "erroneously"],
#     "so": ["very", "extremely", "exceedingly"],
#     "bitterly": ["angrily", "resentfully", "acrimoniously"],
#     "just": ["only", "merely", "simply"],
#     "barely": ["scarcely", "hardly", "just"],
#     "directly": ["immediately", "straightaway", "promptly"],
#     "clearly": ["plainly", "evidently", "obviously"],
#     "a_bit": ["slightly"],
#     "a bit": ["slightly"],
#     "thoughtfully": ["considerately", "attentively", "reflectively"],
#     "apart": ["separately", "individually", "asunder"],
#     "badly": ["poorly", "ineffectively", "insufficiently"],
#     "out of the blue": ["unexpectedly"],
#     "out_of_the_blue": ["unexpectedly"],
#     "in_common": ["collectively"],
#     "in common": ["collectively"],
#     "askance": ["suspiciously", "skeptically", "doubtfully"],
#     "suspiciously": ["distrustfully", "skeptically", "warily"],
#     "greatly": ["significantly", "enormously", "markedly"],
#     "narrowly": ["barely", "closely", "tightly"],
#     "beautifully": ["gorgeously", "wonderfully", "exquisitely"],
#     "stark": ["completely", "entirely", "utterly"],
#     "too": ["excessively", "overly", "excessively"],
#     "officially": ["formally", "bureaucratically", "legally"],
#     "low": ["lowly", "unpretentious", "modestly"],
#     "voraciously": ["greedily", "ravenously", "hungrily"],
#     "inside_out": ["entirely"],
#     "inside out": ["entirely"],
#     "easily": ["effortlessly", "comfortably", "smoothly"],
#     "fully": ["completely", "entirely", "totally"],
#     "very": ["extremely", "exceedingly", "incredibly"],
#     "immediately": ["instantly", "promptly", "directly"],
#     "face to face": ["personally"],
#     "face_to_face": ["personally"],
#     "suddenly": ["abruptly", "unexpectedly", "all of a sudden"],
#     "well": ["healthy", "in good health", "sound"],
#     "aboard": ["on board", "on ship", "on deck"],
#     "sort_of": ["kind_of"],
#     "sort of": ["kind of"],
#     "dead": ["deceased", "lifeless", "deceased"],
#     "from_time_to_time": ["occasionally"],
#     "from time to time": ["occasionally"],
#     "most": ["very", "extremely", "supremely"],
#     "bravely": ["courageously", "valiantly", "heroically"],
#     "deeply": ["profoundly", "intensely", "profoundly"],
#     "merely": ["only", "just", "simply"],
#     "hard": ["difficultly", "laboriously", "strenuously"],
#     "highly": ["very", "extremely", "exceedingly"],
#     "in_effect": ["essentially"],
#     "in effect": ["essentially"],
#     "carefully": ["cautiously", "prudently", "attentively"],
#     "as": ["equally", "likewise", "similarly"],
#     "extremely": ["exceedingly", "incredibly", "exceptionally"],
#     "seriously": ["earnestly", "sincerely", "gravely"],
#     "comfortably": ["cozily", "snugly", "pleasantly"],
#     "automatically": ["spontaneously", "involuntarily", "reflexively"],
#     "thoroughly": ["completely", "entirely", "totally"],
#     "super": ["very", "extremely", "incredibly"],
#     "back": ["backward", "rearward", "behind"],
#     "hysterically": ["frantically", "uncontrollably", "wildly"],
#     "terribly": ["horribly", "dreadfully", "awfully"],
#     "grossly": ["flagrantly", "egregiously", "glaringly"],
#     "in_public": ["openly"],
#     "in public": ["openly"],
#     "brightly": ["brilliantly", "vividly", "radiantly"],
#     "secretly": ["covertly", "discreetly", "clandestinely"],
#     "straight": ["directly", "in a straight line", "evenly"],
#     "abreast": ["alongside", "side by side", "together"],
#     "tightly": ["firmly", "securely", "closely"],
#     "less": ["lesser", "not as much", "not so"],
#     "really": ["truly", "genuinely", "actually"],
#     "gracefully": ["elegantly", "gracefully", "beautifully"],
#     "quickly": ["rapidly", "swiftly", "speedily"],
#     "instantly": ["immediately", "promptly", "directly"],
#     "more": ["additionally", "further", "moreover"],
#     "across": ["over", "through", "spanning"],
#     "quietly": ["silently", "noiselessly", "softly"],
#     "a_little": ["a_bit"],
#     "a little": ["a bit"],
#     "visibly": ["noticeably", "clearly", "distinctly"],
#     "much": ["a lot", "greatly", "significantly"],
#     "girlishly": ["youthfully", "childishly", "naively"],
#     "certainly": ["definitely", "surely", "absolutely"],
#     "curiously": ["inquisitively", "inquiringly", "wonderingly"],
#     "loudly": ["noisily", "audibly", "boisterously"],
#     "safely": ["securely", "harmlessly", "without danger"],
#     "alas": ["regrettably", "unfortunately", "sorrowfully"],
#     "out": ["outside", "outdoors", "away"],
#     "widely": ["broadly", "extensively", "universally"],
#     "upwards": ["upward", "upwardly", "in an upward direction"],
#     "heavily": ["densely", "weightily", "massively"],
#     "calmly": ["tranquilly", "peacefully", "serenely"],
#     "gruesomely": ["horrifyingly", "shockingly", "dreadfully"],
#     "at_any_rate": ["nevertheless"],
#     "at any rate": ["nevertheless"],
#     "more_or_less": ["approximately"],
#     "more or less": ["approximately"],
#     "posthumously": ["after death", "mortuarily", "posthumously"],
#     "all_at_once": ["suddenly"],
#     "all at once": ["suddenly"],
#     "gently": ["softly", "tenderly", "mildly"],
#     "hesitantly": ["uncertainly", "tentatively", "reluctantly"],
#     "slightly": ["somewhat", "a little", "marginally"],
#     "scantily": ["sparsely", "meagerly", "barely"],
#     "by_heart": ["by_memory"],
#     "by heart": ["by memory"],
#     "politely": ["courteously", "respectfully", "mannerly"],
#     "pretty": ["rather", "quite", "fairly"],
#     "all": ["everything", "every bit", "everything considered"],
#     "mentally": ["intellectually", "cerebrally", "cognitively"],
#     "completely": ["entirely", "wholly", "fully"],
#     "after_all": ["nevertheless"],
#     "after all": ["nevertheless"],
#     "partially": ["partly", "incompletely", "fractionally"],
#     "rather": ["quite", "somewhat", "fairly"],
#     "furiously": ["angrily", "wrathfully", "fiercely"],
#     "temporarily": ["briefly", "for a short time", "momentarily"],
#     "usually": ["generally", "typically", "normally"],
#     "silently": ["quietly", "noiselessly", "mutely"],
#     "quite": ["rather", "fairly", "somewhat"],
#     "head_over_heels": ["passionately"],
#     "head over heels": ["passionately"],
#     "bright": ["radiant", "luminous", "gleaming"],
#     "totally": ["completely", "entirely", "wholly"],
#     "hopelessly": ["despairingly", "forlornly", "irretrievably"],
#     "kind_of": ["sort_of"],
#     "kind of": ["sort of"],
# }
#
#
# def find_synonyms(word):
#     synonyms = []
#     for syn in wordnet.synsets(word):
#         for lemma in syn.lemmas():
#             if lemma.synonyms():
#                 synonyms.append(lemma.synonyms()[0].name())
#     return synonyms
#
# def is_adverb_in_text(word, text):
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
# def replace_adverbs(sentence, logical_representation):
#     # Tokenize the sentence
#     tokens = nltk.word_tokenize(sentence)
#     # Extract adverbs from the logical representation
#     logical_adverbs = []
#     for sense in range(1, 10):  # Iterate from .a.01 to .a.09
#         logical_adverbs += [word.split('.')[0] for word in logical_representation.split() if
#                                   word.endswith(f'.r.{sense:02d}')]
#     #logical_adverbs = [word.split('.')[0] for word in logical_representation.split() if
#      #                   word.endswith('.r.01')]  # Assuming .r.01 represents adverbs
#
#     # Replace adverbs
#     replaced_sentence = sentence
#
#     for word in logical_adverbs:
#         if is_adverb_in_text(word, sentence):
#             synonyms = find_synonyms(word)
#
#             if word in manual_synonyms:
#                 synonyms.extend(manual_synonyms[word])
#
#             if synonyms:
#                 synonym = random.choice(synonyms)
#                 # Replace adverbs in both case-sensitive and case-insensitive forms
#                 replaced_sentence = replaced_sentence.replace(word, synonym)
#                 replaced_sentence = replaced_sentence.replace(word.capitalize(), synonym.capitalize())
#                 logical_representation = logical_representation.replace(word, synonym)
#
#     return replaced_sentence, logical_representation
#
# # Read the dataset from "gold_train.sbn"
# input_filename = "gold_train.sbn"
# output_filename = "adverb_replacement_with_synonyms_x1.sbn"
#
# with open(input_filename, "r") as infile:
#     lines = infile.readlines()
#
# # Perform adverb replacement and save the output
# replaced_dataset = []
#
# for line in lines:
#     sentence, logical_representation = line.strip().split('\t')
#     replaced_sentence, replaced_logical_representation = replace_adverbs(sentence,
#                                                                          logical_representation)
#     replaced_dataset.append((replaced_sentence, replaced_logical_representation))
#
# # Save the output to "adverb_replacement_with_synonyms.sbn"
# with open(output_filename, "w") as outfile:
#     for sentence, logical_representation in replaced_dataset:
#         outfile.write(f"{sentence}\t{logical_representation}\n")
