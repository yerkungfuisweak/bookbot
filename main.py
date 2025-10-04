from stats import get_num_words, get_char_count
def main():
    # Open the file within a context manager to ensure it's properly closed after reading
    with open("books/frankenstein.txt") as f:
        # Print the heading for the report with the actual file name
        print(f"--- Begin report of {f.name} ---")
        
        # Read all the contents of the file into a single string
        file_contents = f.read()
        
        # Split the contents into a list of words
        words = file_contents.split()
        
        # Print the number of words found in the document
        print(f"Found {len(words)} total words found in the document\n")
        
        characters = get_num_words(file_contents)
        get_char_count(characters)
    
    # Print the footer for the report
    print('--- End report ---')
    
if __name__ == "__main__":    
    main()