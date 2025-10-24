hex_str = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
data = bytes.fromhex(hex_str)
for key in range(256):
    out = bytes(b ^ key for b in data)
    print(out)

# prosty brut-force - jesli klucz jest jednym bajtem to xorujemy
# kazdy mozliwy bajt z kazdym mozliwym kluczem (0-255)
# 1 bajt - 8 bitow czyli maks 255 