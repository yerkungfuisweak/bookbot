def get_num_words(file_contents):
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
    return characters