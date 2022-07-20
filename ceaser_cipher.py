import time

print("""
Hello there, I am ceaser cipher
I'll assist you keep your secrets.""")


# user cipher
cipher = int(input("\nWhat's your cipher? (lucky number?): "))

# user secret
secret = input("""What's your secret : """)

# punctuation
punctuations = [" ",".",",","'","(",")","\n",":","/","?"]

#alphabets in lower case and uppercase
alphabet_lower = ["a", "b", "c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet_upper = ["A,", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# placeholder for encrypted word
word = ""

# pick each letter 
for letter in secret:
        if letter in alphabet_lower:
            #identify current position of letter
            position = alphabet_lower.index(letter)
            # move to new position
            new_position = position + cipher
            # loop continuously through alphabet_lower's index
            if new_position > 25:
                new_position = new_position - 26
            # encrypted word
            word += alphabet_lower[new_position]
        elif letter in alphabet_upper:
                 #identify current position of letter
                 position = alphabet_upper.index(letter)
                 # move to new position
                 new_position = position + cipher
                 # loop continuously through alphabet_upper's index
                 if new_position > 25:
                     new_position = new_position - 26
                 # encrypted word
                 word += alphabet_upper[new_position]
        # punctuations retain original position
        elif letter in punctuations:
            word += letter   


print("Your coded word is:\n")

print(word)
