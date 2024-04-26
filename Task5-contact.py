class Contact:
    def _init_(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def _init_(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            for index, contact in enumerate(self.contacts):
                print(f"{index + 1}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found matching the search term.")
        else:
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

def main():
    contact_book = ContactBook()

    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter search term (name or phone number): ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            index = int(input("Enter index of contact to update: ")) - 1
            if index < 0 or index >= len(contact_book.contacts):
                print("Invalid index.")
            else:
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                new_contact = Contact(name, phone, email, address)
                contact_book.update_contact(index, new_contact)
                print("Contact updated successfully.")
        elif choice == '5':
            index = int(input("Enter index of contact to delete: ")) - 1
            if index < 0 or index >= len(contact_book.contacts):
                print("Invalid index.")
            else:
                contact_book.delete_contact(index)
                print("Contact deleted successfully.")
        elif choice == '6':
            print("Exiting contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()