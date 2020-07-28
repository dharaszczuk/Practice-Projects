#! python3
# mcb.pyw - save and load text in clipboard
# use py.exe mcb.pyw save <key word> - save clipboard with key word
#     py.exe mcv.pyw <key word> - load key word to clipboard
#     py.exe mcb.pyw list - load all key word to clipboard
#     py.exe mcb.pyw delete - clear all key word
#     py.exe mcb.pyw delete <key word> - remove key word from base

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == "delete":
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()