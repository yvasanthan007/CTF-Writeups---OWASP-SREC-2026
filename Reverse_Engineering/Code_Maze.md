
┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ python3 -c "import re,base64,zlib; d=re.search(r'data = b\"(.*?)\"',open('obfuscated.py').read()).group(1); print(zlib.decompress(base64.b64decode(d)).decode())"

import sys
password = input("Enter password: ")
if password == "s3cr3t":
    print("Correct! Flag: OWASP{0bfu5c4t10n_m4k3s_1t_h4rd3r}")
else:
    print("Wrong!")
    sys.exit(1)


┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ nano solve.py

┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ python3 solve.py
---- decoded payload ----

import sys
password = input("Enter password: ")
if password == "s3cr3t":
    print("Correct! Flag: OWASP{0bfu5c4t10n_m4k3s_1t_h4rd3r}")
else:
    print("Wrong!")
    sys.exit(1)

---- flag ----
OWASP{0bfu5c4t10n_m4k3s_1t_h4rd3r}

┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ ls
ap-south-1-yvasanthan007-regular.ovpn  blackeye-1  Certifications  obfuscated.py  Overthewire  solve.py  zlib  zphisher

┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ cat solve.py
import re, base64, zlib

src = open("obfuscated.py").read()

# Pull the encoded blob out of the file
blob = re.search(r'data\s*=\s*b["\'](.*?)["\']', src).group(1)

# Decode and decompress, but do NOT exec
payload = zlib.decompress(base64.b64decode(blob)).decode()
print("---- decoded payload ----")
print(payload)

# Grab the flag automatically
flag = re.search(r'[A-Za-z0-9_]+\{.*?\}', payload)
print("---- flag ----")
print(flag.group(0) if flag else "No flag pattern found")

┌──(vasanthan㉿Kali)-[~/Downloads]
└─$ python3 solve.py                                                                                                                                                                                                  
---- decoded payload ----

import sys
password = input("Enter password: ")
if password == "s3cr3t":
    print("Correct! Flag: OWASP{0bfu5c4t10n_m4k3s_1t_h4rd3r}")
else:
    print("Wrong!")
    sys.exit(1)

---- flag ----
OWASP{0bfu5c4t10n_m4k3s_1t_h4rd3r}


Flag retrived: OWASP{0bfu5c4t10n_m4k3s_1t_h4rd3r}