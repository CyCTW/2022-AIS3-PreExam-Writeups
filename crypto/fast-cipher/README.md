# Fast Cipher
- Category: Crypto
- Tag: `baby`
- Final Score: 100
- Solve: 125/292

## Writeups :eyes:
### Observation
- `(key & 0xFF)` - Only use the 1 bytes of key to encrypt.
### Exploit
Although we don't know the real key, but we know that only 1 byte of key is used. Hence, we can brute force the last byte of key from 0 to 256 and try to decrypt the ciphertext and find the appropriate one. 





