def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        characters = {}
        for char in file_contents.lower():
            if char not in characters:
                characters[char] = 1  # First time seeing this character
            else:
                characters[char] += 1  # Add one to the existing count
    print(characters)
if __name__ == "__main__":    
    main()

