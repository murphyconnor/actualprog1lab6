# Connor Murphy
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


def decoder(new_string):
    # converts encoder result into an iterable list to be used in the for loop
    encoded_string_list = list(new_string)
    decoded_string = ''
    # loops through each character(number) of the encoded password and performs appropriate operation to decode
    for char in encoded_string_list:
        char = int(char)
        if 0 <= char <= 2:
            char += 7
            char = str(char)
            decoded_string += char
        elif 3 <= char <= 9:
            char -= 3
            char = str(char)
            decoded_string += char
    # returns the decoded password
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
