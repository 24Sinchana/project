Menu={
   "latte":{
      "ingredients":{
         "water":200,
         "milk": 150,
         "coffee":24,
      },
       "cost":150
   },
   "espresso":{
      "ingredients":{
         "water":50,
         "coffee":18,
      },
      "cost":100,
   },
   "cappuccino":{
      "ingredients":{
         "water":250,
         "milk":100,
         "coffee":24,
      },
      "cost": 200,
   }
}
profit=0
resources={
  "water": 500,
  "milk": 200,
  "coffee": 100,
}

#checking if the resources are enough in the ingredients 
def check_resources(order_ingredients):
   for item in order_ingredients:#water #milk
      if order_ingredients[item]>resources[item]:
         print(f"sorry there is no sufficient {item}")
         return False
   return True

#if ingredients are availble then insert coins
def process_coins():
   print("please insert coins")
   total=0
   coins_five=int(input("How many 5Rs coins:"))
   coins_ten=int(input("How many 10Rs coins:"))
   coins_twenty=int(input("How many 20Rs coins:"))
   total=coins_five*5 + coins_ten*10 + coins_twenty*20
   return total

#checking if payment is successful or not
def  is_payment_successful(money_recieved,coffee_cost):
   if money_recieved>=coffee_cost:
      global profit 
      profit += coffee_cost
      change=money_recieved-coffee_cost  #if too much money is inserted then give the change
      print(f"here is your Rs.{change} in change")
      return True
   else:
      print("sorry that's not enough money.Money refunded")
      return False

def make_coffee(coffee_name,coffee_ingredients):
   for item in coffee_ingredients:
      resources[item] -= coffee_ingredients[item]
   print(f"here is your {coffee_name} ☕.enjoy!")

is_on=True
while is_on:
   choice=input("what do u want to have? (latte/espresso/cappuccino): ")
   if choice=="off":
    is_on=False
   elif choice=="report":
      print(f"water={resources['water']}ml")
      print(f"milk={resources['milk']}ml")
      print(f"coffee={resources['coffee']}g")
      print(f"money=Rs.{profit}")
   else:
      coffee_type=Menu[choice]
      print(coffee_type)
      if check_resources(coffee_type['ingredients']):
         payment=process_coins()
         if is_payment_successful(payment,coffee_type['cost']): #payment done and cost of the coffee type chosen
            make_coffee(choice,coffee_type['ingredients'])   #if payment is successful then make coffee
        

      

