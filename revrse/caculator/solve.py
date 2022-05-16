
# print(len(arr))
# ans = ""
# for v in arr:
#     ans += chr(ord(':') ^ v)
# print(ans)

# # 0T_N3T_FRAm3W0rk

# arr2 = [9, 52, 8, 13, 7, 5, 48, 87, 0]
# ans2 = ""
# for v in arr2:
#     ans2 += chr(ord('d') ^ v)
# print(ans2)
# mPlicaT3d (9~17)
# length: 45 = 3 + 
# AIS3{0T_N3T_FRAm3W0rm PlicaT3d G_G}
# G_G}

def pt(arr):
    print("".join(arr))

# 1. 1-45
flag1 = [ '%' for _ in range(45)]
flag1[14] = 'A'
flag1[3] = '{'
for i, val in enumerate([30, 4, 100]):
    flag1[i] = chr(ord('W') ^ val)
pt(flag1)

flag4 = [ '%' for _ in range(41)]
flag4[40] = '}'
flag4[0] = 'D'
for i, val in enumerate([5, 29, 5]):
    flag4[37 + i] = chr(ord('B') ^ val)
pt(flag4)

# 2. 
flag2 = ['%' for _ in range(36)]
flag2[35] = '_'
flag2[34] = '_'
flag2[15] = 'k'
arr2 = [10, 110, 101, 116, 9, 110, 101, 124, 104, 123, 87, 9, 109, 10, 72]
for i in range(15):
    val = arr2[i]
    flag2[i] = chr(ord(':') ^ val)
pt(flag2)

# 3. 
flag3 = ['%' for _ in range(18)]
flag3[0] = flag3[6] = flag3[3] = '_'
flag3[5] = flag3[8] = '0'
flag3[7] = 'C'
flag3[4] = 'S'
arr3 = [9, 52, 8, 13, 7, 5, 48, 87, 0]
for i in range(9):
    val = arr3[i]
    flag3[i + 9] = chr(ord('d') ^ val)
pt(flag3)

# 4. IS3{_xx_S0_C0mPlicaT3d
# 0T_N3T_FRAm3W0rkxxxxxxxxxxxxxxxxxx__
# ________________xx_S0_C0mPlicaT3d__G_G}
# AIS3{D0T_N3T_FRAm3W0rk_15_S0_C0mPlicaT3d__G_G}