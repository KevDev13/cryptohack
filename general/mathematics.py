# GCD

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

print(gcd(66528, 52920))

# Extended GCD
def ext_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quot = old_r // r
        old_r, r = r, old_r - (quot * r)
        old_s, s = s, old_s - (quot * s)
        old_t, t = t, old_t - (quot * t)

    return old_s, old_t

print("\nExtended GCD:")
p = 26513
q = 32321
print(ext_gcd(p, q))

# Modular Arithmetic 1
print("\nModular Arithmetic 1")
print(11 % 6)
print(8146798528947 % 17)

# Modular Arithmetic 2
print("\nModular Arithmetic 2")
print("done by hand... Fermat's Little Theorem!")

# Modular Inverting
print("\nModular Inverting")

def mod_power(x, y, m):
    if y == 0:
        return 1
    p = mod_power(x, y // 2, m) % m
    p = (p * p) % m
    if y % 2 == 0:
        return p
    else:
        return (x * p) % m

def mod_inverse(d, p):
    if gcd(d, p) != 1:
        print("inverse doesn't exist")
    else:
        return mod_power(d, p-2, p)
        
print(mod_inverse(3, 13))
