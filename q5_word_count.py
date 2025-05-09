#5. Develop a program that counts the occurrence of each word in a file.
from collections import Counter
import string

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
            # Remove punctuation and convert to lowercase
            text = text.translate(str.maketrans('', '', string.punctuation)).lower()
            
            words = text.split()
            word_counts = Counter(words)
            
            print("\nWord Occurrences:\n")
            for word, count in word_counts.items():
                print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file name (e.g., text.txt): ").strip()
    count_words_in_file(file_path)
