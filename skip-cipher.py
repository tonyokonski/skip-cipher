# performs a skip cypher. Assume perfect input; no error handling yet. 

import random, getpass  

def scramble():

    chars = '!@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*abcdefghijklmnopqrstuvwxyz!@#$%^&*1234567890!@#$%^&*'
    y = ''
    scrambled = y.join(random.sample(chars,len(chars)))
    
    return scrambled    
    

def random_characters(number):
    i = 0 
    scram_chars = scramble() 
    new_string = ''

    while i < number:
        new_string += scram_chars[random.randint(0,93)]
        i += 1

    return new_string

def key_gen():
    try:
        main_key = int(getpass.getpass('Enter a positive integer as a numerical key: ')) #need try except here
    except ValueError as err:
        print err, '; please enter a positive integer.'
        return key_gen()
    else:
        if main_key < 1:
            print 'Please enter a positive integer.'
            return key_gen()
        else:
            return main_key

def encrypt(msg, key):
    #msg is the string to encrypt and key is the cryptographic key
        
    encrypted_msg = '' # container for the result
    encrypt_tail = random_characters(key) # produces last cypher to be added to msg[-1] to avoid <= index error
    length = len(msg)
    i = 0
    
    while i < length:
        encrypt_cypher = random_characters(key) # generates (key) amount of random letters
        encrypted_msg += (encrypt_cypher + msg[i])
        i += 1
        
    encrypted =  encrypted_msg + encrypt_tail
    
    print 'Encrypted message is:', encrypted

def encrypt_prep():
    
    main_msg = raw_input('Please type in the message that you would like to encrypt and then press ENTER: ')
    
    new_main_msg = ''.join(main_msg.split())
    
    key = key_gen()

    encrypted_message = encrypt(new_main_msg, key)
    
def decrypt(msg, key):
    # msg is the string to decrypt and key is the cryptographic key    
    
    i = 0
    decrypted_msg = ''
    
    while i < len(msg) - key: # skips key number of chars and returns the decrypted string. len(msg) - 1 prevents the loop from exceeding the string index.
        i += key
        decrypted_msg += msg[i]
        i += 1
                
    #print decrypted_msg # for testing purposes
    #print msg # for testing purposes
    
    return decrypted_msg

def secrecy():

    try:
        x = int(raw_input('Encrypt (1) OR decrypt (2): '))        
    except ValueError as err:
        print err, '; please enter a 1 to encrypt or a 2 to decrypt.'
        secrecy()
    else:
        if x == 1:
            encrypt_prep()
        elif x == 2:
            print 'Sent to decryption function'
        else:
            print 'Number entered is not a 1 or 2. Please enter a 1 to encrypt or a 2 to decrypt.'
            secrecy()
                    
if __name__ == '__main__':
    secrecy()
