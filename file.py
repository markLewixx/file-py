# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Line 1: This is a string.\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: Another string with numbers: 3.14, 42\n")
        print("File 'my_file.txt' created and written successfully.")

except Exception as e:
    print("An error occurred while creating and writing to the file:", e)

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("\nContents of 'my_file.txt':")
        print(file.read())

except Exception as e:
    print("An error occurred while reading the file:", e)

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Line 4: Appended line 1.\n")
        file.write("Line 5: Appended line 2.\n")
        file.write("Line 6: Appended line 3.\n")
        print("\nThree lines appended to 'my_file.txt'.")

except Exception as e:
    print("An error occurred while appending to the file:", e)

finally:
    print("\nEnd of script.")
