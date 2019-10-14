import re
import os
from pprint import pprint

filename = os.path.join(
    '/Users/asabeneh/Desktop/projects/data-science-for-everyone/datasets/email_exchanges_big.txt')

def extract_emails():
    file_name = input('Enter a file name: ')
    if file_name == '':
        file_name = filename
    try:
        file_opened = open(file_name, 'r')
        emails = []
        for line in file_opened:
            if re.match('[Ff]rom ', line.strip()):
                line = line.strip().split(' ')
                emails.append(line[1])
        file_opened.close()
        freq_dist = {}
        for email in emails:
            if email not in freq_dist:
                freq_dist[email] = 1
            else:
                freq_dist[email] += 1
        freq_dist_list = freq_dist.items()
        keys = freq_dist.keys()
        values = freq_dist.values()
        keys_and_values = sorted(freq_dist_list)
        final_freq_table = {}
        for key, value in keys_and_values:
            final_freq_table[value] = key
        final_freq_table = sorted(final_freq_table.items(), reverse=True)
        return final_freq_table
    except:
        return 'File was not found'


pprint(extract_emails())
