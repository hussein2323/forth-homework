import sorting

lst = []

while True:
    print("\n--- MENU ---")
    print("1. Enter list")
    print("2. Bubble Sort")
    print("3. Merge Sort")
    print("4. Quick Sort")
    print("5. Show list")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        lst = list(map(int, input("Enter numbers separated by space: ").split()))

    elif choice == "2":
        print(sorting.bubble_sort(lst.copy()))

    elif choice == "3":
        print(sorting.merge_sort(lst.copy()))

    elif choice == "4":
        print(sorting.quick_sort(lst.copy()))

    elif choice == "5":
        print(lst)

    elif choice == "6":
        break

    else:
        print("Invalid choice")