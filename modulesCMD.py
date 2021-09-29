import os 

def clearScreen(sysOps): #This function clean the os screen
    if sysOps == "linux":
        input("Press any key to continue...")
        os.system("clear")
    else:
        input("Press any key to continue...")
        os.system("cls")

def menu(): #This function show the book menu
    menuItems = ['1.- Add a contact', '2.- Update a contact', '3.- Delete a contact', '4.- List of Contacts', '5.- Exit']
    
    menuItems.sort()

    for item in menuItems:
        print(item)
    
    return len(menuItems)