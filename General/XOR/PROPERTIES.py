KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
K2_XOR_K1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
K2_XOR_K3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FINAL = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

KEY2 = bytes(a ^ b for a, b in zip(K2_XOR_K1, KEY1)) # poprostu XOR KEY1 z KEY2
KEY3 = bytes(a ^ b for a, b in zip(K2_XOR_K3, KEY2)) # analog

combined = bytes(a ^ b ^ c for a, b, c in zip(KEY1, KEY3, KEY2))
FLAG = bytes(a ^ b for a, b in zip(FINAL, combined))

print(FLAG.decode())