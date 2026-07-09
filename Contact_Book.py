contacts = []

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        contacts.append(contact)
        print("Contact added successfully.")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContact List")
            for contact in contacts:
                print("----------------------------")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])

    elif choice == "3":
        search = input("Enter Name or Phone Number: ")

        found = False

        for contact in contacts:
            if search == contact["name"] or search == contact["phone"]:
                print("\nContact Found")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "4":
        phone = input("Enter Phone Number of the Contact to Update: ")

        found = False

        for contact in contacts:
            if phone == contact["phone"]:
                contact["name"] = input("Enter New Name: ")
                contact["phone"] = input("Enter New Phone Number: ")
                contact["email"] = input("Enter New Email: ")
                contact["address"] = input("Enter New Address: ")
                print("Contact updated successfully.")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "5":
        phone = input("Enter Phone Number of the Contact to Delete: ")

        found = False

        for contact in contacts:
            if phone == contact["phone"]:
                contacts.remove(contact)
                print("Contact deleted successfully.")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Book.")
        break

    else:
        print("Invalid choice. Please try again.")