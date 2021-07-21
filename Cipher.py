alpha = 'abcdefghijklmnopqrstuvwxyz'
def caesar_encrypt(word:str, key:int) -> str:
    """
    Encrypt word by shifting each character by key index
    Arguments:
    word -- input word to be encrypted
    key -- shifting positions
    Return:
    ciphertext -- encrypted word
    
    """
    ciphertext = ''
    for w in word:
        index = alpha.index(w)
        ciphertext += alpha[(index+key)%26]
    return ciphertext

print(caesar_encrypt('yax', 3))
print(caesar_encrypt('max', 5))



    
    
    



 
    
    
    
