lineup = [("Code Play",  "Indie", 30), ("The Pythonistas", "Rock", 45), ("Syntax Error", "Metal", 60)]
print("\n---Py-Fest 2026 Stage Manager ---")
print("1. View Lineup and Total Time")
print("2. Add New Band")
print("3. Move First Band to End(Late Arrival)")
print("4. Remove a band name")
print("5. Move Band to Specific Position")
print("6. Exit")
choice = input("Select an opption (1-6): ")
if choice == "1":
    print("\n--- Current Lineup ---")
    print(lineup)

