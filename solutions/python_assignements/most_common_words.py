import re


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


print(find_most_common_words('melina_trump_speech.txt', 10))
print('=== ======')
print(find_most_common_words('michelle_obama_speech.txt', 10))
print(find_most_common_words('obama_speech.txt', 10))
print(find_most_common_words('donald_speech.txt', 10))
