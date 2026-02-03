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

    