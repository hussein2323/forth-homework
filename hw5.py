import edit_list

list = []

while True:
    print("\n--- MENU ---")
    print("1. Add element")
    print("2. Delete element")
    print("3. Update element")
    print("4. Show list")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        value = input("Enter value: ")
        list = edit_list.add_element(list, value)

    elif choice == "2":
        index = int(input("Enter index to delete: "))
        list = edit_list.delete_element(list, index)

    elif choice == "3":
        index = int(input("Enter index to update: "))
        value = input("Enter new value: ")
        list = edit_list.update_element(list, index, value)

    elif choice == "4":
        print("List:", list)

    elif choice == "5":
        break

    else:
        print("Invalid choice")