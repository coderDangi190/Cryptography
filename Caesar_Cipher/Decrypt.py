CT = "grpszirwsyr"
key = 4
DT = ""

for c in DT:
    if c.islower:
        DT += chr((ord(c)+key-97)%26+97);

    elif c.isupper:
        DT += chr((ord(c)+key-65)%26+65);

    else: 
        DT += c;

print(f"Plane_text:{DT}");
print(f"Cipher_text:{CT}");