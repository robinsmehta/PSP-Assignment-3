# 2. Write a program to copy the contents of one file to another.

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(content)
        print(f"Contents copied from '{source_file}' to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' was not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")

# Example usage
if __name__ == "__main__":
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")
    copy_file(source, destination)
