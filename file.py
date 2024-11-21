def modify_content(content):
    
    return content.title()

def file_read_write():
    
    # Ask the user for the filename to read
    input_filename = input("Enter the filename to read: ")

    try:
        # Try reading the file
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_content(content)

        # Generate a new filename for the modified content
        output_filename = f"new_{input_filename}"
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{input_filename}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
file_read_write()
