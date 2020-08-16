#! python3
# -*- coding: utf-8 -*-
# madLibs.py - finds word NOUN, VERB, ADVERB and ADJECTIVE in text and change they to inputted

import re

example_text = open("./madLibs.txt")
read_text = example_text.read()
print(read_text)    # line for test
print("\n")
find_word = re.compile(r"NOUN|VERB|ADJECTIVE|ADVERB")
results_list = find_word.findall(read_text)
print(results_list)     # line for test
print("\n")

# Addition new key word and change it in text
new_word = {}
num_noun = 0
num_verb = 0
num_adv = 0
num_adj = 0
for i in range(len(results_list)):
    if results_list[i] == "NOUN":
        new_word["noun{0}".format(num_noun)] = input("Podaj rzeczownik: \n")
        read_text = read_text.replace(results_list[i], new_word["noun{0}".format(num_noun)], 1)
        num_noun += 1
    elif results_list[i] == "VERB":
        new_word["verb{0}".format(num_verb)] = input("Podaj czasownik: \n")
        read_text = read_text.replace(results_list[i], new_word["verb{0}".format(num_verb)], 1)
        num_verb += 1
    elif results_list[i] == "ADVERB":
        new_word["adverb{0}".format(num_adv)] = input("Podaj przysłówek: \n")
        read_text = read_text.replace(results_list[i], new_word["adverb{0}".format(num_adv)], 1)
        num_adv += 1
    elif results_list[i] == "ADJECTIVE":
        new_word["adjective{0}".format(num_adj)] = input("Podaj przymiotnik: \n")
        read_text = read_text.replace(results_list[i], new_word["adjective{0}".format(num_adj)], 1)
        num_adj += 1
print(new_word)     # line for test
print("\n")
print(read_text)    # line for test
print("\n")

# TODO: Zapisanie tekstu w nowym pliku
example_text.close()
