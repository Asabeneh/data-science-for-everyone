## Python Exercises:

1. Find the total number of emails in the [emails_exchange_big](https://raw.githubusercontent.com/Asabeneh/data-science-for-everyone/master/datasets/email_exchanges_big.txt) text file and create a distribution frequency of the email and number of counts. You can call you function, extract_emails.
1. Find the most common [words](https://simple.wikipedia.org/wiki/Most_common_words_in_English) in the English language. Call the name of your function find_most_common_words, it will take two parameters which are a string or a file and a positive integer. Your function will return an array of tuples in descending order. Check the output

   ```py
   print(find_most_common_words('sample.txt', 10))

   [(10, 'the'),
   (8, 'be'),
   (6, 'to'),
   (6, 'of'),
   (5, 'and'),
   (4, 'a'),
   (4, 'in'),
   (3, 'that'),
   (2, 'have'),
   (2, 'I')]

   print(find_most_common_words('sample.txt', 5))

   [(10, 'the'),
   (8, 'be'),
   (6, 'to'),
   (6, 'of'),
   (5, 'and')]
   ```

1. Write a python application which checks similarity between two texts. It takes a file or a string a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of [michelle's](https://github.com/Asabeneh/data-science-for-everyone/blob/master/datasets/michelle_obama_speech.txt) and [melina's](https://github.com/Asabeneh/data-science-for-everyone/blob/master/datasets/michelle_obama_speech.txt) speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
1. Develop a program which calculate the measure of central tendency of a sample(mean, median, mode) and measure of variability(range, variance, standard deviation). In addition to those measure, find the min, max, count and frequency distribution of the sample. Check the output below.

   ```py
   ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

   print('Count:', data.count()) # 25
   print('Sum: ', data.sum()) # 744
   print('Min: ', data.min()) # 24
   print('Max: ', data.max()) # 38
   print('Range: ', data.range() # 14
   print('Mean: ', data.mean()) # 30
   print('Median: ',data.median()) # 29
   print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
   print('Variance: ',data.var()) # 17.5
   print('Standard Deviation: ', data.std()) # 4.2
   print('Variance: ',data.var()) # 17.5
   print('Frequency Distribution: ',data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

   print(data.describe())
   Count: 25
   Sum:  744
   Min:  24
   Max:  38
   Range:  14
   Mean:  30
   Median:  29
   Mode:  (26, 5)
   Variance:  17.5
   Standard Deviation:  4.2
   Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
   ```

1. Find the ten most spoken languages from the [countries](https://github.com/Asabeneh/data-science-for-everyone/blob/master/datasets/countries_data.json) data json file. You can call your function, find_ten_most_spoken_languages.

Solutions for the assignment is available [here](https://github.com/Asabeneh/data-science-for-everyone/tree/master/solutions)

If you want to practice python checkout the [python](https://github.com/Asabeneh/Python-for-Everyone/blob/master/python_for_everyone.ipynb) for everyone material.
