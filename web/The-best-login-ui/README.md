# The Best Login UI
- Category: Web
- Tag: `easy`
- Final Score: 432
- Solve: 32/292

## Writeups :eyes:
### Observation
- From the source code we know that it use mongoDB as database.
- There's a classic NoSQL injection on MongoDB.
### Exploit
We can easily byass the login by using some trick (e.g. `username[$ne]=toto&password[$ne]=toto`).

Then, it show no information when login as admin. We only know that if we're login or not. Hence, it's a blind sql injection.

We just iterate through `strings.printable` and find the secret FLAG.