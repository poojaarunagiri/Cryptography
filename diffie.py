# Diffie-Hellman Key Exchange

p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))

a = int(input("Enter private key of User a: "))
b = int(input("Enter private key of User b: "))

x = (g ** a) % p
y = (g ** b) % p

print("\nPublic key of User a:", x)
print("Public key of User y:", y)

key_x = (y ** a) % p
key_y = (x ** b) % p

print("\nSecret key computed by User A:", key_x)
print("Secret key computed by User B:", key_y)

if key_x == key_y:
    print("\nKey Exchange Successful! Shared Secret Key =", key_x)
else:
    print("\nKey Exchange Failed!")
