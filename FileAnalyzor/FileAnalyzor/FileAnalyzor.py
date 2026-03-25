import glob

# Get all .txt files in the directory

files = glob.glob("server_dump/*.txt") 
ok = 0
warn = 0
error = 0
ok_names = []
warn_names = []
error_names = []
for i in files:
    file = open(i, "r")
    content = file.read()
    sat_1 = "OK"
    sat_2 = "WARN"
    sat_3 = "ERROR"
    if sat_1 in content:
        ok += 1
        ok_names.append(i)
    elif sat_2 in content:
        warn += 1
        warn_names.append(i)
    elif sat_3 in content:
        error += 1
        error_names.append(i)
    file.close
print(f"OK: {ok}")
print(f"WARN: {warn}")
print(f"ERROR: {error}")

choice = input("Would you like to print the file names: ")

if choice == "yes":
    choice_two = input("What file type would you like to print(OK,WARN,ERROR): ")
    if choice_two == "OK":
        print(f"Okay file names:{ok_names}")
    elif choice_two == "WARN":
        print(f"warn file names: {warn_names}")
    elif choice_two == "ERROR":
        print(f"error file names: {error_names}")
    else:
        print("type not found")
else:
    print("Okay Goodbye!")