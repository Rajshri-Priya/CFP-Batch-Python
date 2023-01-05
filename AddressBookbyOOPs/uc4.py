from typing import Dict


class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email


class AddressBook:
    def __init__(self):
        self.contacts = []

    # uc2
    def add_contact(self, contact_info: Dict[str, str]):

        contact = Contact(**contact_info)
        self.contacts.append(contact)

    # uc1
    def get_contact_info(self):
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

    # uc3
    def edit_contact(self):
        first_name = input('Enter the first name of the contact to edit: ')
        last_name = input('Enter the last name of the contact to edit: ')
        field = input('Enter the field to update (first_name, last_name, address, city, state, zip, phone, email): ')
        new_value = input('Enter the new value: ')

        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                setattr(contact, field, new_value)
                return True
            return False

    # uc4
    def delete_contact(self):
        first_name = input('Enter the first name of the contact to delete: ')
        last_name = input('Enter the last name of the contact to delete: ')

        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                return True
            return False

    def display_contact(self):

        for contact in self.contacts:
            # print(self.contacts)
            print(
                f"First name: {contact.first_name}\nLast name: {contact.last_name}\nAddress: {contact.address}\nCity: {contact.city}\nState: {contact.state}\nZip: {contact.zip}\nPhone: {contact.phone}\nEmail: {contact.email}")


address_book = AddressBook()  # obj of class

while True:
    print("***WELCOME TO ADDRESSBOOK***")
    print('1. Create and Add contact \n2. View contacts \n3. Edit contact \n4. Delete contact \n5. Quit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        contact_info = address_book.get_contact_info()
        address_book.add_contact(contact_info)

    elif choice == 2:
        address_book.display_contact()

    elif choice == 3:
        success = address_book.edit_contact()
        if success:
            print('Contact updated successfully')
        else:
            print('Contact not found')

    elif choice == 4:
        success = address_book.delete_contact()
        if success:
            print('Contact deleted successfully')
        else:
            print('Contact not found')

    elif choice == 5:
        break
