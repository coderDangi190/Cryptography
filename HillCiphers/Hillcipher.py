import numpy as np
import math as mt

PT = "Pay More Money"
key = "rrfvsvcct"
PT= PT.replace(" ","")
PT = PT.lower()
# print(PT)

#dictinary making
chartoNum = {chr(i):i-97 for i in range(97,123)};
Numtochar = {i-97:chr(i) for i in range(97,123)};

# print(chartoNum)
# print(Numtochar)
keyintoNumber = [chartoNum[c] for c in key];
PTintoNumber = [chartoNum[c] for c in PT];

# print(keyintoNumber);
# print(PTintoNumber);

BL = round(mt.sqrt(len(key)));
print(BL);

keyMatrix  = np.array(keyintoNumber).reshape(BL,BL)
print(keyMatrix);
PTarray = np.array(PTintoNumber);
print(PTarray);
PTBlock = np.split(PTarray, len(PTintoNumber)/BL);
print(PTBlock);
CTBlock = [np.matmul(PTBlock[i],keyMatrix)%26 for i in range(len(PTBlock))]
print(CTBlock);

CTNumber = np.concatenate(CTBlock);
# print(CTNumber);
CT = [Numtochar[i] for i in CTNumber];
CT = "".join(CT);
print(f"{CT}");

#decryption of hill cipher started
#We already have CT, CTBlock, Keymatrix
k_inv = np.linalg.inv(keyMatrix);
k_det = round(np.linalg.det(keyMatrix));
print(k_inv)
print(k_det)

adj_k = k_inv*k_det %26
print(adj_k)

k_det_mul_inv = pow(k_det,-1,26)
print(k_det_mul_inv);

k_matr_mul_inv = k_det_mul_inv*adj_k%26;
print(k_matr_mul_inv)

PT_block = [np.matmul(CTBlock[i],k_matr_mul_inv)%26 for i in range(len(CTBlock))];
print(PT_block);

PT_list = np.concatenate(PT_block);
print(PT_list);

PT = " "
for i in PT_list:
    if round(i) == 26:
        PT += Numtochar[0];
    else:
        PT += Numtochar[round(i)];
print(f"Plain_text:- {PT}");
print(f"Cipher_text:- {CT}");
