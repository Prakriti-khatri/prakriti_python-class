batteries=[50,30,4,45,12,18,30]
minimum_battery_power=20
usable_battery_power=0
usable_battery_count=0
for battery in batteries:
    if battery>minimum_battery_power:
        usable_battery_power+=battery
        usable_battery_count=usable_battery_count+1
        print(f"there are{usable_battery_count}batteries which can be used to generate{usable_battery_power}")

#alien message game
alien_message="uoy era woh namuh ih"
print(f"""
alien message={alien_message}
now, human message={alien_message[::-1]} """)#reverse string

available_food=[
    "apple",
    "banana",
    "chocolate",
   "mango",
   "kiwi",
   "water",
   "breads",
   "cupcake",
   "pizza",
   "momo",
]
available_crews=3
each_crew_food=len(available_food)//available_crews
remaining_food_count=len(available_food)%available_crews
print(f"each_crew_get{each_crew_food}food and remaining food count={remaining_food_count}")

#functions


def setup_mission():
    print("setting up for the mission....")
    available_food=[
    "apple",
    "banana",
    "chocolate",
   "mango",
   "kiwi",
   "water",
   "breads",
   "cupcake",
   "pizza",
   "momo",
]
    available_crews=int(input("enter available crew"))
    print("setup completed....")
    return available_crews, available_food
 

def alien_attack_game():

    print("welcome to alien attack game")
    print("starting mission.....")
    
    crews_number,foods=setup_mission()
    print(f"you have {crews_number}astronuts and food available={foods}")
   
    print("WELCOME TO THE MARS!!!")
    print("your battery is dead please charge the battery")


   
   
   
    print("mission completed")

alien_attack_game()



