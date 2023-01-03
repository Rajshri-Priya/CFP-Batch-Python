def add_contact(contacts):

    # uc2
    first_name = input('Enter the first name: ')
    last_name = input('Enter the last name: ')
    address = input('Enter the address: ')
    city = input('Enter the city: ')
    state = input('Enter the state: ')
    zip = input('Enter the zip code: ')
    phone = input('Enter the phone number: ')
    email = input('Enter the email address: ')


    # uc1 
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

    # uc2 
    contacts.append(contact)




def main():

  contacts = []
  flag = True
  while flag:
    print("\n***WELCOME TO ADDRESS BOOK***\n")
    print("Enter what you want to do: \n 1. Create and Add Contact  \n2. Exit")
    option = int(input("Enter option: "))
    if option == 1:
        add_contact(contacts)

        # uc5 added ask for multile contact
        while True:
            user_input = input('Add a new contact? (y/n) ')
            if user_input.lower() == 'y':
              add_contact(contacts)
            else:
                break
        print(contacts)

    elif option == 2:
        flag = False

  
main()