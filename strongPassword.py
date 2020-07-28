#! python3
#strongPassword.py - Sprawdza "siłę" hasła: min 8 znaków, małe i duże litery, min 1 cyfra

import re

print("Wprowadź hasło: ")
your_password = input()

def strong_password(password):
    if len(password) < 8:
        print("Hasło musi zawierać min. 8 znaków")

    digit_pass = re.compile(r"[0-9]+")
    mo1 = digit_pass.search(password)
    if mo1 == None:
        print("Hasło musi zawierać min. jedną cyfrę")
    else:
        print(mo1.group())

    upper_pass = re.compile(r"[A-Z]+")
    mo2 = upper_pass.search(password)
    if mo2 == None:
        print("Hasło musi zawierać min. jedną wielką literę")
    else:
        print(mo2.group())

strong_password(your_password)