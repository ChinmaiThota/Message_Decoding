import sys                                                  # importing sys module

def generate_keys():                                        # initializing and defining generate_keys function
    keys = []
    for i in range(1, 8):
        for j in range((2 ** i) - 1):
            key = bin(j)[2:].zfill(i)
            if key != ('1' * i):
                keys.append(key)
    return keys

def mapping(header):                                        # initializing and defining mapping function
    key_to_char = {}                        
    keys = generate_keys()                  
    for i in range(len(header)):
        key_to_char[keys[i]] = header[i]
    return key_to_char
    
def decoding(encoded_message, key_to_char):                 # initializing and defining decoding function
    decoded_message = ""
    key_length = int(encoded_message[:3], 2)
    i = 3
    while key_length != 0:
        while encoded_message[i:i+key_length] != ("1" * key_length):
            key = encoded_message[i:i+key_length]
            decoded_message += key_to_char[key]
            i += key_length
        i += key_length
        key_length = int(encoded_message[i:i+3], 2)
        i += 3
    return decoded_message


header = sys.argv[1]                                          # providing input from command line
enc = sys.argv[2]
key_to_char = mapping(header)
print(decoding(enc, key_to_char))



