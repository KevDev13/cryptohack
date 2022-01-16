# import base64

# h = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
# b64 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# b = base64.b64encode(bytes.fromhex(b64))

# print(b)

# Bytes and Big Ints

from Crypto.Util.number import *

msg_as_int = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
msg_bytes = long_to_bytes(msg_as_int)
print(msg_bytes)
