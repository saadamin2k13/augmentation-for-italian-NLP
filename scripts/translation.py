from googletrans import Translator

def translate_to_urdu(text):
    translator = Translator()
    translation = translator.translate(text, dest='en')
    return translation.text

def translate_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        input_sentences = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as output_file:
        for sentence in input_sentences:
            urdu_translation = translate_to_urdu(sentence.strip())
            output_file.write(f"{urdu_translation}\n")

input_file_path = 'ita.txt'  # Replace with your input file path
output_file_path = 'eng.txt'  # Replace with your desired output file path

translate_file(input_file_path, output_file_path)

#
# from googletrans import Translator
# import time
#
# def translate_to_english(texts):
#     translator = Translator()
#     translations = []
#     for text in texts:
#         try:
#             translation = translator.translate(text, dest='en')
#             translations.append(translation.text)
#         except Exception as e:
#             print(f"Error during translation: {e}")
#             translations.append(text)  # Append original text in case of error
#         time.sleep(1)  # Sleep to avoid hitting rate limits
#     return translations
#
# def translate_file(input_file, output_file, batch_size=100):
#     with open(input_file, 'r', encoding='utf-8') as file:
#         input_lines = file.readlines()
#
#     with open(output_file, 'w', encoding='utf-8') as out_file:
#         for i in range(0, len(input_lines), batch_size):
#             batch = input_lines[i:i + batch_size]
#             batch = [line.strip() for line in batch]
#             translations = translate_to_english(batch)
#             for translation in translations:
#                 out_file.write(f"{translation}\n")
#             print(f"Translated lines {i} to {i + batch_size}")
#
# if __name__ == "__main__":
#     input_file_path = 'ita.txt'  # Replace with your input file path
#     output_file_path = 'eng.txt'  # Replace with your desired output file path
#
#     translate_file(input_file_path, output_file_path)
