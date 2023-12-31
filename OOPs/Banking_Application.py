class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0 
        self.menu()

    def menu(self):
        user_input=input("""
        Hi! How can i help you
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit      
        """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.change_pin()
        elif user_input=="3":
            self.check_balance()
            pass
        elif user_input=="4":
            # withdraw
            pass
        else:
            exit()
    
    def create_pin(self):
        user_pin=int(input('enter your pin'))
        self.pin=user_pin
        
        user_balance=int(input('enter your balance'))
        self.balance=user_balance
        
        print('Pin created successfully')
        self.menu()
        
    def change_pin(self):
        old_pin=int(input('enter old pin'))
        if old_pin==self.pin:
            #let him change the pin
            new_pin=input('Let him change the pin')
            self.pin=new_pin
            print("pin chnaged successfully")
            self.menu()
        else:
            print('try again')
            self.menu()
    
    def check_balance(self):
        user_pin=int(input('enter your pin'))
        if user_pin==self.pin:
            print("Your balance is {}".format(self.balance))
        else:
            print('try again')
            self.menu()
        
obj=Atm()
        
        
        
        