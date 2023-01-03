def add_contact(contacts):

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
    # AddressBook= []
    contacts = []
    flag = True
    while flag:
        print("\n***WELCOME TO ADDRESS BOOK***\n")
        print("Enter what you want to do: \n 1. Create and Add Contact  \n2. Exit")
        option = int(input("Enter option: "))
        if option == 1:
            add_contact(contacts)
            print(contacts)

        elif option == 2:
            flag = False


if __name__ == "__main__":
    main()
