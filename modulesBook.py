def delRecord(book): #This function deteles a contact from specific name
    name = str(input("Please enter the contact name to delete: "))
    for i in book:
        if i.get("Name") == str(name):
            book.remove(i)
            print("The contact was deleted")

def addRecord(book): #This function adds a contact
    name = str(input("Enter the name: "))
    number = str(input("Enter the number: "))
    
    item = {
        "Name" : name,
        "Number" : number
    }

    book.append(item)

    print("The contact was created")
    return book

def editRecord(book): #This function edit number from a contact
    name = str(input("Enter the name: "))
    newNumber = str(input("Enter the new number: "))
    for i in book:
        if i.get("Name") == str(name):
            i.update({"Number" : newNumber})
            print("Thw contact was edited")

def __getItemAttribute(obj): #Private function that return the name attribute from an object
    return obj['Name']

def contactList(book): #This function return the list of contacts sort by name
    book.sort(key=__getItemAttribute)
    print("These are the contacts:")
    for i in book:
        print("Contact {} at {}".format(i.get("Name"), i.get("Number")))