#! python3
#madLibs.py - finds word NOUN, VERB, ADVERB and ADJECTIVE in text and change they to inputted

import os, re

#TODO: Otworzenie pliku z tekstem
example_text = open("./madLibs.txt")
read_text = example_text.read()
print(read_text)

#TODO: Wyszukanie słowa kluczowego w tekście
find_word = re.compile(r"NOUN|VERB|ADJECTIVE|ADVERB")
results_list = find_word.findall(read_text)
print(results_list[0])


# TODO: Wprowadzenie nowych słów
# TODO: Podmiana słów w tekście
# TODO: Zapisanie tekstu w nowym pliku

example_text.close()