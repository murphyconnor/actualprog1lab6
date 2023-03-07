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

def printmenu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")

def main():
    while True:
        printmenu()
        print()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            input_string = input("Please enter your password to encode: ")
            new_string = encoder(input_string)
            print("Your password has been encoded and stored!")
        elif user_input == 2:
            decoded_string = decoder(new_string)
            print(f"The encoded password is {new_string}, and the original password is {decoded_string}.")
        elif user_input == 3:
            break

# comment
if __name__ == "__main__":
    main()

