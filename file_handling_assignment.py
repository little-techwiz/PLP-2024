try:
    #create a new text file in write mode
    with open("my_file.txt", 'w') as file:
        # Writing three lines of text to the file
        file.write("Hello, welcome to Python\n")
        file.write("Python is a beginner friendly programming language\n")
        file.write("Python is awesome!\n")
    
    #read and display the contents of the file
    with open("my_file.txt", 'r') as file:
        print("Content of my_file.txt:")
        print(file.read())

    #open the file in append mode and appending three more lines of text
    with open("my_file.txt", 'a') as file:
        file.write("Experience Python's artistry as it crafts a literary masterpiece \n")
        file.write("With each line of code, Python breathes life into programs\n")
        file.write("Witness the magic of Python\n")

    #read and display the updated contents of the file
    with open("my_file.txt", 'r') as file:
        print("\nUpdated content of my_file.txt:")
        print(file.read())

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    print("File handling operation completed.")
