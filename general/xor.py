def xor_string(string, val):
    r = ""
    for c in string:
        r += chr(ord(c) ^ val)
    return r


# XOR Starter
print("XOR Starter:")
s = xor_string("label", 13)
print(s)


# XOR Properties

def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

print("XOR Properties:")

k1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k2_k1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2_k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_k123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

k1 = bytes.fromhex(k1_hex)
k2 = xor_bytes(bytes.fromhex(k2_k1), k1)
k3 = xor_bytes(bytes.fromhex(k2_k3), k2)
flag = xor_bytes(xor_bytes(bytes.fromhex(flag_k123), k1), xor_bytes(k2, k3))

print(flag)

# Favorite Byte
print("Favorite byte:")

b = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
res = ""

for c in range(256):
    for s in b:
        res += chr(c ^ s)
    if res.startswith("crypto"):
        print(res)
        break
    res = ""
