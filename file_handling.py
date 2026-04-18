try:
    note = input("Enter a short note: ")
    
    with open("notes.txt", "w") as file:
        file.write(note)
    
    print("\nNote saved successfully!")

    
    print("\nReading file content:")
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)

    
    new_note = input("\nEnter another note: ")
    
    with open("notes.txt", "a") as file:
        file.write("\n" + new_note)

    
    print("\nUpdated file content:")
    with open("notes.txt", "r") as file:
        updated_content = file.read()
        print(updated_content)


except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print("An error occurred:", e)