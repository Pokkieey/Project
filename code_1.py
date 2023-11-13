bank_data = {
    "Bangkok Bank (BBL)": {
        'Savings Account': {'Interest Rate': 0.50},
        'Fixed Deposit Accounts': {
            '3 months': 1.20,
            '6 months': 1.25,
            '12 months': 1.60,
            '24 months': 2.00
        },
        "Loan with collateral": 12,
        "Loan without collateral": 22,
    },
    "Kasikorn (KBank)": {
        'Savings Account': {'Interest Rate': 0.30},
        'Fixed Deposit Accounts': {
            '3 months': 1.07,
            '6 months': 1.23,
            '12 months': 1.65,
            '24 months': 2.20
        },
        "Loan with collateral": 12.5,
        "Loan without collateral": 18,
    },
    "Siam Commercial Bank (SCB)": {
        'Savings Account': {'Interest Rate': 0.30},
        'Fixed Deposit Accounts': {
            '3 months': 1.10,
            '6 months': 1.25,
            '12 months': 1.70,
            '24 months': 2.25
        },
        "Loan with collateral": 11,
        "Loan without collateral": 25,
    },
    "Krungsri (BAY)": {
        'Savings Account': {'Interest Rate': 0.30},
        'Fixed Deposit Accounts': {
            '3 months': 1.10,
            '6 months': 1.25,
            '12 months': 1.70,
            '24 months': 2.10
        },
        "Loan with collateral": 11.5,
        "Loan without collateral": 24,
    },
    "Krungthai (KTB)": {
        'Savings Account': {'Interest Rate': 0.30},
        'Fixed Deposit Accounts': {
            '3 months': 1.17,
            '6 months': 1.25,
            '12 months': 1.70,
            '24 months': 2.40
        },
        "Loan with collateral": 10.7,
        "Loan without collateral": 20,
    },
}
def calculate_total_loan_amount(loan_amount, interest_rate):
    return loan_amount * (1 + interest_rate / 100)

def find_cheapest_bank(loan_amount, collateral, bank_data):
    cheapest_bank = None
    cheapest_total_amount = float('inf')

    for bank_name, bank_info in bank_data.items():
        interest_rate = bank_info["Loan with collateral"] if collateral else bank_info["Loan without collateral"]
        total_amount = calculate_total_loan_amount(loan_amount, interest_rate)

        if total_amount < cheapest_total_amount:
            cheapest_total_amount = total_amount
            cheapest_bank = bank_name

    return cheapest_bank, cheapest_total_amount

def find_best_bank(selected_duration, bank_data):
    # Find the bank with the highest interest rate for the selected duration
    max_interest_bank = None
    max_interest_rate = 0

    for bank_name, bank in bank_data.items():
        interest_rate = bank['Fixed Deposit Accounts'].get(selected_duration, 0)
        if interest_rate > max_interest_rate:
            max_interest_rate = interest_rate
            max_interest_bank = bank_name

    return max_interest_bank, max_interest_rate

def calculate_remaining_amount(principal, interest_rate, time):
    # Compound interest formula
    remaining_amount = 0
    for i in range(1,time+1):
        remaining_amount += principal * ((1 + interest_rate / 100) ** time)
    return remaining_amount

def calculate_savings_plan(goal_amount, income, expenses, selected_duration, bank_data):
    remaining_amount = income - expenses

    if remaining_amount <= 0:
        print("You have no money left to save. Adjust your expenses or consider increasing your income.")
        return None  # Return None if there's an issue

    selected_bank, interest_rate = find_best_bank(selected_duration, bank_data)

    if selected_bank is None or interest_rate == 0:
        print(f"No suitable bank found for the selected duration ({selected_duration}).")
        return None  # Return None if there's an issue

    remaining_amount_after_duration = calculate_remaining_amount(remaining_amount, interest_rate, int(selected_duration.split()[0]))
   
    monthly_savings = goal_amount / int(selected_duration.split()[0])

    result_text = (
        f"In order to have ${goal_amount}, it is recommended to save ${monthly_savings:.2f} per month "
        f"with an interest rate of {interest_rate}% at {selected_bank}. "
        f"If you save ${remaining_amount:.2f} per month for {selected_duration}, "
        f"you will have ${remaining_amount_after_duration:.2f} in your bank account."
    )
    return result_text

if __name__ == "__main__":
    while True:
        print("Choose an option:")
        print("1. Calculate Savings Plan")
        print("2. Find Cheapest Loan")

        option_choice = input("Enter the number corresponding to your choice: ")

        if option_choice == '1':
            goal_amount = float(input("What is your savings goal? "))
            income = float(input("Enter your monthly income: "))
            expenses = float(input("Enter your monthly expenses: "))

            print("\nWould you like to cash out during the time?")
            cash_out_choice = input("Enter 'y' for yes or 'n' for no: ").lower()

            if cash_out_choice == 'y':
                result = calculate_savings_plan(goal_amount, income, expenses, None, bank_data, cash_out=True)
            elif cash_out_choice == 'n':
                print("\nSelect a saving duration:")
                print("1. 3 months")
                print("2. 6 months")
                print("3. 12 months")
                print("4. 24 months")

                duration_choice = input("Enter the number corresponding to your choice: ")
                duration_mapping = {'1': '3 months', '2': '6 months', '3': '12 months', '4': '24 months'}
                selected_duration = duration_mapping.get(duration_choice)

                if not selected_duration:
                    print("Invalid choice. Please enter a valid number.")
                    continue

                result = calculate_savings_plan(goal_amount, income, expenses, selected_duration, bank_data)
            print(result)

        elif option_choice == '2':
            loan_amount = float(input("Enter the desired loan amount: "))
            collateral = input("Do you have collateral? (yes/no): ").lower() == "yes"

            cheapest_bank, cheapest_total_amount = find_cheapest_bank(loan_amount, collateral, bank_data)

            print(f"The cheapest bank for a loan of {loan_amount} with {'collateral' if collateral else 'no collateral'} is {cheapest_bank} with a total amount of {cheapest_total_amount:.2f}.")

        else:
            print("Invalid choice. Please enter either '1' or '2'.")

        # Ask the user if they want to repeat
        repeat = input("Do you want to perform another calculation? (y/n): ").lower()
        if repeat != 'y':
            break
