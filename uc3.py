def add_contact(contacts):
    first_name = input('Enter the first name: ')
    last_name = input('Enter the last name: ')
    address = input('Enter the address: ')
    city = input('Enter the city: ')
    state = input('Enter the state: ')
    zip = input('Enter the zip code: ')
    phone = input('Enter the phone number: ')
    email = input('Enter the email address: ')

    contact = {
        'first_name': first_name,
        'last_name': last_name,
        'address': address,
        'city': city,
        'state': state,
        'zip': zip,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)



def update_contact(contacts):
    first_name = input('Enter the first name of the contact to update: ')
    last_name = input('Enter the last name of the contact to update: ')
    field = input('Enter the field to update (e.g. email, phone): ')
  
    value = input('Enter the new value: ')
    updated_info = {field: value}

    for contact in contacts:
        if contact['first_name'] == first_name and contact['last_name'] == last_name:
            contact.update(updated_info)

  
    
def main():
    
  contacts = []
  flag = True
  while flag:
    print("\n***WELCOME TO ADDRESS BOOK***\n")
    print("Enter what you want to do: \n 1. Create and Add Contact  \n2. edit  \n3. Exit")
    option = int(input("Enter option: "))
    if option == 1:
        add_contact(contacts)

        # uc2 added ask for new contact
        while True:
            user_input = input('Add a new contact? (y/n) ')
            if user_input.lower() == 'y':
              add_contact(contacts)
            else:
                break
        print(contacts)
        
    elif option == 2:
        update_contact(contacts)
        print(contacts)

    elif option == 3:
        flag = False

if __name__ == "__main__":
    main()