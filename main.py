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
        print(len(words), 'words found in the document\n')
        
        # Initialize an empty dictionary to hold character counts
        characters = {}
        
        # Iterate over each character in the file, converted to lowercase
        for char in file_contents.lower():
            # Check if the character is an alphabet letter
            if char.isalpha():
                # If the character is not yet in the dictionary, add it with a count of 1
                if char not in characters:
                    characters[char] = 1
                # If it is already in the dictionary, increment its count
                else:
                    characters[char] += 1
        
        # Sort characters by their counts in descending order and convert to a list of tuples
        sorted_chars = sorted(characters.items(), key=lambda x: x[1], reverse=True)
        
        # Print each character and its count
        for char, count in sorted_chars:
            print(f"The '{char}' character was found {count} times")
    
    # Print the footer for the report
    print('--- End report ---')
    
if __name__ == "__main__":    
    main()