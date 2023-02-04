# this is work on linux operating system
# import crypt module
import crypt
crypt.crypt("cyber","HX")

# this is work on windows operating system
# import maskpass module
import maskpass
pwd = maskpass.askpass(mask=" ")
print(pwd)

import maskpass
pwd = maskpass.advpass()
print('Password : ', pwd)

# base64 encoding
string = "cybersecurity"
x = string.encode("UTF-8")
print(x)

# advance encrypting method
import base64
string = "CyberSecurity"
encode = base64.b64encode(string.encode("utf-8"))
print("str-byte :", encode)

# advance decrypting method
import base64
string = "CyberSecurity"
decode = base64.b64encode(string.encode("utf-8"))
print("str-byte :", decode)
