import base64, codecs, urllib.parse

def run():
    print("1- Base64 decode/encode")
    print("2- Rot13 decode/encode")
    print("3- Hex decode/encode")
    print("4- URL decode/encode")
    op = input("Escolha: ")
    if op == "1":
        txt = input("Texto: ")
        modo = input("d=decode, e=encode: ")
        if modo == "d":
            print(base64.b64decode(txt).decode())
        else:
            print(base64.b64encode(txt.encode()).decode())
    elif op == "2":
        txt = input("Texto: ")
        print(codecs.encode(txt, 'rot_13'))
    elif op == "3":
        txt = input("Texto: ")
        modo = input("d=decode, e=encode: ")
        if modo == "d":
            print(bytes.fromhex(txt).decode())
        else:
            print(txt.encode().hex())
    elif op == "4":
        txt = input("Texto: ")
        modo = input("d=decode, e=encode: ")
        if modo == "d":
            print(urllib.parse.unquote(txt))
        else:
            print(urllib.parse.quote(txt))
