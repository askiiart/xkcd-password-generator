import csv
import random

with open('1k_most_common_words.txt', 'rt') as words_file:
    reader = csv.reader(words_file, delimiter='\n')
    words = []
    for row in reader:
        if row:
            words.append(row[0])

for _ in range(4):
    print(words[random.randint(0, len(words))].title(), end='')
