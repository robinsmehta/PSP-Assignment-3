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

