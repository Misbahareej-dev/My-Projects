balance = 5000
pin = "1234"

print("==============================")
print("        ATM SIMULATOR")
print("==============================")

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:

    while True:
        print("\n==============================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your balance is:", balance, "PKR")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance += amount
                print("Money deposited successfully!")
                print("New balance:", balance, "PKR")
            else:
                print("Invalid amount.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining balance:", balance, "PKR")

        elif choice == "4":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN!")
    print("Access denied.")