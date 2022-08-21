class CoffeeMachine:
    def __init__(self, money, water, milk, coffee, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups

    def remaining(self):
        print("The coffee machine has:")
        print("{} ml of water".format(self.water))
        print("{} ml of milk".format(self.milk))
        print("{} g of coffee beans".format(self.coffee))
        print("{} disposable cups".format(self.cups))
        print("${} of money\n".format(self.money))

    def buy(self):
        choice = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu\n"))
        if choice == 'back':
            return
        else:
            cups_need = 1
            if choice == '1':
                water_need = 250
                milk_need = 0
                coffee_need = 16
                money_add = 4
            elif choice == '2':
                water_need = 350
                milk_need = 75
                coffee_need = 20
                money_add = 7
            elif choice == '3':
                water_need = 200
                milk_need = 100
                coffee_need = 12
                money_add = 6
            if self.water >= water_need and self.coffee >= coffee_need and self.cups >= cups_need and self.milk >= milk_need:
                print("I have enough resources, making you a coffee!\n")
                self.water -= water_need
                self.milk -= milk_need
                self.coffee -= coffee_need
                self.money += money_add
                self.cups -= cups_need
            else:
                if self.water < water_need:
                    missing = 'water'
                elif self.milk < milk_need:
                    missing = 'milk'
                elif self.coffee < coffee_need:
                    missing = 'coffee'
                elif self.cups < cups_need:
                    missing = 'cups'
                print("Sorry, not enough {}!\n".format(missing))

    def fill(self):
        self.water += int(input("Write how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.coffee += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.cups += int(input("Write how many disposable cups you want to add:\n"))

    def take(self):
        print("I gave you ${}\n".format(self.money))
        self.money = 0

    def start(self):
        stop = 0
        while stop == 0:
            request = input("Write action (buy, fill, take, remaining, exit):\n")
            if request == "buy":
                machine.buy()
            elif request == "fill":
                machine.fill()
            elif request == "take":
                machine.take()
            elif request == "remaining":
                machine.remaining()
            elif request == "exit":
                stop = 1


start_money = 550
start_water = 400
start_milk = 540
start_coffee = 120
start_cups = 9

machine = CoffeeMachine(start_money, start_water, start_milk, start_coffee, start_cups)
machine.start()





