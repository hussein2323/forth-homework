import edit_string

while True:
    print("\n--- MENU ---")
    print("1. Reverse string")
    print("2. String length")
    print("3. Delete spaces")
    print("4. Check string")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        st= input("Enter string: ")
        print(edit_string.reverse_string(s))

    elif choice == "2":
        st= input("Enter string: ")
        print(edit_string.string_length(s))

    elif choice == "3":
        s = input("Enter string: ")
        print(edit_string.delete_spaces(s))

    elif choice == "4":
        s = input("Enter string: ")
        print(edit_string.check_string(s))

    elif choice == "5":
        break

    else:
        print("Invalid choice")