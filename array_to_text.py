def arr_str(ar,b):

# Step 1 : Converting integer array to binary string

    dec_binary=""

    for i in range(b):
        for j in range(64):
            dec_binary+= str(ar[i][j])



# Step 2 : Converting binary string into text

    dec_str= ""

    def binary_string(ss):
        sum=0
        for x in range(len(ss)):
            sum+= (int(ss[len(ss)-1-x]))*(2**x)
        ch= chr(sum)
        return ch

    for x in range(len(dec_binary)//8) :
        dec_str+=binary_string(dec_binary[x*8:(x+1)*8])

    print(dec_str)