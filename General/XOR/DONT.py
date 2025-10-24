from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(flag, 'crypto{'.encode())) # 'myXORke+y...'
print(xor(flag, 'myXORkey'.encode())) # znalezienie dokladnego klucza

# znajac haslo albo jego czesc mozemy obejsc brak znania klucza
# niech A to ciag bajtow oznaczajacy haslo (u nas zakodowane crypto{...})
# niec K to klucz (nieznany)
# mamy wiec zaszyfrowane: A XOR K
# jezeli ja zrobie z nowu (A XOR K) XOR A = (A XOR A) XOR K = 0 XOR K
# to mi wyjdzie klucz