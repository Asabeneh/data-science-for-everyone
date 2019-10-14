import re
import pprint
from stop_words import stop_words as sw

file_name_melina = '/Users/asabeneh/Desktop/projects/data-science-for-everyone/datasets/melina_trump_speech.txt'
file_name_michelle = '/Users/asabeneh/Desktop/projects/data-science-for-everyone/datasets/michelle_obama_speech.txt'

def clean_text(file_name=file_name_melina):
    file_opened = open(file_name)
    words = []
    for line in file_opened:
        line = re.sub(r'[^a-zA-Z ]', '', line.strip()).split(' ')
        for word in line:
            words.append(word.lower().strip())
    file_opened.close()
    return words


def remove_support_words(words):
    main_words = []
    for word in words:
        if word not in sw:
            main_words.append(word)
    return main_words


def change_list_to_dict(lst):
    dct = {}
    for word in lst:
        if word not in dct:
            dct[word] = 1
        else:
            dct[word] += 1
    return dct


def freq_dist(dct):
    freq_table = []
    for key, value in dct.items():
        if key and value:
            freq_table.append((value, key))
    return sorted(freq_table, reverse=True)


melina_cleaned_words = clean_text(file_name_melina)
melina_main_words = remove_support_words(melina_cleaned_words)
melina_dct = change_list_to_dict(melina_main_words)
melina_word_freq = freq_dist(melina_dct)

michelle_cleaned_words = clean_text(file_name_michelle)
michelle_main_words = remove_support_words(michelle_cleaned_words)
michelle_dct = change_list_to_dict(michelle_main_words)
michelle_word_freq = freq_dist(michelle_dct)


def check_text_similarity():
    Melina = set(melina_main_words)
    Michelle = set(michelle_main_words)
    common = len(Melina.intersection(Michelle))
    melina_percentage = round(common * 100 / len(melina_main_words))
    michelle_percentage = round(common * 100 / len(michelle_main_words))

    return {
        'common_words': common,
        'melina__main_words': len(melina_main_words),
        'michelle_main_words': len(michelle_main_words),
        'melina_similarity':  str(melina_percentage) + ' %',
        'michelle_similarity':  str(michelle_percentage) + ' %',
    }


pprint.pprint(check_text_similarity())
