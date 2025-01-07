import numpy as np
import math as ma

#key Value pair dictionary

chartonumber = {chr(i): i-97 for i in range(97,123)} #lowercase letter
numbertochar = {i-97:chr(i) for i in range(97,123)} #lowercase letter

print(f"{chartonumber}");
print(f"{numbertochar}");

PT = "Pay More Money"
key = "rrfvsvcct"

PT = PT.replace(" ", "")
PT = PT.lower()

PT_number =[chartonumber[i] for i in PT] # list of plain text into number
key_number =[chartonumber[i] for i in key]#list of key into number

print(f"{PT_number}");
print(f"{key_number}");

#check given matrix is square or not

BL = round(ma.sqrt(len(key_number)))
print(BL);

key_matrix = np.array(key_number).reshape(BL, BL) #reshaping matrix size 3x3
print(key_number);

PT_array = np.array(PT_number);
print(PT_array);

PT_block = np.split(PT_array, len(PT_array)/BL)
print(PT_block);

#now starting multiplication as per the encryption algorithm
#CT = PT * K % 26
#CT = matrix in result
#PT = matrix
#K = square matrix

CT_block = [np.matmul(PT_block[i],key_matrix)%26 for i in range(len(PT_block))];
print(CT_block);

CT_array = np.concatenate(CT_block)
print(CT_array);


#chaning number into character
CT_list = [numbertochar[i] for i in CT_array]
print(CT_list)

CT = ''.join(CT_list)
print(f"plain_text:{PT}")
print(f"Cipher_text:{CT}")

