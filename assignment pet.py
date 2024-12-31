import random
def main():
    pet_name=input("enter the pet name")
    pet={
    "name":pet_name,
    "hunger":50,
    "happiness" :50,
    "energy":50,

    }
    print("/npet created")
    print(f"name{pet['name']}")
    print(f"hunger{pet['hunger']}")
    print(f"happiness{pet['happiness']}")
    print(f"energy{pet['happiness']}")

def feed():
     hunger=min(hunger-10,100)
     print(f"{name}is feed hunger level increse{feed}")

def play():
         global happiness
         happiness=min(happiness+10,100)
         energy=max(energy-10,0)
         print(f"{happiness}increase happiness level{energy}decrease energy level")

def rest():
            """ increase energy"""
            energy=min(energy+10,100)
            hunger=max(hunger-10,0)
            print(f"{energy}increase the energy level{hunger}decrease the hunger level")

while True:
        print("\nWhat is your pet name")
        print("1.hunger")
        print("2.happiness")
        print("3.energy")
        choice = input("Enter your choice (1/2/3) : ").strip()

        if choice == "1":
           feed()
           
        elif choice == "2":
            play()
        elif choice =="3":
            rest()
            
            break
        else:
            print("invalid chooice.please try again")

          
          


     
     


if __name__ == "__main__":
        main()