inventory = {}


while True:
    print("\nOptions: [1] Add [2] Remove [3] List [4] Exit")
    choice = input("Select an option(1-4): ")
    while choice != "4":
        if choice == "1":
            name = input("Enter item name: ").strip().capitalize()
            qty = int(input(f"How many {name}'s? "))
            inventory[name] = inventory.get(name, 0) + qty
            break

        elif choice == "2":
            name = input("which item would you like to remove? ").strip().capitalize()
            print(f"removed {name} from inventory.")
            break
        elif choice == "3":
            for item, qty in inventory.items():
                print(f"- {item}: {inventory[item]}")
            break
    
       

