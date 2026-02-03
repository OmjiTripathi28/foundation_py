class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0 
        self.menu()

    def menu(self):
        user_input = input(
            """
            1. create pin
            2. change pin
            3. check balance
            4. withdraw 
            5. exit"""
        )

        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.change_pin()
        elif user_input == 3:
            self.check_balance()
        elif user_input == 4:
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        pin = input("enter your pin : ")
        self.pin = pin
        balance = int(input("enter your balance : "))
        self.balance = balance
        print("PIN CREATED SUCCESSFULLY !!")

    def change_pin(self):
        old_pin = input("enter your old pin : ")
        if old_pin == self.pin :
            new_pin = input("enter your new pin : ")
            self.pin = new_pin 
        else:
            print("wrong old pin")
            self.menu()

    def check_balance(self):
        pin = input("enter your pin : ")
        if pin == self.pin :
            print(f"your account balance is {self.balance}")
        else:
            print("wrong pin")
            self.menu()

    def withdraw(self):
        amount = input("enter the amount you wanna withdraw : ")
        if amount<= self.balance :
            print(f"you ramaining amount is {self.balance - amount}")
        else:
            print("invalid amount")
            self.menu()
            