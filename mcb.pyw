#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: python mcb.pyw save <keyword> - Saves clipboard to keyword.
# python mcb.pyw <keyword> - Loads keyword to clipboard
# python mcb.pyw list <keyword> - Loads all keywords to clipboard

import shelve, pyperclip, sys


mcbShelf = shelve.open('mcb')

task = sys.argv[1].lower()

# Check command line arguments
if len(sys.argv) == 3:
    snippet = sys.argv[2]

    if task == 'save':
        # Save clipboard content
        mcbShelf[snippet] = pyperclip.paste()

    elif task == 'del':
        del mcbShelf[snippet]

elif len(sys.argv) == 2:
    # List keywords and load content
    
    if task == 'list':
        pyperclip.copy(str(mcbShelf.keys()))

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(str(mcbShelf[sys.argv[1]]))

    elif task == 'delall':
        #delete all entries

        print 'Deleting all Entries!'
        mcbShelf.clear()

    else:
        print('Unkonwn entry to complete!')
    
mcbShelf.close()
