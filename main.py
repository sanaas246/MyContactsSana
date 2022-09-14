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

def allnames():
    for contact in contacts:
        print(f"\n - {contact}")

def search(): # use a dictionary
    searchcontact = input("Please enter a contact you want to search up: ")
    if searchcontact in contacts:
        print(contacts.index(searchcontact))
    else:
        print("no contact found")

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
    if selection == "2" or selection == "search for contact":
        search()

