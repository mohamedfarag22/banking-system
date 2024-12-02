class Customer():
    def __init__(self, **kwrg):
        self.name = kwrg.get('name', '')
        self.number = kwrg.get('number', '')
        self.password = kwrg.get('password', '')
        self.id_cart = kwrg.get('id_cart', '')
        self.money = float(kwrg.get('money', 0))

    def create_account(self):
        print(f'Your name is {self.name}, your number is {self.number}, and your ID card is {self.id_cart}.')
        return {self.number: dict(name=self.name, password=self.password, number=self.number, id_cart=self.id_cart,
                                  money=self.money)}

    def log_in(self, data_customer, number_log, password_logs):
        if number_log in data_customer and data_customer[number_log]['password'] == password_logs:
            print('Login successful!')
            return True
        else:
            return False

    def balance(self, data_customer):
        return data_customer[self.number]['money']

    def balance_deposit(self, data_customer, deposit_money):
        current_balance = data_customer[self.number]['money']
        new_balance = current_balance + float(deposit_money)
        data_customer[self.number]['money'] = new_balance
        return new_balance

    def balance_withdraw(self, data_customer, withdraw_money):
        current_balance = data_customer[self.number]['money']
        if float(withdraw_money) > current_balance:
            print("Insufficient funds!")
            return current_balance
        new_balance = current_balance - float(withdraw_money)
        data_customer[self.number]['money'] = new_balance
        return new_balance


data_customer = {}
while True:
    choice = int(input(
        'Select the option by writing the number:\n 1 - Create account \n 2 - Log in\n 3- end program\n Provide your number: '
    ))

    if choice == 1:
        input_data = input(
            'Write your name, password, phone number, ID card, and money on the account; separate by spaces!\n')
        input_data_clean = input_data.split()  # Split by spaces and clean any extra spaces
        if len(input_data_clean) != 5:
            print("Invalid input. Please provide exactly 5 values separated by spaces.")
            continue

        name, password, number, id_cart, money = input_data_clean
        customer = Customer(name=name, password=password, number=number, id_cart=id_cart, money=money)
        new_customer = customer.create_account()
        data_customer.update(new_customer)
        print(data_customer)
        print(f"Account for {number} created successfully.")
        continue

    elif choice == 2:
        if not data_customer:  # Check if any accounts exist first
            print("No accounts found. Please create an account first.")
            continue


        while True:
            check_log = input('Write your phone number and password to log in separated by spaces!\n')
            check_log_clean = check_log.split()
            if len(check_log_clean) != 2:
                print("Invalid input. Please provide exactly 2 values: phone number and password.")
                continue

            phone_number_log, password_log = check_log_clean
            if phone_number_log in data_customer:
                customer_login = Customer(number=phone_number_log)
                if customer_login.log_in(data_customer, phone_number_log, password_log):
                    account = int(input(
                        f'Login successful! Welcome! You need:\n 1 - Deposit \n 2 - Withdraw\n 3 - Check balance\n 4 - End program\nProvide your choice: '))

                    if account == 1:
                        deposit_num = input('Enter deposit amount: ')
                        result_money_deposit = customer_login.balance_deposit(data_customer, deposit_num)
                        print(f'Your deposit of {deposit_num}$ is done!')
                        print(f'Your balance after deposit is {result_money_deposit}$!')
                        continue

                    elif account == 2:
                        withdraw_num = input('Enter withdrawal amount: ')
                        result_money_withdraw = customer_login.balance_withdraw(data_customer, withdraw_num)
                        print(f'Your withdrawal of {withdraw_num}$ is done!')
                        print(f'Your balance after withdrawal is {result_money_withdraw}$!')
                        continue

                    elif account == 3:
                        result_balance = customer_login.balance(data_customer)
                        print(f'Your balance is {result_balance}$!')
                        continue

                    elif account == 4:
                        break

                    else:
                        print('Please write a valid number (1, 2, 3, or 4)!')

                else:
                    print('Invalid login. Please try again.')
            else:
                print('Account not found. Please try again.')
            break
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break
    else:
        print('Please write a valid option (1 or 2)!')



