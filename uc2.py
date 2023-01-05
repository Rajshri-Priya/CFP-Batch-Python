from typing import Dict

contacts = []


# uc1
def get_contact_info():
    return {
        'first_name': input('Enter the first name: '),
        'last_name': input('Enter the last name: '),
        'address': input('Enter the address: '),
        'city': input('Enter the city: '),
        'state': input('Enter the state: '),
        'zip': input('Enter the zip code: '),
        'phone': input('Enter the phone number: '),
        'email': input('Enter the email address: ')
    }


# uc2
def add_contact(contact_info: Dict[str, str]):
    contact = contact_info
    contacts.append(contact)


def main():
    contacts = []
    flag = True
    while flag:
        print("\n***WELCOME TO ADDRESS BOOK***\n")
        print(
            "Enter what you want to do: \n1. Create Contact and Add Contact  \n2. Edit  \n3. Delete \n4. Add multiple contacts \n5. Add multiple AddressBook \n6. Exit")
        option = int(input("Enter option: "))
        if option == 1:
            contact_info = get_contact_info()
            add_contact(contact_info)
            print(contact_info)

        elif option == 6:
            flag = False


main()
