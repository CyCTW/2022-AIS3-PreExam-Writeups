# subsitution cipher


a = open('cipher.py', 'r')
b = open('cipher.py.enc', 'r')

mp = {}

while 1:
    a1 = a.read(1)
    b1 = b.read(1)
    if not a1:
        break
    mp[b1] = a1

flag_enc = '5xvJ{IVnCDwT_I24t6W626DVw_ODPzJi_FDMz_awVFw_PWmDw6J86_m66cOa}'

flag = ""
for i in flag_enc:
    flag += mp[i]
print(flag)





