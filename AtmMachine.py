class Atm:

    def __init__(self):
        self.pin = "1234"
        self.balance = 10000
        print("Welcome to ATM Machine")

    def menu(self):
        user_input = input("""
Hi, How can I help you?

1. Press 1 to Create PIN
2. Press 2 to Change PIN
3. Press 3 to Check Balance
4. Press 4 to Withdraw Money
5. Press 5 to Exit

Enter your choice: 
""")

        if user_input == "1":
            self.create_pin()

        elif user_input == "2":
            self.change_pin()

        elif user_input == "3":
            self.check_balance()

        elif user_input == "4":
            self.withdraw_money()

        elif user_input == "5":
            print("Thank You for using ATM!")
            return

        else:
            print("Invalid Choice!")
            self.menu()

    def create_pin(self):
        self.pin = input("Enter your new PIN: ")
        self.balance = int(input("Enter initial balance: "))
        print("PIN created successfully!")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter your old PIN: ")

        if old_pin == self.pin:
            self.pin = input("Enter your new PIN: ")
            print("PIN changed successfully!")
        else:
            print("Incorrect PIN!")

        self.menu()

    def check_balance(self):
        user_pin = input("Enter your PIN: ")

        if user_pin == self.pin:
            print("Your balance is:", self.balance)
        else:
            print("Incorrect PIN!")

        self.menu()

    def withdraw_money(self):
        user_pin = input("Enter your PIN: ")

        if user_pin == self.pin:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful!")
                print("Remaining balance:", self.balance)
            else:
                print("Insufficient balance!")
        else:
            print("Incorrect PIN!")

        self.menu()


# Create ATM object
obj = Atm()
obj.menu()