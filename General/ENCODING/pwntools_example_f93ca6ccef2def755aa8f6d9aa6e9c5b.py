from pwn import *
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def utf8_dec(array):
    literki = ""
    for num in array:
        literki += chr(num)
    return literki

def hex_dec(string):
    literki = ""
    for i in range(0, len(string), 2):
        literki += chr(int(string[i:i+2], 16))
    return literki

def b64_dec(string):
    import base64
    literki = base64.b64decode(string)
    return literki.decode() 

def int_dec(msg):
    hex_value = hex(msg)
    ascii_value = bytes.fromhex(hex_value[2:]).decode('utf-8')
    return ascii_value



received = json_recv()

while "flag" not in received or "error" not in received:
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    if received["type"] == "utf-8":
        decoded = utf8_dec(received["encoded"])
    elif received["type"] == "hex":
        decoded = hex_dec(received["encoded"])
    elif received["type"] == "base64":
        decoded = b64_dec(received["encoded"])
    elif received["type"] == "bigint":
        decoded = int_dec(int(received["encoded"], 0))
    elif received["type"] == "rot13":
        import codecs
        decoded = codecs.decode(received["encoded"], 'rot_13')
    print("Decoded value: ")
    print(decoded)

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

    received = json_recv()