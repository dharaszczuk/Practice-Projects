#! python3
# mcb.pyw - save and load text in clipboard
# use py.exe mcb.pyw save <key word> - save clipboard with key word
#     py.exe mcv.pyw <key word> - load key word to clipboard
#     py.exe mcb.pyw list - load all key word to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

#TODO: Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #TODO: Print list of key word and load content
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()