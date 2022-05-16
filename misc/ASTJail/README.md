# ASTJail
- Category: Misc
- Tag: `baby`
- Final Score: 100
- Solve: 4/292

## Writeups :eyes:
### Observation
- AST Document [link](https://docs.python.org/3.10/library/ast.html) in source 
code

### Exploit
Carefully check the `chal.py` and find if there is any AST type check is missing. 

In `ast.Slice`, the source code only check its `lower` and `upper` child node, which lost the check of `step` child node!

Then, we can try to build a exploit payload e.g. `[1, 2][1:2:<payload>]` and get remote code execution.

> Note: 
See the document and the source code carefully! 
I have seen at least three times of Document and source code. 