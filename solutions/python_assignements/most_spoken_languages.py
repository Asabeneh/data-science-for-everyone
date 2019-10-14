import json
import os
from pprint import pprint

def most_spoken_languages(n):
    filename ='/Users/asabeneh/Desktop/projects/data-science-for-everyone/datasets/countries_data.json'
    languages = {}
    with open(filename) as f:
        data = json.load(f)
        for country in data:
            for lang in country['languages']:
                if lang not in languages:
                    languages[lang] = 1
                else:
                    languages[lang] += 1
    freq_table = []
    for key, value in languages.items():
        freq_table.append((value, key))
    freq_table = sorted(freq_table, reverse=True)[:n+1]
    return freq_table


pprint(most_spoken_languages(10))
