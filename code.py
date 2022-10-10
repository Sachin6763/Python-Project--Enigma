import numpy as np
from Encryption import encryption
from function import bina, function
from Key_generation import key
from array_to_text import arr_str

def code(M,b):

# Step 1 : Defining K and Plain Text 

    K= [ 0,0,0,1,    0,0,1,1,    0,0,1,1,    0,1,0,0,
         0,1,0,1,    0,1,1,1,    0,1,1,1,    1,0,0,1,
         1,0,0,1,    1,0,1,1,    1,0,1,1,    1,1,0,0,
         1,1,0,1,    1,1,1,1,    1,1,1,1,    0,0,0,1  ]


# Step 2 : Calling funtion "key" for generating keys 

    K1_16= key(K)


# Step 3 : Using keys making Cipher Text  ---> Encryption

    IP_inverse = encryption(K1_16,M,1)
    print("Encrypted code= ",IP_inverse)
    print("Cipher Text= ", end='')
    Cipher_text= IP_inverse.reshape(1,64)
    b=1
    arr_str(Cipher_text,b)                        
 


# Step 4 : Converting plain text into Cipher Text ---> Decryption 

    K16_1=np.arange(16*48).reshape(16,48)

    for i in range(16):
        K16_1[i]=K1_16[15-i]

    M1= encryption ( K16_1,IP_inverse,2)

#  print("Decrypted Code= ",M)

    return M
