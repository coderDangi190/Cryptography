DT="I love You "
key = 4
CT = ""

for c in DT:
    if c.islower:
        CT += chr((ord(c)+key-97)%26+97);

    elif c.isupper:
        CT += chr((ord(c)+key-65)%26+65);

    else: 
        CT += c;

print(f"Plane_text:{DT}");
print(f"Cipher_text:{CT}");