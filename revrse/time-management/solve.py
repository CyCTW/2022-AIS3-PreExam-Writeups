

secrets = ['33534941', '1', '6F6F687B', '9', '5F796172', '5', '69727473', '6', '5F73676E', '8', '615F7369', 'B', '7961776C',  '7', '6E615F73', '2', '6573755F', '4', '5F6C7566', '0', '6D6D6F63', '0A', '7D646E61', '3']
keys = ['3A011001', '0', '3104321A', '454F40', '41D1432', '3A0B002D', '0C1A002C', '0D3E1103', '2C120A31', '1A003100', '4C4C1B0D', '3E2D161D']
a = bytes.fromhex('33534941')
print(a)

flag = ""

for i in range(0, 23, 2):
    v4 = int(secrets[i], 16) ^ int(keys[ int(secrets[i+1], 16) ], 16)
    # print(v4)
    a = bytes.fromhex(hex(v4)[2:])
    flag += a[::-1].decode()
print(flag)
