class BankAccount:
    def __init__(self, customer_name, account_no, balance):
        self.customer_name = customer_name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")
        print("Current balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
        print("Current balance:", self.balance)

    def show_balance(self):
        print("Current balance:", self.balance)

name = input("Enter your name: ")
acc_no = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, acc_no, balance)

while True:
    print("\n--- MENU ---")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance Inquiry")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")