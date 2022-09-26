# My Contacts Assignment by Sana S

# Contacts List
contacts = [{
    "name": "John Doe", 
    "number": "888555", 
    "email": "johndoe@email.com"
    }, 
{
    "name": "Jane Doe", 
    "number": "333777", 
    "email": "janedoe@email.com"
    }, 
{
    "name": "Mary Doe", 
    "number": "111222", 
    "email": "marydoe@email.com"
    }]

# Functions
def searchArray(name):
    for i in range (len(contacts)):
        if contacts[i]["name"] == name:
            return i
    return -1

def allnames():
    for contact in contacts:
        print(contact["name"])

def search(): 
    searchcontact = input("Please enter a contact you want to search up: ")
    index = searchArray(searchcontact)
    if index != -1:
        print(contacts[index]["name"]) 
        print(contacts[index]["number"]) 
        print(contacts[index]["email"])
    else:
        print("Contact not found")   

def edit():
    updatecontact = input("Please enter a contact you want to update: ")
    index = searchArray(updatecontact)
    if index != -1:
        contacts[index]["name"] = input("What is the new name of this contact? ")
        contacts[index]["number"] = input("What is the new email for this contact? ")
        contacts[index]["email"] = input("What is the new number for this contact? ")
    else:
        print("Contact not found")

def new():
    newname = input("What is the new name of this contact? ")
    newemail = input("What is the new email for this contact? ")
    newnumber = input("What is the new number for this contact? ")
    print("Contact Added")
    newcontact = {
        "name": newname,
        "email": newemail,
        "number": newnumber
    }
    contacts.append(newcontact)

def remove():
    removename = input("What is the name of the contact you would like to delete? ")
    index = searchArray(removename)
    if index != -1:
        del contacts[index]
    else:
        print("Contact not found")

def exit():
    loop = False
    print("\nBye!")

# Main Menu
loop = True 
while loop: 
    # Menu Options
    print(f"\n********MAIN MENU********")
    print("1. Display Contact Names")
    print("2. Search for Contact")
    print("3. Edit Contact")
    print("4. New Contact")
    print("5. Remove Contact")
    print("6. Exit")
    selection = input("\nChoose an option please: ").lower()

    if selection == "1" or selection == "display contact names":
        allnames()
    elif selection == "2" or selection == "search for contact":
        search()
    elif selection == "3" or selection == "edit contact":
        edit()
    elif selection == "4" or selection == "new contact":
        new()
    elif selection == "5" or selection == "remove contact":
        remove()
    elif selection == "6" or selection == "exit":
        exit()
    else: 
        print("Please choose an option. ")

