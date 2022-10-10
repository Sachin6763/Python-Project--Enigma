import numpy as np
from function import bina, function
from Key_generation import key


def encryption(K1_16,M,ch ):


# Step 1: Defining IP of 64 bit

    IP= [ 58,    50,   42,    34,    26,   18,    10,    2,
          60,    52,   44,    36,    28,   20,    12,    4,
          62,    54,   46,    38,    30,   22,    14,    6,
          64,    56,   48,    40,    32,   24,    16,    8,
          57,    49,   41,    33,    25,   17,     9,    1,
          59,    51,   43,    35,    27,   19,    11,    3,
          61,    53,   45,    37,    29,   21,    13,    5,
          63,    55,   47,    39,    31,   23,    15,    7   ]



# Step 2: Applying initial permutations IP on M --> 64 bit


    IP1= np.arange(64)

    for i in range(64):
        IP1[i]=M[(IP[i]-1)]
        


# Step 3: Divide IP1 into L0 and R0 each of 32 bit

    L0= np.arange(32)
    R0= np.arange(32)

    for i in range(64):
        if(i <32):
            L0[i]=IP1[i]
        else:
            R0[i-32]=IP1[i]



# Step 4: Defining L1-16 and R1-16


    L0_16= np.arange(17*32).reshape(17,32)
    R0_16= np.arange(17*32).reshape(17,32)
    for x in range(32):
        R0_16[0][x]=R0[x]
        L0_16[0][x]=L0[x]


# Step 5: Calculating L16 and R16

    s=np.arange(32)

    for p in range(16):
        s=function(R0_16[p],K1_16[p])

        for x in range(32):
            R0_16[p+1][x] =((L0_16[p][x] + s[x])%2)
            L0_16[p+1]=R0_16[p]



# Step 6: Assigning IP(inverse) and calculating it

    IP_1= [    40,     8,   48,    16,    56,   24,    64,   32,
               39,     7,   47,    15,    55,   23,    63,   31,
               38,     6,   46,    14,    54,   22,    62,   30,
               37,     5,   45,    13,    53,   21,    61,   29,
               36,     4,   44,    12,    52,   20,    60,   28,
               35,     3,   43,    11,    51,   19,    59,   27,
               34,     2,   42,    10,    50,   18,    58,   26,
               33,     1,   41,     9,    49,   17,    57,   25    ]


    R16L16 = np.arange(64)

    for i in range(64):
        if i<32:
            R16L16[i] =R0_16[16][i]
        else:
            R16L16[i] =L0_16[16][i-32] 


    IP_inverse= np.arange(64)

    for j in range(64):
        IP_inverse[j]= R16L16[IP_1[j]-1]

  
    return IP_inverse 



