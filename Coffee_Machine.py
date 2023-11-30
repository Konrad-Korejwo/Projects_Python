#This code is a simulator of the coffee machine. It is a base of the back-end. The project does not contain calculating the coins
#used to give the change and machine technology like pouring the coffee.

coffee ={
  "espresso": {
    "ingredients":{
      "water": 50,
      "coffee": 18,
      "milk":0,
    },
  "cost": 1.5,
    
  },
  "latte":{
    "ingredients": {
      "water": 200,
      "coffee": 24,
      "milk": 150,
    },
  "cost": 2.5,
  },
  "cappuccino": {
    "ingredients":{
      "water": 250,
      "coffee": 24,
      "milk": 100,
    },
  "cost": 3,
  },
  "report": {
    "ingredients":{
      "water": 300,
      "coffee": 100,
      "milk": 200,
    },
  "cost": 0,
  }
}
decision = 1

def choice():

  c_milk = coffee[decision]['ingredients']['milk']
  c_water = coffee[decision]['ingredients']['water']
  c_coffee = coffee[decision]['ingredients']['coffee']
  c_money = coffee[decision]['cost']
  coffee_ing=[c_milk, c_water, c_coffee,c_money]
  return coffee_ing
  
    

def sufficient(coffee_ing, magazine_res):
  if coffee_ing[0] <= magazine_res[0] and coffee_ing[1] <= magazine_res[1] and coffee_ing[2] <= magazine_res[2]:
    return True
  else:
    return False

def money_calculation():
  money = 0
  money += int(input("\nHow many pennies(1) do you have?: "))*0.01
  money += int(input("How many nickels(5) do you have?: "))*0.05
  money += int(input("How many dimes(10) do you have?: "))*0.10
  money += int(input("How many quarters(25) do you have?: "))*0.25
  return money
  

while decision!="bye":
  
  decision = input("\nWhat coffee would you like, espresso / latte / cappuccino?: \n")
  if decision == "espresso" or decision == "latte" or decision == "cappuccino":
    coffee_ing = choice() #coffe_ing
    magazine_res = [coffee['report']['ingredients']['milk'], coffee['report']['ingredients']['water'], coffee['report']['ingredients']['coffee']]
    if sufficient(coffee_ing,magazine_res) == True:
      money = money_calculation()
      money_rest = coffee_ing[3]
      if money>=money_rest:
        print(f"\nYou have {money}$. Take your change equal to {round(money-money_rest,2)}. Please take your coffee! :) \n")
        coffee['report']['ingredients']['milk'] -= coffee_ing[0]
        coffee['report']['ingredients']['water'] -= coffee_ing[1]
        coffee['report']['ingredients']['coffee'] -= coffee_ing[2]
      else:
        print("You don't have enough money.\n")

    else:
      print("There are too few resources! \n")
    
  elif decision == "report":
    print(coffee['report'])
  elif decision == "off":
    print("\nThank you and good bye! :)")
    decision = "bye"
  elif decision == "fill":
    coffee['report']['ingredients']['milk'] = 200
    coffee['report']['ingredients']['water'] = 300
    coffee['report']['ingredients']['coffee'] = 100
    print("\nAll sources filled, thank you! :) ")
  else:
    print("You typed wrong word. Please try again. \n")
