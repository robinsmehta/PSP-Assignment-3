#3. Write a program to find and replace a specific word in a file with another word.

def find_and_replace(file_name, old_word, new_word):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        
        if old_word not in content:
            print(f"'{old_word}' not found in the file.")
            return

        updated_content = content.replace(old_word, new_word)

        with open(file_name, 'w') as file:
            file.write(updated_content)

        print(f"All occurrences of '{old_word}' have been replaced with '{new_word}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")

# Example usage
if __name__ == "__main__":
    filename = input("Enter the file name: ")
    old = input("Enter the word to be replaced: ")
    new = input("Enter the new word: ")
    find_and_replace(filename, old, new)
