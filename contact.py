from _ast import Add

import contact

contacts = {}
def Addcontact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    if Name in contacts:
        print("This contact already exists.")
    else:
        contacts[Name] = phone
        print("Contact added successfully.")

def Deletecontact():
    name = input("Enter Name: ")
    if Name in contacts:
        Delcontacts[Name]
        print("Contact deleted successfully.")
    else:
        print("This contact does not exist.")

def Updatecontact():
    Name = input("Enter Name: ")
    for contact in contacts:
        if contact == Name:
            phone = input("Enter the new phone number: ")
            contacts[Name] = phone
            print("Contact updated successfully.")
            break
    else:
        print("This contact does not exist.")

def Searchcontact():
    name = input("Enter Name: ")
    for contact in contacts:
        if contact.lower()== Name.lower():
            print("Contact Found")
            print(contact, contacts[contact])
            break
    else:
        print("Contact not found.")

def Displaycontacts():
    if contacts == {}:
        print("There are no contacts.")
    else:
        print("Contacts List:")
        for name, phone in contacts.items():
            print(name, phone)
while True:
    print("\nContact Book Menu:")
    print("1. AddContact")
    print("2. DeleteContact")
    print("3. UpdateContact")
    print("4. SearchContact")
    print("5. DisplayContacts")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        Addcontact()
    elif choice == 2:
        Deletecontact()
    elif choice == 3:
        Updatecontact()
    elif choice == 4:
        Searchcontact()
    elif choice == 5:
        Displaycontacts()
    elif choice == 6:
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")