import sys
import modulesBook
import modulesCMD

book = []
sysOps = sys.platform

modulesCMD.clearScreen(sysOps)

while True:

    print("Book is empty...\n")

    itemsNumber = modulesCMD.menu() #Get the number options in the modulesCMD
    
    #Control the input option selection
    try:
        funBook = int(input("Select one option: ")) 
    except ValueError:
        print("This is not an option")
        modulesCMD.clearScreen(sysOps)
        continue

    if funBook > itemsNumber:
        print("This is not an option")
        modulesCMD.clearScreen(sysOps)
        continue
    else:
        if funBook == 1: #This option adds a new contact to the book
            modulesBook.addRecord(book)
            modulesCMD.clearScreen(sysOps)
            continue
        elif funBook == 2: #This option updates a contact from the book
            modulesBook.editRecord(book)
            modulesCMD.clearScreen(sysOps)
            continue
        elif funBook == 3: #This option deletes a contact from the book 
            modulesBook.delRecord(book)
            modulesCMD.clearScreen(sysOps)
        elif funBook == 4: #This option lists every contact to the book
            modulesBook.contactList(book)
            modulesCMD.clearScreen(sysOps)
            continue
        elif funBook == 5: #This option close the program
            modulesCMD.clearScreen(sysOps)
            exit()
