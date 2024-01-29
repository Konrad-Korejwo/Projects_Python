import os

coffee = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 2
    },
}

report = {
        "ingredients": {
            "water": 1000,
            "coffee": 100,
            "milk": 500,
        },
        "cost": 0
    }
switched_on = True

def money(cost, coins):
    if cost > coins:
        print("You don't have enough. Please take your money. ")
        switched_on = False
        return switched_on
    else:
        print(f"Please take your change ({coins-cost})$. The coffee is made. Thank you! :)")

def if_continue(decision):
    switched_on = True
    while decision == False:
        if_continue = input("Do you want to continue? T or N\n").lower()
        if if_continue == "t":
            os.system('cls')
            decision = True
        elif if_continue == "n":
            switched_on = False
            decision = True
            print("Good Bye! :)")
        else:
            decision = False
            print("You typed wrong letter.\n")
    return switched_on

while switched_on==True:
    choice = input("Hello! What coffee do you want? Type:\nEspresso\nLatte\nCappuccino\n").lower()
    if choice == "magazine":
        print(f"Money: {report["cost"]}$\nWater: {report["ingredients"]["water"]}L\nCoffee: {report["ingredients"]["coffee"]}g\nMilk: {report["ingredients"]["milk"]}L")
    elif choice == "restart":
        report["cost"] = 0
        report["ingredients"]["water"] = 1000
        report["ingredients"]["coffee"] = 100
        report["ingredients"]["milk"] = 500
        print("All is restarted succesfully. ")
    elif choice != "espresso" and choice != "latte" and choice != "cappuccino":
        print("You typed wrong number! Please try again.\n")
    else:
        pennies = int(input("How much pennies(1) do you have?: "))
        nickels = int(input("How much nickels(5) do you have? "))
        dimes = int(input("How much dimes(10) do you have?: "))
        quarters = int(input("How much quarters(25) do you have?: "))
        coins = pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25
        print(f"You have insert {coins}$. ")
        if coffee[choice]["cost"]<coins:
            report["cost"] += coffee[choice]["cost"]
            report["ingredients"]["water"] -= coffee[choice]["ingredients"]["water"]
            report["ingredients"]["coffee"] -= coffee[choice]["ingredients"]["coffee"]
            report["ingredients"]["milk"] -= coffee[choice]["ingredients"]["milk"]
        money(coffee[choice]["cost"],coins)
    print("\n")

    decision = False
    switched_on = if_continue(decision)

