# Knock
- Category: Misc
- Tag: `baby`
- Final Score: 100
- Solve: 46/292

## Writeups :eyes:
### Observation
- After submitting `CTF token` to the website, it knock the VPN Client IP.
### Exploit
The website only tell us that it has knock our VPN Client IP. In order to check the request, we can use `wireshark` to intercept the packets send to VPN Client IP.