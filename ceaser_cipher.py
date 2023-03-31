import time


def get_cipher():
    try:
         cipher = int(input("\nWhat's your cipher? (lucky number?): "))
    except ValueError as e:
         print((f"Cipher cannot be a word, must be a digit"))
    else:
         return cipher

def welcome_message():
     return "Hello there, I am ceaser cipher \nI'll assist you keep your secrets."


def get_Secret():
     secret = input("""What's your secret : """)
     return secret

class SecretError(Exception):
     pass


def word_reserve(cipher:int, secret_word:str):
    try:
        if type(cipher) is not int:
             raise ValueError
        if secret_word.isalpha() == False:
             raise SecretError
        # punctuation
        punctuations = [" ",".",",","'","(",")","\n",":","/","?"]

        #alphabets in lower case and uppercase
        alphabet_lower = ["a", "b", "c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        alphabet_upper = ["A,", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


        # placeholder for encrypted word
        word = ""

        # pick each letter 
        for letter in secret_word:
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
    except ValueError:
         print("cipher needs to be a number")

    except SecretError:
         print("Secrets cannot contain numbers at the moment")
    else:
        return word 
         
         
if __name__ == "__main__":
     print(word_reserve(1,"coq2w"))
     
    
