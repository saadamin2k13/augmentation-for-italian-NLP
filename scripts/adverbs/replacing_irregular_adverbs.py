# import random
#
# manual_synonyms = {
#     "all_of_a_sudden": ["suddenly"],
#     "all of a sudden": ["suddenly"],
#     "on board": ["aboard"],
#     "on_board": ["aboard"],
#     "a_bit": ["slightly"],
#     "a bit": ["slightly"],
#     "out of the blue": ["unexpectedly"],
#     "out_of_the_blue": ["unexpectedly"],
#     "in_common": ["collectively"],
#     "in common": ["collectively"],
#     "inside_out": ["entirely"],
#     "inside out": ["entirely"],
#     "face to face": ["personally"],
#     "face_to_face": ["personally"],
#     "sort_of": ["kind_of"],
#     "sort of": ["kind of"],
#     "from_time_to_time": ["occasionally"],
#     "from time to time": ["occasionally"],
#     "in_effect": ["essentially"],
#     "in effect": ["essentially"],
#     "in_public": ["openly"],
#     "in public": ["openly"],
#     "a_little": ["a_bit"],
#     "a little": ["a bit"],
#     "at_any_rate": ["nevertheless"],
#     "at any rate": ["nevertheless"],
#     "more_or_less": ["approximately"],
#     "more or less": ["approximately"],
#     "all_at_once": ["suddenly"],
#     "all at once": ["suddenly"],
#     "by_heart": ["by_memory"],
#     "by heart": ["by memory"],
#     "after_all": ["nevertheless"],
#     "after all": ["nevertheless"],
#     "head_over_heels": ["passionately"],
#     "head over heels": ["passionately"],
#     "kind_of": ["sort_of"],
#     "kind of": ["sort of"],
# }
# def replace_exact_phrases_with_synonyms(sentence, synonyms_dict):
#     # Initialize an empty list to store the final sentence
#     replaced_sentence = []
#
#     # Split the sentence into words
#     words = sentence.split()
#
#     i = 0
#     while i < len(words):
#         word = words[i]
#
#         # Check if the current word and the next word together form a phrase in the dictionary
#         if i < len(words) - 1 and (word + ' ' + words[i + 1]) in synonyms_dict:
#             # Randomly choose a synonym for the phrase
#             synonym = random.choice(synonyms_dict[word + ' ' + words[i + 1]])
#             replaced_sentence.append(synonym)
#             # Skip the next word since it's part of the phrase
#             i += 2
#         else:
#             # If the current word is not part of a phrase, add it as is to the final sentence
#             replaced_sentence.append(word)
#             i += 1
#
#     # Reconstruct the sentence
#     replaced_sentence = ' '.join(replaced_sentence)
#     return replaced_sentence
#
# # Example usage for replacing phrases in a file
# input_file_path = "gold_train.sbn"  # Replace with the path to your input file
# output_file_path = "output.sbn"  # Replace with the path to your output file
#
# with open(input_file_path, "rt") as fin, open(output_file_path, "wt") as fout:
#     for line in fin:
#         replaced_line = replace_exact_phrases_with_synonyms(line.strip(), manual_synonyms)
#         fout.write(replaced_line + '\n')

#input file
fin = open("../gold.sbn", "rt")
#output file to write the result to
fout = open("output.sbn", "wt")
#for each line in the input file
for line in fin:
#read replace the string and write to output file

  ####### the line below is used for PMB-3.0.0
  #fout.write(line.replace('TPR t1 "now"', 'TPR "now" t1'))
  ####### the line below is used for PMB-5.0.0
#      "all_of_a_sudden": ["suddenly"],
# #     "all of a sudden": ["suddenly"],

    #fout.write(line.replace('all_of_a_sudden', 'suddenly'))
    fout.write(line.replace('all of a sudden', 'suddenly'))
    #
    # fout.write(line.replace('on_board', 'aboard'))
    # fout.write(line.replace('on board', 'aboard'))
    #
    # fout.write(line.replace('a_bit', 'slightly'))
    # fout.write(line.replace('a bit', 'slightly'))
    #
    # fout.write(line.replace('out_of_the_blue', 'unexpectedly'))
    # fout.write(line.replace('out of the blue', 'unexpectedly'))
    #
    # fout.write(line.replace('in_common', 'collectively'))
    # fout.write(line.replace('in common', 'collectively'))
    #
    # fout.write(line.replace('inside_out', 'entirely'))
    # fout.write(line.replace('inside out', 'entirely'))
    # fout.write(line.replace('face_to_face', 'personally'))
    # fout.write(line.replace('face to face', 'personally'))
    # fout.write(line.replace('sort_of', 'kind_of'))
    # fout.write(line.replace('sort of', 'kind of'))
    #
    # fout.write(line.replace('from time to time', 'occasionally'))
    # fout.write(line.replace('from_time_to_time', 'occasionally'))
    # fout.write(line.replace('in effect', 'essentially'))
    # fout.write(line.replace('in_effect', 'essentially'))
    # fout.write(line.replace('in_public', 'openly'))
    # fout.write(line.replace('in public', 'openly'))
    # fout.write(line.replace('a_little', 'a_bit'))
    # fout.write(line.replace('a little', 'a bit'))
    # fout.write(line.replace('at_any_rate', 'nevertheless'))
    # fout.write(line.replace('at any rate', 'nevertheless'))
    # fout.write(line.replace('more or less', 'approximately'))
    # fout.write(line.replace('more_or_less', 'approximately'))
    # fout.write(line.replace('all at once', 'suddenly'))
    # fout.write(line.replace('all_at_once', 'suddenly'))
    # fout.write(line.replace('by heart', 'by memory'))
    # fout.write(line.replace('by_heart', 'by_memory'))
    # fout.write(line.replace('after_all', 'nevertheless'))
    # fout.write(line.replace('after all', 'nevertheless'))
    # fout.write(line.replace('head_over_heels', 'passionately'))
    # fout.write(line.replace('head over heels', 'passionately'))
    # fout.write(line.replace('kind of', 'sort of'))
    # fout.write(line.replace('kind_of', 'sort_of'))
#close input and output files
fin.close()
fout.close()