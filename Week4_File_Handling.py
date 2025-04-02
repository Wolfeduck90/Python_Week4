try:
    # Open the input file in read mode and the output file in write mode.
    # This ensures that we can read data from one file and write the processed data to another. Specifying encoding helps the program to read the files.
    with open("input.txt", "r", encoding="utf-8") as infile, open("output.txt", "w", encoding="utf-8") as outfile:
        # Use enumerate to iterate through each line of the input file,
        # while also keeping track of the line numbers.
        for line_number, line in enumerate(infile, start=1):
            if line_number == 1:  # This is the line to be modified
                # Modify the specific line (e.g., changing line 1).
                outfile.write("Today's society sacrifices on the altar of functionalism\n")
            else:
                # For all other lines, write them as they are.
                outfile.write(line)
except FileNotFoundError:
   # Handle the error if the input file does not exist.
    # Print a message to inform the user about the missing file.
    print("The input file does not exist.")

while True:
    try:
        # Ask the user for a filename to read from. This allows dynamic input and customization.
        filename = input("Enter the filename: ")
        
        # Attempt to open the file in read mode, specifying coding as vscode gave me grey hairs trying to figure that out.
        with open(filename, "r", encoding="utf-8") as file:
            # If successful, read the file content and display a success message.
            content = file.read()
            print("File content successfully read.")
            break  # Exit the loop after successfully reading the file.
    except FileNotFoundError:
        # Handle the error if the file does not exist.
        print("Error: File not found. Please try again.")
    except IOError:
        # Handle errors related to file permissions or other input/output issues.
        print("Error: File cannot be read. Please check permissions.")
