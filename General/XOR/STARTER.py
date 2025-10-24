s = "label"
key = 13
parts = []
for i, ch in enumerate(s):
    orig_ord = ord(ch) # na Unicode
    # 2) binarna reprezentacja tylko do wypisania (string)
    orig_bin = format(orig_ord, "08b")
    # 3) XOR na poziomie liczb (int)
    xored_ord = orig_ord ^ key
    # 4) binarna reprezentacja wyniku (string)
    xored_bin = format(xored_ord, "08b")
    # 5) konwersja wyniku XOR z powrotem na znak
    new_char = chr(xored_ord)
    # 6) dodajemy do listy i wypisujemy szczegóły
    print(new_char)