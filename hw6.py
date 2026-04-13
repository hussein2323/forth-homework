import simple_math

while True:
    print("\n--- MENU ---")
    print("1. Factorial")
    print("2. Check Prime")
    print("3. Check Positive/Negative")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        n = int(input("Enter number: "))
        print("Factorial:", simple_math.factorial(n))

    elif choice == "2":
        n = int(input("Enter number: "))
        if simple_math.is_prime(n):
            print("Prime number")
        else:
            print("Not prime")

    elif choice == "3":
        n = int(input("Enter number: "))
        print(simple_math.check_number(n))

    elif choice == "4":
        break

    else:
        print("Invalid choice")