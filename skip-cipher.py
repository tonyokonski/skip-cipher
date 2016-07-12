# performs a skip cypher. Assume perfect input; no error handling yet. 

import random  

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
        
    #print encrypt_cypher # for testing purposes
    #print 'Encrypted message is:', encrypted_msg  # for testing purposes
        
    return encrypted_msg + encrypt_tail


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

def main():
    # drives the program
    
    choice = int(raw_input('Encrypt (1) or Decrypt (2): '))
    main_msg = raw_input('Message: ')
    new_main_msg = ''
    main_key = int(raw_input('Key: '))
    i = 0   
    
    if choice == 1: # if spaces are in the string, removes spaces and sends string to encrypt function. Else sends string to encrypt function.
        while i < len(main_msg): # need to account for main_msg[-1] == ' '
            if main_msg[i] == ' ':
                i += 1
                new_main_msg += main_msg[i]
            else:
                new_main_msg += main_msg[i]
                
            i += 1
            
            encrypted_message = encrypt(new_main_msg, main_key)
            
        #print new_main_msg # for testing purposes        

        print # prints an empty line
        print 'Encrypted message:', encrypted_message        
    else:
        decrypted_message = decrypt(main_msg,main_key) # as per instructions, the cypher to decrypt will not have spaces. User provides the random values * key between each letter.
        
        print # prints an empty line
        print 'Decrypted message:', decrypted_message
        
main()

# Prep for re-doing the initial function

#def secrecy():
#
#    try:
#        x = int(raw_input('Encrypt (1) OR decrypt (2): '))        
#    except ValueError as err:
#        print err, '; please enter a 1 to encrypt or a 2 to decrypt.'
#        secrecy()
#    else:
#        if x == 1:
#            print 'Sent to encryption funcion'
#        elif x == 2:
#            print 'Sent to decryption function'
#        else:
#            print 'Number entered is not a 1 or 2. Please enter a 1 to encrypt or a 2 to decrypt.'
#            secrecy()
#                    
#if __name__ == '__main__':
#    secrecy()
