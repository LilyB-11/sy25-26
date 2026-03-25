import datetime
v1 = "mydiary.txt"
v2 = input("Select 1-4 (1. Write, 2. Read, 3. Clear, 4. Exit):")
v4 = datetime.datetime.now().strftime("%Y-%m-%d- %H:%M:%S")
while True:
    if v2 == '1':
        v3 = open(v1, "a")
        v5 = input("Entry: ")
        v6 = v3.write(f"[{v4}]{v5}/n")
        v3.close()
        v2 = input("Select 1-4 (1. Write, 2. Read, 3. Clear, 4. Exit):")
    elif v2 == '2':
        v3 = open(v1, "r")
        v7 = v3.readlines()
        for v8 in v7: print(v8.strip())
        v3.close()
        v2 = input("Select 1-4 (1. Write, 2. Read, 3. Clear, 4. Exit):")
    elif v2 == '3':
        v3 = open(v1, "w")
        v2 = input("Select 1-4 (1. Write, 2. Read, 3. Clear, 4. Exit):")
        v3.close()
    elif v2 == '4':
        break
    else:
        print("Error")