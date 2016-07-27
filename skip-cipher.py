# performs a "skip-cypher."  

import random, getpass  

def scramble():
    # creates a randomized string of characters.

    chars = '!@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*abcdefghijklmnopqrstuvwxyz!@#$%^&*1234567890!@#$%^&*'
    y = ''
    scrambled = y.join(random.sample(chars,len(chars)))
    
    return scrambled    
    

def random_characters(number):
    # asks scramble() to return a set of character with number length

    i = 0 
    scram_chars = scramble() 
    new_string = ''

    while i < number:
        new_string += scram_chars[random.randint(0,93)]
        i += 1

    return new_string


def key_gen():
    # ensures that the user enters the correctly formatted key
    
    try:
        main_key = int(getpass.getpass('Enter a positive integer as a numerical key: ')) 
    except ValueError as err:
        print err, '; please enter a positive integer.'
        print
        return key_gen()
    else:
        if main_key < 1:
            print 'Please enter a positive integer.'
            print
            return key_gen()
        else:
            return main_key


def encrypt(msg, key):
    #encrypts the desired message. msg is the string to encrypt and key is the cryptographic key
        
    encrypted_msg = '' # container for the result
    encrypt_tail = random_characters(key) # produces last cypher to be added to msg[-1] to avoid <= index error
    length = len(msg)
    i = 0
    
    while i < length:
        encrypt_cypher = random_characters(key) # generates (key) amount of random letters
        encrypted_msg += (encrypt_cypher + msg[i])
        i += 1
        
    encrypted =  encrypted_msg + encrypt_tail
    print '*******'
    print
    print 'Encrypted message is:', encrypted
    print
    print '*******'


def encrypt_prep():
    # removes spaces from the message, calls key_gen() to create the key, then sends both data to encryption function. Removing spaces
    # was a requirement for the class assignment that this project is based upon. May or may not remove this requirement later.

    main_msg = raw_input('Please type in the message that you would like to encrypt and then press ENTER: ')
    
    new_main_msg = ''.join(main_msg.split())
    
    key = key_gen()

    encrypted_message = encrypt(new_main_msg, key)
    

def decrypt():
    # decrypts a message that was encrypted by this program

    msg = raw_input('Please type in or paste the message that you would like to decrypt and then press ENTER: ' )
    i = 0
    decrypted_msg = ''
    key = key_gen()
    
    while i < len(msg) - key: 
        i += key
        decrypted_msg += msg[i]
        i += 1
    print '*******'
    print
    print 'Decrypted message is:', decrypted_msg
    print
    print '*******'


def secrecy():
    # starts the program and asks user whether to encrypt or decrypt. Error checks and sends answer to the appropriate functions.
    try:
        x = int(raw_input('Encrypt (1) OR decrypt (2): '))        
    except ValueError as err:
        print
        print err, '; please enter a 1 to encrypt or a 2 to decrypt.'
        secrecy()
    else:
        if x == 1:
            encrypt_prep()
        elif x == 2:
            decrypt()
        else:
            print
            print 'Number entered is not a 1 or 2. Please enter a 1 to encrypt or a 2 to decrypt.'
            secrecy()
                    

if __name__ == '__main__':
    secrecy()
