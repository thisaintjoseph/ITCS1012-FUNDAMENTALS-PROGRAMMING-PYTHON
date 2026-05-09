import os


def display_menu():
    print("\n--- Dreams File Manager ---")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")

def read_messages():
    try:
        with open("dreams.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("\n[The file is currently empty]")
            else:
                print("\n--- Inspiring Messages ---")
                print(content)
    except FileNotFoundError:
        print("\n[dreams.txt not found. Please make sure the file exists.]")

def add_message():
    message = input("\nEnter your inspiring message: ")
    with open("dreams.txt", "a") as file:
        file.write(message + "\n")
    print("[Message added successfully!]")

def rewrite_file():
    confirm = input("\nAre you sure you want to overwrite the file? (yes/no): ").lower()
    if confirm == "yes":
        new_content = input("Enter the new inspiring messages: \n")
        with open("dreams.txt", "w") as file:
            file.write(new_content + "\n")
        print("[File has been overwritten!]")
    else:
        print("[Rewriting has been cancelled]")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            read_messages()
        elif choice == "2":
            add_message()
        elif choice == "3":
            rewrite_file()
        elif choice == "4":
            print("\nExiting Dreams File Manager. Goodbye!")
            break
        else:
            print("[Invalid choice. Please try again.]")

if __name__ == "__main__":
    main()
