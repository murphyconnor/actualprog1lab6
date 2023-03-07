def encoder(input_string):
    new_string = ""
    for char in input_string:
        char = int(char)
        char += 3
        if char >= 10:
            char = char % 10
        char = str(char)
        new_string += char
    return new_string

def decoder(input_string):
    decoded_string = ""
    for char in input_string:
        char = int(char)
        char -= 3
        if char <= 0:
            char = char  + 10
        char = str(char)
        decoded_string += char
    return decoded_string

def main():
    new_string = encoder(input("Enter an eight-digit string of numbers:"))
    print(f"Encoded password: {new_string} ")
    decoded_string = decoder(new_string)
    print(f"Decoded password: {decoded_string} ")

# comment
if __name__ == "__main__":
    main()

