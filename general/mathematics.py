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
