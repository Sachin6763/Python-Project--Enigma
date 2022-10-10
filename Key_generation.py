import numpy as np


def key(K1):

# Step 1: Assigning K
    K = [  0,0,0,1,    0,0,1,1,    0,0,1,1,    0,1,0,0,
           0,1,0,1,    0,1,1,1,    0,1,1,1,    1,0,0,1,
           1,0,0,1,    1,0,1,1,    1,0,1,1,    1,1,0,0,
           1,1,0,1,    1,1,1,1,    1,1,1,1,    0,0,0,1  ]



# Step 2: Assigning PC1

    PC1= [  57,49,41,33,    25,17,9,1,    58,50,42,34,    26,18,10,2,
            59,51,43,35,    27,19,11,3,   60,52,44,36,    63,55,47,39,
            31,23,15,7,     62,54,46,38,  30,22,14,6,     61,53,45,37,
            29,21,13,5,     28,20,12,4                                   ]



# Step 3: Creating K+

    Kplus=np.arange(0,56)
    for i in range(56):
       Kplus[i]=K[(PC1[i]-1)]


# Step 4: Creating C0

    Czero=np.arange(28)

    for i in range(28):
        Czero[i]=Kplus[i] 



# Step 5: Creating D0

    Dzero=np.arange(28)

    for j in range(28):
        Dzero[j]= Kplus[28+j]




# Step 6: Creating C1,C2,C3.... C16

    C1_16=np.arange(28*16).reshape(16,28)

    NS=  [  1,1,2,2,    2,2,2,2,    
            1,2,2,2,    2,2,2,1  ] 

    sum=0

    for x in range(16):
        sum+=NS[x]

        for y in range(28):
            C1_16[x][y]=Czero[(y+sum)%28]



# Step 6: Creating D1,D2,D3,....16

    D1_16=np.arange(28*16).reshape(16,28)

    sum=0

    for x in range(16):
        sum+=NS[x]

        for y in range(28):
            D1_16[x][y]=Dzero[(y+sum)%28]



# Step 7: Creating C1D1,C2D2,C3D3,... C16D16

    C1_16D1_16=np.arange(56*16).reshape(16,56)

    for i in range(16):
        for j in range(56):
            if(j<28):
                C1_16D1_16[i][j]=C1_16[i][j]
            else:
                C1_16D1_16[i][j]=D1_16[i][j-28]




# Step 8: Assigning PC2

    PC2=  [  14,    17,    11,    24,    1,    5,
              3,    28,    15,     6,   21,   10,
             23,    19,    12,     4,   26,    8,
             16,     7,    27,    20,   13,    2,
             41,    52,    31,    37,   47,   55,
             30,    40,    51,    45,   33,   48,
             44,    49,    39,    56,   34,   53,
             46,    42,    50,    36,   29,   32   ]



# Step 9: Step Creating K1,K2,K3, .. K16

    K1_16=np.arange(48*16).reshape(16,48)

    for m in range(16):
        for n in range(48):
             K1_16[m][n]=C1_16D1_16[m][PC2[n]-1]


# Step 10: Cross Check

    k= [  0,1,1,1,    0,1,0,1,    0,1,1,1,     0,0,0,1,
          1,1,1,1,    0,1,0,1,    1,0,0,1,     0,1,0,0,
          0,1,1,0,    0,1,1,1,    1,1,1,0,     1,0,0,1   ]

    success=0
    for i in range(48):
        if K1_16[11][i]==k[i]:
            success+=1
            continue
        print("Some Error")
        break

    return K1_16
