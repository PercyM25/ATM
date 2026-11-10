balance = 1000.00
attempts = 3
unlocked = False

# PIN check: 3 attempts before the card locks
while attempts > 0:
    pin = input("Enter PIN: ")
    if pin == "4545":
        unlocked = True
        break
    attempts -= 1
    print(f"Wrong PIN. {attempts} attempt(s) left.")

if not unlocked:
    print("Access Denied!.")
else:
    while True:
        print("\n1. Balance  2. Deposit  3. Withdraw  4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            print(f"Balance: R{balance:.2f}")

        elif choice == "2":
            print(f"Current balance: R{balance:.2f}")
            amount = float(input("Deposit amount: R"))
            balance += amount
            print(f"New balance: R{balance:.2f}")

        elif choice == "3":
            amount = float(input("Withdraw amount: R"))
            if amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                print(f"New balance: R{balance:.2f}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.Please choose an option from 1 to 4. Thank you.")