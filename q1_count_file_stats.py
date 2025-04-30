#1. Write a program to count the number of lines, words, and characters in a text file.
def count_file_contents(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)

            print(f"Lines: {line_count}")
            print(f"Words: {word_count}")
            print(f"Characters: {char_count}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = input("Enter the filename: ")
count_file_contents(filename)
