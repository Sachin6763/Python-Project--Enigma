import numpy as np 
from code import code
from array_to_text import arr_str


# Step 1 : Inputing the String from user

str1= input("Enter the text which you want to send ")

a= len(str1)
a1= a%8

if a1!=0:
    for i1 in range(8-a1):
        str1+='\0'


# Step 2 : Converting it into binary

bin = ''.join(format(ord(i), '08b') for i in str1)


b=len(bin)//64        # b -- > divider kitne parts me bhegana hai
c=len(bin)




# Step 3 : Sending 64 Bit each for encryption and decryption 

rounds =np.arange(b*64).reshape(b, 64)

for x in range(b):
    for y in range(64):
        rounds[x][y]= int(bin[y+x*64])




# Step 4 : Sending each 64 bit for encryption and decryption in the form of integer array and Getting Decrypted integer array 

dec_array=np.arange(b*64).reshape(b,64)

for x in range(b):
   dec_array[x]= code(rounds[x],b)            # call to function code for Encryption + Decryption



# Step 5 : Converting array of integers to text

print("Decrypted Text= ", end='')
arr_str(dec_array,b)                        # call to function arr_str for converting array of integers to text







