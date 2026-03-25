file_name = "notes.txt"
def add_note():
    with open(file_name, "a") as file:
        note = input("Enter your note: ")
        file.write(note + "\n")
def view_notes():
    try:
        with open(file_name, "r") as file:
            notes = file.readlines()
            for line in notes:
                print(line)
    except FileNotFoundError:
        print("No file found (try adding notes)")
def delete_notes():
    with open("notes.txt", "r") as file:
        notes = file.readlines()
        try:
            delete_note = input("What note do you want deleted?: ")
            notes = [note for note in notes if note.strip() != delete_note.strip()]  
            
        except ValueError:
            print("Note not found")
        with open(file_name, "w") as file:
            notes = [note if note.endswith('\n') else note + '\n' for note in notes]  
            file.writelines(notes)
choice = input("Would you like to 1) add note 2) view all notes 3) delete note: ")
if choice == "1":
    add_note()
    choice = input("Would you like to 1) add note 2) view all notes 3) delete note: ")
    
elif choice == "2":
    view_notes()
    choice = input("Would you like to 1) add note 2) view all notes 3) delete note: ")
elif choice == "3":
    delete_notes()
    choice = input("Would you like to 1) add note 2) view all notes 3) delete note: ")
   
else:
    print("okay goodbye!")