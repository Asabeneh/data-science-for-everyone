import re
from pprint import pprint


def find_most_common_words(file_name='clown.txt', n=10):
    file_opened = open(file_name)
    words = []
    for line in file_opened:
        line = re.sub(r'[^a-zA-Z ]', '', line.strip()).split(' ')
        for word in line:
            words.append(word)
    dct = {}
    for word in words:
        if word not in dct:
            dct[word] = 1
        else:
            dct[word] += 1
    freq_table = []
    for key, value in dct.items():
        if value and key:
            freq_table.append((value, key))
        else:
            pass

    return sorted(freq_table, reverse=True)[:n+1]


print('=== ======')
filename_melina = '/Users/asabeneh/Desktop/projects/data-science-for-everyone/datasets/melina_trump_speech.txt'
filename_michelle = '/Users/asabeneh/Desktop/projects/data-science-for-everyone/datasets/michelle_obama_speech.txt'
pprint(find_most_common_words(filename_melina, 10))
pprint(find_most_common_words(filename_michelle, 10))

