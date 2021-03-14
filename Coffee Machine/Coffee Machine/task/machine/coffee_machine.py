# Global variables
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


# Display number of supplies
def supplies():
    print("\n")
    print("The coffee machine has:")
    print("{} of water".format(water))
    print("{} of milk".format(milk))
    print("{} of coffee beans".format(coffee_beans))
    print("{} of disposable cups".format(disposable_cups))
    print("{} of money".format(money))
    print("\n")


def purchase(water_used, milk_used, beans_used, money_given):
    global water
    global milk
    global coffee_beans
    global disposable_cups
    global money

    print("I have enough resources, making you a coffee!")

    water -= water_used
    milk -= milk_used
    coffee_beans -= beans_used
    disposable_cups -= 1
    money += money_given


def current_supplies(water_used, milk_used, beans_used, money_given):
    global water
    global milk
    global coffee_beans
    global disposable_cups

    if water_used > water:
        print("Sorry, not enough water!")
    elif milk_used > milk:
        print("Sorry, not enough milk!")
    elif beans_used > coffee_beans:
        print("Sorry, not enough coffee beans!")
    elif disposable_cups == 0:
        print("Sorry, not enough disposable cups!")
    else:
        purchase(water_used, milk_used, beans_used, money_given)


while True:
    option = input("Write action (buy, fill, take, remaining, exit):")

    # Option to "buy" coffee
    if option == "buy":
        coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino (or enter 'back' to return to main menu):")

        # espresso
        if coffee == "1":
            water_needed = 250
            milk_needed = 0
            beans_needed = 16
            money_needed = 4

            current_supplies(water_needed, milk_needed, beans_needed, money_needed)

        # latte
        elif coffee == "2":
            water_needed = 350
            milk_needed = 75
            beans_needed = 20
            money_needed = 7

            current_supplies(water_needed, milk_needed, beans_needed, money_needed)

        # cappuccino
        elif coffee == "3":
            water_needed = 200
            milk_needed = 100
            beans_needed = 12
            money_needed = 6

            current_supplies(water_needed, milk_needed, beans_needed, money_needed)

        elif coffee == "back":
            continue

    # Option to "fill" supplies
    elif option == "fill":
        water += int(input("Write how many ml of water do you want to add:"))
        milk += int(input("Write how many ml of milk do you want to add:"))
        coffee_beans += int(input("Write how many grams of coffee beans do you want to add:"))
        disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    # Option to "take" money
    elif option == "take":
        print("I gave you ${}".format(money))
        money -= money

    # Option to print current resources
    elif option == "remaining":
        supplies()

    elif option == "exit":
        break
