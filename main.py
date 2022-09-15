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
def allnames():
    for contact in contacts:
        print(contact["name"])
    # Using index:
    # for i in range(len(contacts)):
    #     print(contacts[i]["name"])

def search(): 
    searchcontact = input("Please enter a contact you want to search up: ")
    found = True
    for contact in contacts:
        if contact["name"] == searchcontact:
            print("\n",contact["name"]) 
            print(contact["number"]) 
            print(contact["email"])
        else:
            print("Name not found in contacts.")
            break

def edit():
    print("edit")

def new():
    print("new")

def remove():
    print("remove")

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

