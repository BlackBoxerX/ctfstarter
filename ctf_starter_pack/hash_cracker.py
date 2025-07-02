import hashlib

def run():
    hash_input = input("Hash para crackear: ").strip()
    for palavra in ["admin", "123456", "password", "ctf", "flag", "root"]:
        for algo in [hashlib.md5, hashlib.sha1, hashlib.sha256]:
            if algo(palavra.encode()).hexdigest() == hash_input:
                print(f"[+] SENHA ENCONTRADA: {palavra} ({algo.__name__})")
                return
    print("[-] Nenhuma senha fraca encontrada.")
