#! python3
#phoneAndEmial.py - Wyszukuje numery tel i adresy e-mail w tekście skopiowanym do schowka

"""Przykłądowy tekst  (415)-555-4242 ext 44 zawierający numery
422 111 4545 telefonów example@domain.com.pl
oraz adresy mail przyk_lad-owy@mail.com. Wystraczy skopiować."""

import re
import pyperclip

clipboard = str(pyperclip.paste())

find_num = re.compile(r"""(
    (\d{3}|\(\d{3}\))?                 #numer kierunkowy
    (\s|-|\.)?                         #separator
    (\d{3})                            #pierwsze 3 cyfry
    (\s|-|\.)?                         #separator
    (\d{4})                            #ostatnie cyfry
    (\s*(ext|x|ext.)\s*(\d{2,5}))?     #numer wewnętrzny
    )""", re.VERBOSE)

find_email = re.compile(r"""(
    ([a-zA-Z0-9._-])+       #nazwa użytkownika
    @                       #małpa
    ([a-zA-Z0-9._-])+       #nazwa domeny
    (\.[a-zA-Z]{2,4})+      #końcówka
    )""", re.VERBOSE)

clip_out = []
for groups in find_num.findall(clipboard):
    phone_num = "-".join([groups[1], groups[3], groups[5]])
    if groups[8]!= "":
        phone_num += " x" + groups[8]
    clip_out.append(phone_num)
for groups in find_email.findall(clipboard):
    clip_out.append(groups[0])

if len(clip_out) > 0:
    print("Skopiowano do schowka: ")
    print("\n".join(clip_out))
    pyperclip.copy("\n".join(clip_out))
else:
    print("Nie znaleziono numerów tel. i adresów e-mail")
