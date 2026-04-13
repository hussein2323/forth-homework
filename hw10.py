import shapes

while True:
    print("\n--- MENU ---")
    print("1. Circle Area")
    print("2. Circle Circumference")
    print("3. Square Area")
    print("4. Square Circumference")
    print("5. Rectangle Area")
    print("6. Rectangle Circumference")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        r = float(input("Enter radius: "))
        print(shapes.circle_area(r))

    elif choice == "2":
        r = float(input("Enter radius: "))
        print(shapes.circle_circumference(r))

    elif choice == "3":
        a = float(input("Enter side: "))
        print(shapes.square_area(a))

    elif choice == "4":
        a = float(input("Enter side: "))
        print(shapes.square_circumference(a))

    elif choice == "5":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print(shapes.rectangle_area(l, w))

    elif choice == "6":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print(shapes.rectangle_circumference(l, w))

    elif choice == "7":
        break

    else:
        print("Invalid choice")