class Bank:
    def __init__(self, name, interest_rate, max_loan_amount, max_loan_term):
        self.name = name
        self.interest_rate = interest_rate
        self.max_loan_amount = max_loan_amount
        self.max_loan_term = max_loan_term

    def calculate_loan_payment(self, loan_amount, loan_term):
        interest = loan_amount * self.interest_rate * loan_term
        total_payment = loan_amount + interest
        monthly_payment = total_payment / loan_term
        return total_payment, monthly_payment

def calculate_loan(loan_amount, loan_term):
    banks = [
        Bank("Bank A", 0.05, 500000, 5),
        Bank("Bank B", 0.06, 600000, 4),
        Bank("Bank C", 0.04, 450000, 6)
    ]

    result = ""
    for bank in banks:
        if loan_amount <= bank.max_loan_amount and loan_term <= bank.max_loan_term:
            total_payment, monthly_payment = bank.calculate_loan_payment(loan_amount, loan_term)
            result += f"\nBank: {bank.name}\n"
            result += f"Interest Rate: {bank.interest_rate * 100}%\n"
            result += f"Total Payment: {total_payment:.2f} THB\n"
            result += f"Monthly Payment: {monthly_payment:.2f} THB\n"
        else:
            result += f"\nSorry, {bank.name} cannot offer a loan for the given amount and term.\n"

    return result

def calculate_savings(savings_amount, savings_type):
    if savings_type == "Saving Account":
        interest_rate = 0.02
        total_interest = savings_amount * interest_rate
        result = f"\nSavings Account Details:\n"
        result += f"Interest Rate: {interest_rate * 100}%\n"
        result += f"Total Interest Earned: {total_interest:.2f} THB\n"
    elif savings_type == "Current Deposit":
        result = "\nCurrent Deposit Details:\nNo interest is earned on current deposits.\n"
    elif savings_type == "Fixed Deposit":
        interest_rate = 0.04
        total_interest = savings_amount * interest_rate
        result = f"\nFixed Deposit Account Details:\n"
        result += f"Interest Rate: {interest_rate * 100}%\n"
        result += f"Total Interest Earned: {total_interest:.2f} THB\n"

    return result

if __name__ == "__main__":
    print("Welcome to the Loan and Savings Calculator!")

    while True:
        print("\nWhat do you want to do?")
        print("1. Loan Calculator")
        print("2. Savings Calculator")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            try:
                loan_amount = float(input("Enter the loan amount: "))
                loan_term = int(input("Enter the loan term (in years): "))
                print(calculate_loan(loan_amount, loan_term))
            except ValueError:
                print("Please enter valid numeric values for loan amount and term.")

        elif choice == "2":
            try:
                savings_amount = float(input("Enter the savings amount: "))
                savings_type = input("Enter the savings type (Saving Account/Current Deposit/Fixed Deposit): ")
                print(calculate_savings(savings_amount, savings_type))
            except ValueError:
                print("Please enter valid numeric values for savings amount.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
