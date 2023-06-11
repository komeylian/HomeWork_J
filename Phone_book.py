# 1402-03-09
# pip install ast

import ast


def load_phone_book():
    try:
        with open('phone_book.txt', 'r') as file:
            phone_book_data = file.read()
            if phone_book_data:
                return ast.literal_eval(phone_book_data)
    except FileNotFoundError:
        pass
    return {}


def save_phone_book(phone_book):
    with open('phone_book.txt', 'w') as file:
        file.write(str(phone_book))


def add_contact(phone_book):
    name = input("Enter the contact name: ")
    numbers = input("Enter phone numbers (comma-separated): ").split(',')
    phone_book[name] = numbers
    save_phone_book(phone_book)
    print(f"Contact '{name}' added successfully.")


def delete_contact(phone_book):
    name = input("Enter the contact name: ")
    if name in phone_book:
        del phone_book[name]
        save_phone_book(phone_book)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")


def update_contact(phone_book):
    name = input("Enter the contact name: ")
    if name in phone_book:
        numbers = input(
            "Enter updated phone numbers (comma-separated): ").split(',')
        phone_book[name] = numbers
        save_phone_book(phone_book)
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")


def search_contact(phone_book):
    search_term = input("Enter the search (Number / contact): ")
    found = False

    # Search by contact name
    for name, numbers in phone_book.items():
        if search_term.lower() in name.lower():
            print(f"Contact: {name}")
            print("Phone Numbers:")
            for number in numbers:
                print(number)
            print()
            found = True

    # Search by phone number
    for name, numbers in phone_book.items():
        for number in numbers:
            if search_term in number:
                print(f"Contact: {name}")
                print(f"Phone Number: {number}")
                print()
                found = True

    if not found:
        print("No contacts found.")


def main():
    phone_book = load_phone_book()

    while True:
        print("\n\nPhone Book Menu :\n")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. Exit\n")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact(phone_book)
        elif choice == '2':
            delete_contact(phone_book)
        elif choice == '3':
            update_contact(phone_book)
        elif choice == '4':
            search_contact(phone_book)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

        print()


if __name__ == "__main__":
    main()