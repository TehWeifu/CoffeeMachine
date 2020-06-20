class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 400
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.menu()

    def menu(self):
        menu_option = input("Write action (buy, fill, take, remaining, exit): ")
        while menu_option != "exit":
            if menu_option == "buy":
                self.buy()
            elif menu_option == "fill":
                self.fill()
            elif menu_option == "take":
                self.take()
            else:
                self.remaining()
            menu_option = input("Write action (buy, fill, take, remaining, exit): ")

    def buy(self):
        buy_menu = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if buy_menu != "back":
            if buy_menu == '1':
                if self.water >= 250:
                    if self.coffee_beans >= 16:
                        if self.cups >= 1:
                            print("I have enough resources, making you a coffee!")
                            self.water -= 250
                            self.coffee_beans -= 16
                            self.money += 4
                            self.cups -= 1
                        else:
                            print("Sorry, not enough cups")
                    else:
                        print("Sorry, not enough coffee beans")
                else:
                    print("Sorry, not enough water")

            elif buy_menu == '2':
                if self.water >= 350:
                    if self.milk >= 75:
                        if self.coffee_beans >= 16:
                            if self.cups >= 1:
                                print("I have enough resources, making you a coffee!")
                                self.water -= 350
                                self.milk -= 75
                                self.coffee_beans -= 20
                                self.money += 7
                                self.cups -= 1
                            else:
                                print("Sorry, not enough cups")
                        else:
                            print("Sorry, not enough coffee beans")
                    else:
                        print("Sorry, not enough milk")
                else:
                    print("Sorry, not enough water")
            else:
                if self.water >= 200:
                    if self.milk >= 100:
                        if self.coffee_beans >= 12:
                            if self.cups >= 1:
                                print("I have enough resources, making you a coffee!")
                                self.water -= 200
                                self.milk -= 100
                                self.coffee_beans -= 12
                                self.money += 6
                                self.cups -= 1
                            else:
                                print("Sorry, not enough cups")
                        else:
                            print("Sorry, not enough coffee beans")
                    else:
                        print("Sorry, not enough milk")
                else:
                    print("Sorry, not enough water")

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"
                           ))
        self.milk += int(input("Write how many ml of milk do you want to add:"
                           ))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add:"
                           ))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"
                       ))

    def take(self):
        print("I gave you $", self.money)
        self.money = 0

    def remaining(self):
        print("The coffee machine has")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")


test = CoffeeMachine()
