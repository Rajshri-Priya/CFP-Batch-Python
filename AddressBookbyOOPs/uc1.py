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

    def display_contact(self):
        for contact in self.contacts:
            print(
                f"First name: {contact.first_name}\nLast name: {contact.last_name}\nAddress: {contact.address}\nCity: {contact.city}\nState: {contact.state}\nZip: {contact.zip}\nPhone: {contact.phone}\nEmail: {contact.email}")


address_book = AddressBook()  # obj of class

while True:
    print("***WELCOME TO ADDRESSBOOK***")
    print('1. Create and Add contact \n2. View contacts \n3. Quit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        contact_info = address_book.get_contact_info()

    elif choice == 2:
        address_book.display_contact()

    elif choice == 3:
        break
